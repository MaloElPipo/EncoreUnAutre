# ============================================================
# DÉTECTION DES VALUE BETS
# ============================================================
# Une value bet existe quand NOTRE probabilité > probabilité Pinnacle
#
# Exemple :
# Notre modèle dit    : France gagne à 65%  → fair odd = 1.54
# Pinnacle (sans marge) dit : 58%           → cote = 1.72
# → On pense que France gagne PLUS souvent que Pinnacle
# → La cote 1.72 est sous-évaluée → VALUE BET ✅

from config.settings import VALUE_THRESHOLD, HIGH_VALUE_THRESHOLD

def calculate_value(our_probability, pinnacle_odd):
    """
    Calcule la value d'un pari
    
    our_probability  : notre proba en décimal (ex: 0.65)
    pinnacle_odd     : cote Pinnacle AVEC marge (ex: 1.72)
    
    Formule : Value = (notre_proba × cote_pinnacle) - 1
    Si > 0  → value bet
    Si < 0  → pas intéressant
    """
    value = (our_probability * pinnacle_odd) - 1
    return round(value, 4)

def detect_value_bets(home_team, away_team, our_probs, pinnacle_odds):
    """
    Compare nos probabilités vs Pinnacle sur les 3 issues
    
    our_probs : dict avec p_home, p_draw, p_away en %
    pinnacle_odds : dict avec odd_home, odd_draw, odd_away
    """
    results = []

    matchups = [
        ("home",  home_team,  our_probs["p_home"] / 100, pinnacle_odds["odd_home"]),
        ("draw",  "Nul",      our_probs["p_draw"] / 100, pinnacle_odds["odd_draw"]),
        ("away",  away_team,  our_probs["p_away"] / 100, pinnacle_odds["odd_away"]),
    ]

    for outcome, label, our_prob, pin_odd in matchups:
        value = calculate_value(our_prob, pin_odd)

        if value >= HIGH_VALUE_THRESHOLD:
            tier = "🔥 FORTE VALUE"
        elif value >= VALUE_THRESHOLD:
            tier = "✅ VALUE"
        else:
            tier = None  # Pas intéressant

        if tier:
            results.append({
                "match":    f"{home_team} vs {away_team}",
                "outcome":  label,
                "our_prob": f"{round(our_prob * 100, 1)}%",
                "pin_odd":  pin_odd,
                "value":    f"+{round(value * 100, 1)}%",
                "tier":     tier
            })

    return results

def display_value_bets(value_bets):
    if not value_bets:
        print("  Aucune value bet détectée sur ce match.")
        return

    for bet in value_bets:
        print(f"\n  {bet['tier']}")
        print(f"  Match   : {bet['match']}")
        print(f"  Issue   : {bet['outcome']}")
        print(f"  Notre %  : {bet['our_prob']}")
        print(f"  Cote    : {bet['pin_odd']}")
        print(f"  Value   : {bet['value']}")
