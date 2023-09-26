import DataAccessPoint as Dap
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import JsonLocalAccess as Jla

app = Dash(__name__)

dropdown1 = dcc.Dropdown(["Enterprise Attacks", "Mobile Attacks", "Ics Attacks"], "Ics Attacks", clearable=False)
dropdown2 = dcc.Dropdown(["Techniques per Mitigation", "Mitigations per Technique", "Techniques per Data source",
                         "Data sources per Technique"], "Techniques per Mitigation", clearable=False)
graph = dcc.Graph()

app.layout = html.Div([
    html.H1(children='Mitre Data Visualization', style={'textAlign':'center'}),
    dcc.Loading(
        id="loading-1",
        type="default",
        children=html.Div(id="loading-output-1")
    ),
    html.Div([html.H4("Effectiveness by the numbers"), dropdown1, dropdown2, graph])])


def update_enterprise():
    source = Dap.DataAccessPoint("enterprise_attack")
    key_vals = source.get_key_values(source.mitigate_to_technique(), 50)
    Jla.access_mit_tech_e(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_mitigate(), 50)
    Jla.access_tech_mit_e(True, data=key_vals)
    key_vals = source.get_key_values(source.datasource_to_technique(), 50)
    Jla.access_comp_tech_e(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_datasource(), 50)
    Jla.access_tech_comp_e(True, data=key_vals)


def update_mobile():
    source = Dap.DataAccessPoint("mobile_attack")
    key_vals = source.get_key_values(source.mitigate_to_technique(), 50)
    Jla.access_mit_tech_m(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_mitigate(), 50)
    Jla.access_tech_mit_m(True, data=key_vals)
    key_vals = source.get_key_values(source.datasource_to_technique(), 50)
    Jla.access_comp_tech_m(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_datasource(), 50)
    Jla.access_tech_comp_m(True, data=key_vals)


def update_ics():
    source = Dap.DataAccessPoint("ics_attack")
    key_vals = source.get_key_values(source.mitigate_to_technique(), 50)
    Jla.access_mit_tech_i(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_mitigate(), 50)
    Jla.access_tech_mit_i(True, data=key_vals)
    key_vals = source.get_key_values(source.datasource_to_technique(), 50)
    Jla.access_comp_tech_i(True, data=key_vals)
    key_vals = source.get_key_values(source.technique_to_datasource(), 50)
    Jla.access_tech_comp_i(True, data=key_vals)


def get_ics(graph_num):
    match graph_num:
        case "Techniques per Mitigation":
            return Jla.access_mit_tech_i(False)
        case "Mitigations per Technique":
            return Jla.access_tech_mit_i(False)
        case "Techniques per Data source":
            return Jla.access_comp_tech_i(False)
        case "Data sources per Technique":
            return Jla.access_tech_comp_i(False)


def get_enterprise(graph_num):
    match graph_num:
        case "Techniques per Mitigation":
            return Jla.access_mit_tech_e(False)
        case "Mitigations per Technique":
            return Jla.access_tech_mit_e(False)
        case "Techniques per Data source":
            return Jla.access_comp_tech_e(False)
        case "Data sources per Technique":
            return Jla.access_tech_comp_e(False)


def get_mobile(graph_num):
    match graph_num:
        case "Techniques per Mitigation":
            return Jla.access_mit_tech_m(False)
        case "Mitigations per Technique":
            return Jla.access_tech_mit_m(False)
        case "Techniques per Data source":
            return Jla.access_comp_tech_m(False)
        case "Data sources per Technique":
            return Jla.access_tech_comp_m(False)


@callback(Output(graph, "figure"), Input(dropdown1, 'value'), Input(dropdown2, 'value'))
def update_bar_chart(attack_type, relation_type):
    fig = None
    graph_data = None
    match attack_type:
        case "Ics Attacks":
            graph_data = get_ics(relation_type)
        case "Mobile Attacks":
            graph_data = get_mobile(relation_type)
        case "Enterprise Attacks":
            graph_data = get_enterprise(relation_type)
    fig = px.bar(x=graph_data.keys(), y=graph_data.values())
    return fig


if __name__ == '__main__':
    app.run(debug=True)
