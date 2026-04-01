# ============================================================
# RAPPORT DE BACKTEST
# ============================================================
# Affiche les résultats du backtest de manière lisible
# Permet de juger rapidement si le modèle est rentable

def display_report(backtest_results):
    """
    Affiche un rapport complet du backtest
    backtest_results : dict retourné par run_backtest()
    """

    print("\n" + "=" * 55)
    print("         📊 RAPPORT DE BACKTEST")
    print("=" * 55)

    # --------------------------------------------------------
    # RÉSUMÉ GLOBAL
    # --------------------------------------------------------
    print(f"\n  📌 Paris joués     : {backtest_results['total_bets']}")
    print(f"  ✅ Paris gagnés    : {backtest_results['total_wins']}")
    print(f"  🎯 Taux de réussite: {backtest_results['win_rate']}")
    print(f"  💰 Total misé      : {backtest_results['total_staked']}")
    print(f"  📈 Profit net      : {backtest_results['total_profit']}")
    print(f"  🔄 ROI             : {backtest_results['roi']}")

    # --------------------------------------------------------
    # INTERPRÉTATION DU ROI
    # --------------------------------------------------------
    roi_value = float(backtest_results['roi'].replace('%', ''))

    print("\n  📋 Interprétation :")
    if roi_value >= 10:
        print("  🔥 Excellent — Modèle très rentable")
    elif roi_value >= 5:
        print("  ✅ Bon — Modèle rentable")
    elif roi_value >= 0:
        print("  ⚠️  Neutre — Modèle à surveiller")
    else:
        print("  ❌ Négatif — Modèle non rentable")

    # --------------------------------------------------------
    # DÉTAIL DES PARIS
    # --------------------------------------------------------
    print("\n" + "-" * 55)
    print("  DÉTAIL DES PARIS")
    print("-" * 55)

    for bet in backtest_results['bet_log']:
        icon = "✅" if bet['win'] else "❌"
        print(f"\n  {icon} {bet['match']}")
        print(f"     Issue pariée : {bet['predicted']}")
        print(f"     Résultat réel: {bet['actual']}")
        print(f"     Cote         : {bet['odd']}")
        print(f"     Value        : +{bet['value']}%")
        print(f"     Profit/Perte : {bet['profit']}€")

    print("\n" + "=" * 55 + "\n")


# ============================================================
# RAPPORT SYNTHÉTIQUE (version courte)
# ============================================================
