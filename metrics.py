def compute_kpis(df):
    """
    KPI calculations for dashboard cards.
    """

    kpis = {
        "total_assets": len(df),
        "missing_fingerprints": df["Err_All_Fingerprints_Missing"].sum(),
        "duplicate_mac": df["Err_Duplicate_MAC"].sum(),
        "avg_quality_score": round(df["Data_Quality_Score"].mean(), 1),
    }

    return kpis
