# ============================================================
# CONVERSION PROBABILITÉS → FAIR ODDS
# ============================================================
# Fair Odds = cotes sans la marge du bookmaker
# Exemple : prob 60% → fair odd = 1/0.60 = 1.67

def prob_to_fair_odd(probability):
    """Convertit une probabilité (0-1) en fair odd"""
    if probability <= 0:
        return None
    return round(1 / probability, 3)

def get_fair_odds(home_win_pct, draw_pct, away_win_pct):
    """
    Prend les 3 probabilités en % et retourne les 3 fair odds
    
    Exemple :
    home_win_pct = 55.0
    draw_pct     = 25.0
    away_win_pct = 20.0
    """
    # Conversion % → décimal
    p_home = home_win_pct / 100
    p_draw = draw_pct / 100
    p_away = away_win_pct / 100

    return {
        "fair_odd_home": prob_to_fair_odd(p_home),
        "fair_odd_draw": prob_to_fair_odd(p_draw),
        "fair_odd_away": prob_to_fair_odd(p_away)
    }

def display_fair_odds(home_team, away_team, fair_odds):
    print(f"\n💰 Fair Odds - {home_team} vs {away_team}")
    print(f"  🏠 {home_team} : {fair_odds['fair_odd_home']}")
    print(f"  🤝 Nul        : {fair_odds['fair_odd_draw']}")
    print(f"  ✈️  {away_team} : {fair_odds['fair_odd_away']}")
