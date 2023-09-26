import DataAccessPoint as Dap
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import JsonLocalAccess as Jla
import pandas as pd

app = Dash(__name__, external_stylesheets=["assets/styles.css"])


dropdown1 = dcc.Dropdown(["Enterprise Attacks", "Mobile Attacks", "Ics Attacks"], "Ics Attacks", clearable=False)
dropdown2 = dcc.Dropdown(["Techniques per Mitigation", "Mitigations per Technique", "Techniques per Data source",
                         "Data sources per Technique"], "Techniques per Mitigation", clearable=False)
dropdown3 = dcc.Dropdown(["10", "20", "30", "40", "50"], "10", clearable=False)
graph = dcc.Graph()

app.layout = html.Div(
    style={'margin': '5w'},
    children=[
        html.H1(
            children='Mitre Data Visualization',
            style={
                'textAlign': 'center',
                'color': '#f7f7f7',
                'font-family': 'Arial, sans-serif',
                'font-size': '36px',
                'padding': '10px',
                'background-color': '#3f3f3f',
                'box-shadow': '0px 0px 10px rgba(0, 0, 0, 0.2)',
                'margin': '0'
            }
        ),
        dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output-1")
        ),
        html.Div([html.H4("Effectiveness by the numbers"), dropdown1, dropdown2, dropdown3, graph])])


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


def retrieve_data(graph_num, limit, attack):
    match graph_num:
        case "Techniques per Mitigation":
            return Jla.access_json("mit", "tech", attack, limit), "Number of Techniques"
        case "Mitigations per Technique":
            return Jla.access_json("tech", "mit", attack, limit), "Number of Mitigations"
        case "Techniques per Data source":
            return Jla.access_json("comp", "tech", attack, limit), "Number of Techniques"
        case "Data sources per Technique":
            return Jla.access_json("tech", "comp", attack, limit), "Number of Data Sources"


@callback(Output(graph, "figure"), Input(dropdown1, 'value'), Input(dropdown2, 'value'), Input(dropdown3, 'value'))
def update_bar_chart(attack_type, relation_type, limit):
    limit = int(limit)
    fig = None
    graph_data = None
    key_list = []
    value_list = []
    axis_title = ""
    match attack_type:
        case "Ics Attacks":
            graph_data, axis_title = retrieve_data(relation_type, limit, "i")
        case "Mobile Attacks":
            graph_data, axis_title = retrieve_data(relation_type, limit, "m")
        case "Enterprise Attacks":
            graph_data, axis_title = retrieve_data(relation_type, limit, "e")
    for item in graph_data:
        key_list.append(item[0])
        value_list.append(item[1])

    fig = px.bar(x=key_list, y=value_list)
    fig.update_layout(yaxis_title=axis_title, xaxis_title=None)
    return fig


if __name__ == '__main__':
    app.run(debug=True)
