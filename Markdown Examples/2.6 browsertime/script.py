import dash
from dash import html
from dash.dependencies import Output, Input
import marvmiloTools as mmt

app = dash.Dash()
app.layout = html.Div(
    children = [
        html.Div(id = "dummy-out"),
        mmt.dash.browsertime.htmlObj()
    ]
)

app.clientside_callback(*mmt.dash.browsertime.clientside_callback_args)

@app.callback(
    [Output("dummy-out", "children")],
    [Input("browser-time", "data")]
)
def callback(browsertime):
    datetime_object = mmt.dash.browsertime.datetime(browsertime)
    time_shift = mmt.dash.browsertime.time_shift(browsertime)
    print(datetime_object)    
    print(time_shift)
    return [browsertime]

app.run_server(debug = True)