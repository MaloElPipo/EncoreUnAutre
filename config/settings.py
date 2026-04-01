# ============================================================
# PARAMÈTRES GÉNÉRAUX - Tu peux modifier ces valeurs librement
# ============================================================

# --- API ---
API_KEY = "fapi_74nP4A2JJ8Ts7DD3YeZQlkG8bcJPoMlQ"
BASE_URL = "https://api.thestatsapi.com/v1"

# --- Compétitions suivies ---
COMPETITIONS = {
    "world_cup": True,
    "qualifications": True,
    "friendly": False,      # Mis à False = ignorés par défaut
}

# --- ELO : Pondération par type de match ---
K_FACTORS = {
    "friendly": 10,
    "qualification": 25,
    "world_cup_group": 40,
    "world_cup_ko": 50,
}

# --- ELO de départ pour toute nouvelle équipe ---
DEFAULT_ELO = 1500
HOME_ADVANTAGE_ELO = 100    # Bonus points ELO pour jouer à domicile

# --- Match Rating ---
LAST_N_MATCHES = 6          # Nombre de matchs pour calculer le rating (PDF = 6)

# --- Value Bet ---
VALUE_THRESHOLD = 0.05      # 5% minimum pour signaler une value
HIGH_VALUE_THRESHOLD = 0.08 # 8%+ = alerte renforcée

# --- Historique ---
HISTORY_YEARS = 6           # Années d'historique à charger

# --- Affichage ---
SHOW_ALL_MATCHES = False     # True = affiche tous les matchs, False = value bets seulement
