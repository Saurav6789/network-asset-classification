from jupyter_dash import JupyterDash
from dash import dcc, html

from data_processing import prepare_data
from metrics import compute_kpis
from callbacks import register_callbacks

# -------------------------
# LOAD DATA
# -------------------------
# final_df must already exist OR load it here
df = prepare_data()

# -------------------------
# INIT APP
# -------------------------
app = JupyterDash(__name__)

# -------------------------
# KPI DATA
# -------------------------
kpis = compute_kpis(df)

# -------------------------
# STYLE
# -------------------------
card_style = {
    "backgroundColor": "#ffffff",
    "padding": "15px",
    "borderRadius": "12px",
    "boxShadow": "0px 4px 12px rgba(0,0,0,0.08)",
    "textAlign": "center",
    "width": "23%",
    "borderLeft": "5px solid #3498db",
}

# -------------------------
# LAYOUT
# -------------------------
app.layout = html.Div(
    [
        html.H1(
            "Asset Classification & Data Quality Dashboard",
            style={"textAlign": "center"},
        ),
        # KPI SECTION
        html.Div(
            [
                html.Div(
                    [html.H3(kpis["total_assets"]), html.P("Total Assets")],
                    style=card_style,
                ),
                html.Div(
                    [
                        html.H3(kpis["missing_fingerprints"]),
                        html.P("Missing Fingerprints"),
                    ],
                    style=card_style,
                ),
                html.Div(
                    [html.H3(kpis["duplicate_mac"]), html.P("Duplicate MACs")],
                    style=card_style,
                ),
                html.Div(
                    [html.H3(kpis["avg_quality_score"]), html.P("Avg Quality Score")],
                    style=card_style,
                ),
            ],
            style={"display": "flex", "justifyContent": "space-between"},
        ),
        html.Hr(),
        # FILTERS
        html.Div(
            [
                dcc.Dropdown(
                    options=[
                        {"label": c, "value": c}
                        for c in df["Category"].dropna().unique()
                    ],
                    id="category_filter",
                    multi=True,
                    placeholder="Category",
                ),
                dcc.Dropdown(
                    options=[
                        {"label": r, "value": r}
                        for r in df["risk_level"].dropna().unique()
                    ],
                    id="risk_filter",
                    multi=True,
                    placeholder="Risk Level",
                ),
                dcc.Dropdown(
                    options=[
                        {"label": m, "value": m}
                        for m in df["Model_Type"].dropna().unique()
                    ],
                    id="model_filter",
                    multi=True,
                    placeholder="Model Type",
                ),
            ],
            style={"width": "80%", "margin": "auto"},
        ),
        html.Hr(),
        # GRAPHS
        html.Div(
            [
                dcc.Graph(id="category_dist"),
                dcc.Graph(id="vendor_dist"),
                dcc.Graph(id="os_dist"),
            ]
        ),
        html.Div(
            [
                dcc.Graph(id="risk_dist"),
                dcc.Graph(id="fp_integrity_dist"),
                dcc.Graph(id="quality_score_dist"),
            ]
        ),
        html.Div([dcc.Graph(id="error_counts"), html.Div(id="error_table")]),
    ],
    style={"padding": "20px", "backgroundColor": "#f5f7fa"},
)

# -------------------------
# REGISTER CALLBACKS
# -------------------------
register_callbacks(app, df)

# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    app.run(debug=True, port=8051)
