from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import JsonLocalAccess as Jla
import plotly.graph_objects as go
import pandas
import time

# Initializing app and server
app = Dash(__name__, external_stylesheets=["assets/styles.css"])
server = app.server
app.title = "MITRE ATT&CK Data"

# Dropdown menus used as input for graphs
g1_attack_drop = dcc.Dropdown(["Enterprise Attacks", "Mobile Attacks", "Ics Attacks"], "Enterprise Attacks", id='drop1',
                              clearable=False)
g1_option_drop = dcc.Dropdown(["Techniques per Mitigation", "Mitigations per Technique", "Techniques per Data source",
                         "Data sources per Technique"], "Techniques per Mitigation", id='drop2', clearable=False)
g1_limit_drop = dcc.Dropdown(["10", "20", "30", "40", "50"], "10", id='drop3', clearable=False)
g2_attack_drop = dcc.Dropdown(["Enterprise Attacks", "Mobile Attacks", "Ics Attacks"], "Enterprise Attacks", id='drop4',
                              clearable=False)

# Initializing graphs
relation_graph = dcc.Graph(id='graph')
chain_graph = dcc.Graph(id='graph2')

# Dash Html layout
app.layout = html.Div(
    children=[
        html.Div(id='banner', children=[html.Img(src='assets/mitre_attack_logo.png'),
                                        html.H1('Mitre Data Visualization')]),
        html.Div(id='graphDiv', children=[html.H4("Effectiveness by the numbers"),
                                          html.Div(id='dropdown', children=[g1_attack_drop, g1_option_drop,
                                                                            g1_limit_drop]),
                                          dcc.Loading(id="loading-icon1",
                                                      children=[html.Div(dcc.Graph(id='graph'))], type="default")]),
        html.Div(id='chainDiv', children=[html.H4("Mapping to the Kill Chain"),
                                          html.Div(id='dropdown2', children=[g2_attack_drop]),
                                          dcc.Loading(id="loading-icon2",
                                                      children=[html.Div(dcc.Graph(id='graph2'))], type="default")])
    ])


# Returns data from local Json files about the appropriate relationships
# Takes as input the relationship wanted, the display limit, and the attack type to query the correct file
def retrieve_relation_data(graph_num, limit, attack):
    match graph_num:
        case "Techniques per Mitigation":
            return Jla.access_relation_json("mit", "tech", attack, limit), "Number of Techniques"
        case "Mitigations per Technique":
            return Jla.access_relation_json("tech", "mit", attack, limit), "Number of Mitigations"
        case "Techniques per Data source":
            return Jla.access_relation_json("comp", "tech", attack, limit), "Number of Techniques"
        case "Data sources per Technique":
            return Jla.access_relation_json("tech", "comp", attack, limit), "Number of Data Sources"


# Returns data from local Json files about the kill chain phases
# Takes as input the type of attack to query correct file.
# Function is trivial and could be deleted, I was expecting heavier logic here until code refactoring.
def retrieve_chain_data(attack):
    return Jla.access_phases(attack)


# Callback function that updates the Relations graph.
# Takes as input the attack type, type of relation, and display limit and displays the data accordingly.
@callback(Output(relation_graph, "figure"), Input('drop1', 'value'), Input('drop2', 'value'), Input('drop3', 'value'))
def update_relation_bar_chart(attack_type, relation_type, limit):
    limit = int(limit)
    graph_data = None
    key_list = []
    value_list = []
    axis_title = ""
    match attack_type:
        case "Ics Attacks":
            graph_data, axis_title = retrieve_relation_data(relation_type, limit, "i")
        case "Mobile Attacks":
            graph_data, axis_title = retrieve_relation_data(relation_type, limit, "m")
        case "Enterprise Attacks":
            graph_data, axis_title = retrieve_relation_data(relation_type, limit, "e")
    for item in graph_data:
        key_list.append(item[0])
        value_list.append(item[1])

    fig = px.bar(x=key_list, y=value_list)
    fig.update_layout(yaxis_title=axis_title, xaxis_title=None)
    return fig


# Callback function that updates the kill chain graph.
# Takes as input the attack type dropdown and displays required the data accordingly.
@callback(Output(chain_graph, "figure"), Input('drop4', 'value'))
def update_chain_bar_chart(attack_type):
    graph_dict = {}
    tech_data = {}
    x_list = []
    tech_list = []
    mit_list = []
    source_list = []

    match attack_type:
        case "Ics Attacks":
            tech_data = retrieve_chain_data('i')
        case "Mobile Attacks":
            tech_data = retrieve_chain_data('m')
        case "Enterprise Attacks":
            tech_data = retrieve_chain_data('e')

    for item in tech_data[0]:
        graph_dict[item] = [len(tech_data[0][item]), 0, 0]

    for item in tech_data[1]:
        graph_dict[item][1] += len(tech_data[1][item])

    for item in tech_data[2]:
        graph_dict[item][2] += len(tech_data[2][item])

    for item in graph_dict:
        x_list.append(item)
        tech_list.append(graph_dict[item][0])
        mit_list.append(graph_dict[item][1])
        source_list.append(graph_dict[item][2])

    fig = go.Figure(data=[
        go.Bar(name='Techniques', x=x_list, y=tech_list),
        go.Bar(name='Mitigations', x=x_list, y=mit_list),
        go.Bar(name='Data Components', x=x_list, y=source_list)
    ])
    pandas.DataFrame()
    return fig


if __name__ == '__main__':
    app.run()
