import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import threading
import time
from sniffing.packet_sniffer import packet_data, run_sniffer_in_thread

# Start sniffer in background
run_sniffer_in_thread()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Live Network Traffic"),
    dcc.Interval(id="interval-update", interval=2000, n_intervals=0),  # Refresh every 2 seconds
    dcc.Graph(id="live-graph")
])

@app.callback(
    Output("live-graph", "figure"),
    [Input("interval-update", "n_intervals")]
)
def update_graph(n):
    if not packet_data:
        return px.scatter(title="No Data Captured Yet")

    df = pd.DataFrame(packet_data)
    fig = px.scatter(df, x="Source", y="Destination", color="Protocol",
                     title="Live Network Traffic", hover_data=["Source", "Destination", "Protocol"])
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
