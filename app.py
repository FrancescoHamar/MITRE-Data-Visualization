import DataAccessPoint as Dap
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import JsonLocalAccess as Jla

app = Dash(__name__, external_stylesheets=["assets/styles.css"])


dropdown1 = dcc.Dropdown(["Enterprise Attacks", "Mobile Attacks", "Ics Attacks"], "Enterprise Attacks", id='drop1',
                         clearable=False)
dropdown2 = dcc.Dropdown(["Techniques per Mitigation", "Mitigations per Technique", "Techniques per Data source",
                         "Data sources per Technique"], "Techniques per Mitigation", id='drop2', clearable=False)
dropdown3 = dcc.Dropdown(["10", "20", "30", "40", "50"], "10", id='drop3', clearable=False)
graph = dcc.Graph(id='graph')

app.layout = html.Div(
    style={'margin': '5w'},
    children=[
        html.H1('Mitre Data Visualization'),
        html.Div(id='graphDiv', children=[html.H4("Effectiveness by the numbers"),
                  html.Div(id='dropdown', children=[dropdown1, dropdown2, dropdown3]), graph])])


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


@callback(Output(graph, "figure"), Input('drop1', 'value'), Input('drop2', 'value'), Input('drop3', 'value'))
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
