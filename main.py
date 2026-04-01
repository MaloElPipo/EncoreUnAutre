# ============================================================
# POINT D'ENTRÉE PRINCIPAL
# ============================================================
# Lance l'analyse complète :
# 1. Récupère les matchs du jour via API
# 2. Calcule nos probabilités (modèle Poisson)
# 3. Récupère les cotes Pinnacle
# 4. Détecte les value bets
# 5. Affiche les résultats

from api.fetch_matches   import get_todays_matches
from api.fetch_odds      import get_pinnacle_odds
from models.poisson      import predict_match
from betting.value_finder import detect_value_bets, display_value_bets
from utils.display       import display_match_header, display_probabilities

# ============================================================
# ANALYSE D'UN MATCH
# ============================================================

def analyse_match(match):
    """
    Pipeline complet pour un match donné
    match : dict avec home_team, away_team, league
    """
    home = match["home_team"]
    away = match["away_team"]

    display_match_header(home, away, match.get("league", ""))

    # --- Étape 1 : Prédiction Poisson ---
    prediction = predict_match(home, away)
    if not prediction:
        print("  ⚠️  Données insuffisantes pour ce match.\n")
        return

    display_probabilities(prediction)

    # --- Étape 2 : Récupération cotes Pinnacle ---
    pinnacle_odds = get_pinnacle_odds(home, away)
    if not pinnacle_odds:
        print("  ⚠️  Cotes Pinnacle indisponibles.\n")
        return

    # --- Étape 3 : Détection value bets ---
    value_bets = detect_value_bets(
        home_team    = home,
        away_team    = away,
        our_probs    = prediction,
        pinnacle_odds = pinnacle_odds
    )

    display_value_bets(value_bets)
    print()

# ============================================================
# LANCEMENT PRINCIPAL
# ============================================================

def main():
    print("\n" + "=" * 55)
    print("     ⚽ FOOTBALL VALUE BET ANALYSER")
    print("=" * 55)

    # Récupère les matchs du jour
    matches = get_todays_matches()

    if not matches:
        print("\n  Aucun match disponible aujourd'hui.\n")
        return

    print(f"\n  {len(matches)} match(s) trouvé(s) — Analyse en cours...\n")

    for match in matches:
        analyse_match(match)

    print("=" * 55)
    print("  ✅ Analyse terminée")
    print("=" * 55 + "\n")

# ============================================================
# EXÉCUTION
# ============================================================

if __name__ == "__main__":
    main()
