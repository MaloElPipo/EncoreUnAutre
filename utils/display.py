# ============================================================
# UTILITAIRES D'AFFICHAGE
# ============================================================
# Fonctions réutilisables pour afficher proprement
# les informations dans le terminal

# ============================================================
# EN-TÊTE D'UN MATCH
# ============================================================

def display_match_header(home, away, league=""):
    """
    Affiche l'en-tête d'un match
    """
    print("-" * 55)
    if league:
        print(f"  🏆 {league}")
    print(f"  ⚽ {home} vs {away}")
    print("-" * 55)


# ============================================================
# PROBABILITÉS
# ============================================================

def display_probabilities(prediction):
    """
    Affiche les probabilités calculées par notre modèle
    prediction : dict retourné par predict_match()
    """
    print(f"\n  📊 Probabilités (Modèle Poisson) :")
    print(f"     🏠 Victoire {prediction['home_team']:<20} : {prediction['p_home']}%")
    print(f"     🤝 Match nul                        : {prediction['p_draw']}%")
    print(f"     ✈️  Victoire {prediction['away_team']:<20} : {prediction['p_away']}%")

    print(f"\n  📌 Score le plus probable : "
          f"{prediction['home_team']} {prediction['most_likely_score']} {prediction['away_team']}")


# ============================================================
# RÉSUMÉ GLOBAL (plusieurs matchs)
# ============================================================

def display_global_summary(total_matches, total_value_bets):
    """
    Affiche un résumé global après analyse de tous les matchs
    """
    print("\n" + "=" * 55)
    print("  📋 RÉSUMÉ GLOBAL")
    print("=" * 55)
    print(f"  Matchs analysés   : {total_matches}")
    print(f"  Value bets trouvés : {total_value_bets}")

    if total_value_bets == 0:
        print("  ℹ️  Aucune opportunité aujourd'hui.")
    else:
        print(f"  ✅ {total_value_bets} opportunité(s) détectée(s) !")
    print("=" * 55 + "\n")


# ============================================================
# SÉPARATEUR
# ============================================================

def separator(char="-", length=55):
    """
    Affiche un séparateur visuel
    """
    print(char * length)
