from elo import get_elo, expected_score

def rate_match(home_team, away_team):
    elo_home = get_elo(home_team)
    elo_away = get_elo(away_team)
    
    prob_home = expected_score(elo_home, elo_away)
    prob_away = expected_score(elo_away, elo_home)
    prob_draw = 1 - abs(prob_home - prob_away)
    
    # Normalisation
    total = prob_home + prob_away + prob_draw
    prob_home /= total
    prob_away /= total
    prob_draw /= total
    
    return {
        "home_win": round(prob_home * 100, 2),
        "draw": round(prob_draw * 100, 2),
        "away_win": round(prob_away * 100, 2)
    }

def display_rating(home_team, away_team):
    rating = rate_match(home_team, away_team)
    print(f"\n📊 {home_team} vs {away_team}")
    print(f"  ✅ Victoire {home_team}: {rating['home_win']}%")
    print(f"  🤝 Match nul: {rating['draw']}%")
    print(f"  ✅ Victoire {away_team}: {rating['away_win']}%")
