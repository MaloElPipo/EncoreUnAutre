# ============================================================
# MOTEUR DE BACKTEST
# ============================================================
# Teste nos prédictions sur des matchs PASSÉS
# Pour voir si notre modèle aurait généré du profit
#
# Logique :
# 1. On charge des matchs passés avec résultats réels
# 2. On simule nos paris (value bets détectées)
# 3. On calcule le ROI, le taux de réussite, le profit net

from betting.value_finder import calculate_value

# ============================================================
# CONSTANTES DE MISE
# ============================================================
DEFAULT_STAKE = 10  # Mise fixe par pari (en €)

# ============================================================
# SIMULATION D'UN PARI
# ============================================================

def simulate_bet(our_prob, pinnacle_odd, actual_outcome, predicted_outcome, stake=DEFAULT_STAKE):
    """
    Simule un pari unique
    
    our_prob          : notre probabilité (décimal)
    pinnacle_odd      : cote Pinnacle
    actual_outcome    : résultat réel  ('home', 'draw', 'away')
    predicted_outcome : issue sur laquelle on parie
    stake             : mise en €
    
    Retourne : profit/perte en €
    """
    value = calculate_value(our_prob, pinnacle_odd)

    # On ne parie que si value bet détectée
    if value < 0:
        return None

    if actual_outcome == predicted_outcome:
        profit = round((pinnacle_odd - 1) * stake, 2)  # Gain
    else:
        profit = round(-stake, 2)  # Perte

    return {
        "predicted": predicted_outcome,
        "actual":    actual_outcome,
        "odd":       pinnacle_odd,
        "value":     round(value * 100, 1),
        "stake":     stake,
        "profit":    profit,
        "win":       actual_outcome == predicted_outcome
    }

# ============================================================
# BACKTEST COMPLET
# ============================================================

def run_backtest(matches):
    """
    Lance le backtest sur une liste de matchs passés
    
    Chaque match doit avoir :
    {
        "home_team"       : str,
        "away_team"       : str,
        "our_probs"       : { p_home, p_draw, p_away } en %
        "pinnacle_odds"   : { odd_home, odd_draw, odd_away }
        "actual_outcome"  : 'home' | 'draw' | 'away'
    }
    """
    total_bets    = 0
    total_wins    = 0
    total_profit  = 0
    total_staked  = 0
    bet_log       = []

    for match in matches:
        home = match["home_team"]
        away = match["away_team"]

        outcomes = [
            ("home", match["our_probs"]["p_home"] / 100, match["pinnacle_odds"]["odd_home"]),
            ("draw", match["our_probs"]["p_draw"] / 100, match["pinnacle_odds"]["odd_draw"]),
            ("away", match["our_probs"]["p_away"] / 100, match["pinnacle_odds"]["odd_away"]),
        ]

        for outcome, our_prob, pin_odd in outcomes:
            result = simulate_bet(
                our_prob          = our_prob,
                pinnacle_odd      = pin_odd,
                actual_outcome    = match["actual_outcome"],
                predicted_outcome = outcome
            )

            if result:
                total_bets   += 1
                total_staked += result["stake"]
                total_profit += result["profit"]
                if result["win"]:
                    total_wins += 1

                bet_log.append({
                    "match":  f"{home} vs {away}",
                    **result
                })

    roi = round((total_profit / total_staked) * 100, 2) if total_staked > 0 else 0
    win_rate = round((total_wins / total_bets) * 100, 2) if total_bets > 0 else 0

    return {
        "total_bets":   total_bets,
        "total_wins":   total_wins,
        "win_rate":     f"{win_rate}%",
        "total_staked": f"{total_staked}€",
        "total_profit": f"{total_profit}€",
        "roi":          f"{roi}%",
        "bet_log":      bet_log
    }
