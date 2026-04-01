# ============================================================
# SYSTÈME ELO - Calcul et mise à jour des ratings
# ============================================================

from config import DEFAULT_ELO, HOME_ADVANTAGE_ELO, K_FACTORS

# Stockage des ratings ELO en mémoire
elo_ratings = {}


def get_elo(team: str) -> float:
    """Retourne l'ELO d'une équipe, DEFAULT_ELO si inconnue."""
    return elo_ratings.get(team, DEFAULT_ELO)


def expected_score(elo_a: float, elo_b: float) -> float:
    """Probabilité de victoire de A contre B."""
    return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))


def update_elo(home: str, away: str, result: str, match_type: str, neutral: bool = False):
    """
    Met à jour l'ELO après un match.
    result = 'home' | 'away' | 'draw'
    match_type = clé dans K_FACTORS
    """
    k = K_FACTORS.get(match_type, 25)

    elo_home = get_elo(home)
    elo_away = get_elo(away)

    # Bonus domicile
    advantage = 0 if neutral else HOME_ADVANTAGE_ELO
    exp_home = expected_score(elo_home + advantage, elo_away)
    exp_away = 1 - exp_home

    # Score réel
    if result == "home":
        score_home, score_away = 1, 0
    elif result == "away":
        score_home, score_away = 0, 1
    else:
        score_home, score_away = 0.5, 0.5

    # Mise à jour
    elo_ratings[home] = elo_home + k * (score_home - exp_home)
    elo_ratings[away] = elo_away + k * (score_away - exp_away)


def get_win_probabilities(home: str, away: str, neutral: bool = False) -> dict:
    """
    Retourne les probabilités home/draw/away basées sur l'ELO.
    """
    elo_home = get_elo(home)
    elo_away = get_elo(away)

    advantage = 0 if neutral else HOME_ADVANTAGE_ELO
    prob_home = expected_score(elo_home + advantage, elo_away)
    prob_away = expected_score(elo_away, elo_home + advantage)

    # Probabilité draw = ce qui reste
    prob_draw = 1 - prob_home - prob_away

    return {
        "home": round(prob_home, 4),
        "draw": round(max(prob_draw, 0), 4),
        "away": round(prob_away, 4),
    }
