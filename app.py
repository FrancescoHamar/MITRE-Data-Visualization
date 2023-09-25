import DataAccessPoint as Dap
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import json

app = Dash(__name__)

dropdown = dcc.Dropdown(["1", "2", "3", "4"], "1", clearable=False)
graph = dcc.Graph()

app.layout = html.Div([
    html.H1(children='Mitre Data Visualization', style={'textAlign':'center'}),
    dcc.Loading(
        id="loading-1",
        type="default",
        children=html.Div(id="loading-output-1")
    ),
    html.Div([html.H4("Effectivness by the numbers"), dropdown, graph])])


@callback(Output(graph, "figure"), Input(dropdown, "value"))
def update_bar_chart(day):
    fig = None
    if day == "1":
        fig = px.bar(x=indict.keys(), y=indict.values())
    # elif day == "2":
    #     fig = px.bar(x=keys2, y=value2)
    # elif day == "3":
    #     fig = px.bar(x=keys3, y=value3)
    # elif day == "4":
    #     fig = px.bar(x=keys4, y=value4)
    return fig


source = Dap.DataAccessPoint("ics_attack")
source.display_single(source.technique_to_mitigate(), 10)
with open("data/mit_tech_m.json", 'r') as indata:
    indict = json.load(indata)

if __name__ == "__main__":
    app.run_server(debug=True)

