# ============================================================
# SUPPRESSION DE LA MARGE PINNACLE
# ============================================================
# Pinnacle intègre une marge dans ses cotes (environ 2-3%)
# On doit la retirer pour comparer avec nos fair odds
#
# Exemple :
# Cotes brutes Pinnacle : 1.85 / 3.40 / 4.20
# Total implicite       : 54.1% + 29.4% + 23.8% = 107.3%  ← marge = 7.3%
# Après suppression     : on ramène tout à 100%

def remove_margin(odd_home, odd_draw, odd_away):
    """
    Supprime la marge bookmaker des cotes Pinnacle
    Retourne les probabilités réelles (sans marge)
    """
    # Étape 1 : Convertir les cotes en probabilités implicites
    p_home = 1 / odd_home
    p_draw = 1 / odd_draw
    p_away = 1 / odd_away

    # Étape 2 : Calculer la marge totale
    total = p_home + p_draw + p_away  # Ex: 1.073

    # Étape 3 : Normaliser → ramener à 100%
    p_home_clean = p_home / total
    p_draw_clean = p_draw / total
    p_away_clean = p_away / total

    return {
        "margin": round((total - 1) * 100, 2),       # Ex: 7.3%
        "p_home": round(p_home_clean * 100, 2),
        "p_draw": round(p_draw_clean * 100, 2),
        "p_away": round(p_away_clean * 100, 2),
    }
