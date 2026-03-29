import pandas as pd


def prepare_data() -> pd.DataFrame:
    """
    Cleans and prepares dataset for dashboard usage.
    """

    df = pd.read_csv("Dashboard Data/dashboard_data.csv")

    # Ensure error columns are boolean
    error_columns = [c for c in df.columns if c.startswith("Err_")]
    df[error_columns] = df[error_columns].fillna(False).astype(bool)

    return df


def apply_filters(df, category, risk, model):
    """
    Applies dashboard filters.
    """

    dff = df.copy()

    if category:
        dff = dff[dff["Category"].isin(category)]

    if risk:
        dff = dff[dff["risk_level"].isin(risk)]

    if model:
        dff = dff[dff["Model_Type"].isin(model)]

    return dff
