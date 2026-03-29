from dash import Input, Output
import plotly.express as px

from data_processing import apply_filters


def register_callbacks(app, df):

    # ================= CATEGORY =================
    @app.callback(
        Output("category_dist", "figure"),
        Input("category_filter", "value"),
        Input("risk_filter", "value"),
        Input("model_filter", "value"),
    )
    def update_category(category, risk, model):
        dff = apply_filters(df, category, risk, model)
        return px.pie(dff, names="Category", title="Asset Category Distribution")

    # ================= VENDOR =================
    @app.callback(
        Output("vendor_dist", "figure"),
        Input("category_filter", "value"),
        Input("risk_filter", "value"),
        Input("model_filter", "value"),
    )
    def update_vendor(category, risk, model):
        dff = apply_filters(df, category, risk, model)

        top_vendors = dff["vendor_normalized"].value_counts().nlargest(10).reset_index()
        top_vendors.columns = ["Vendor", "Count"]

        return px.bar(top_vendors, x="Vendor", y="Count", title="Top 10 Vendors")

    # ================= OS =================
    @app.callback(
        Output("os_dist", "figure"),
        Input("category_filter", "value"),
        Input("risk_filter", "value"),
        Input("model_filter", "value"),
    )
    def update_os(category, risk, model):
        dff = apply_filters(df, category, risk, model)

        top_os = dff["OS_normalized"].value_counts().nlargest(10).reset_index()
        top_os.columns = ["OS", "Count"]

        return px.bar(top_os, x="OS", y="Count", title="Top OS Distribution")

    # ================= RISK =================
    @app.callback(
        Output("risk_dist", "figure"),
        Input("category_filter", "value"),
        Input("risk_filter", "value"),
        Input("model_filter", "value"),
    )
    def update_risk(category, risk, model):
        dff = apply_filters(df, category, risk, model)
        return px.histogram(dff, x="risk_level", title="Risk Level Distribution")

    # ================= FP =================
    @app.callback(
        Output("fp_integrity_dist", "figure"),
        Input("category_filter", "value"),
        Input("risk_filter", "value"),
        Input("model_filter", "value"),
    )
    def update_fp(category, risk, model):
        dff = apply_filters(df, category, risk, model)

        return px.histogram(
            dff,
            x="FP_Integrity_Score",
            nbins=5,
            title="Fingerprint Integrity Score Distribution",
        )

    # ================= QUALITY =================
    @app.callback(
        Output("quality_score_dist", "figure"),
        Input("category_filter", "value"),
        Input("risk_filter", "value"),
        Input("model_filter", "value"),
    )
    def update_quality(category, risk, model):
        dff = apply_filters(df, category, risk, model)

        return px.histogram(
            dff,
            x="Data_Quality_Score",
            nbins=10,
            title="Data Quality Score Distribution",
        )

    # ================= ERROR CHART =================
    @app.callback(
        Output("error_counts", "figure"),
        Input("category_filter", "value"),
        Input("risk_filter", "value"),
        Input("model_filter", "value"),
    )
    def update_errors(category, risk, model):
        dff = apply_filters(df, category, risk, model)

        error_cols = [c for c in dff.columns if c.startswith("Err_")]

        error_summary = dff[error_cols].sum().sort_values(ascending=False).reset_index()
        error_summary.columns = ["Error Type", "Count"]

        return px.bar(
            error_summary, x="Error Type", y="Count", title="Error Distribution"
        )

    # ================= TABLE =================
    @app.callback(
        Output("error_table", "children"),
        Input("category_filter", "value"),
        Input("risk_filter", "value"),
        Input("model_filter", "value"),
    )
    def update_table(category, risk, model):
        dff = apply_filters(df, category, risk, model)
        top = dff.sort_values("Total_Error_Count", ascending=False).head(10)

        return html.Table(
            [
                html.Thead(
                    html.Tr(
                        [html.Th("Asset ID"), html.Th("MAC Address"), html.Th("Errors")]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Td(top.iloc[i]["Asset ID"]),
                                html.Td(top.iloc[i]["MAC Address"]),
                                html.Td(top.iloc[i]["Total_Error_Count"]),
                            ]
                        )
                        for i in range(len(top))
                    ]
                ),
            ]
        )
