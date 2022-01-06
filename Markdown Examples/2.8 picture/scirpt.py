import dash
from dash import html
import marvmiloTools as mmt

app = dash.Dash(__name__)
app.layout = html.Div(
    mmt.dash.content_div(
        width = "1500px",
        padding = "2%",
        children = [
            html.Div(
                mmt.dash.picture(
                    path = "pictures/smiley.jpg",
                    width = "20rem",
                    aspect_ratio = "2 / 1",
                    children = ["Hello world!"],
                    additional_style = {"borderRadius": "2rem"}
                )
            )
        ]
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)