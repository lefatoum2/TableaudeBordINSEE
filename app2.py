import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from version5_dashboard.data import *

# Chargement du document CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Instance de l'application
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Figure bar
fig = px.bar(df, x="Age", y="Nombre de morts", color="Genre", barmode="group", title="Mortalité selon le genre")
fig2 = px.pie(df2, values='Total', names='Age', title="Mortalité en 2020 selon l'âge")

app.layout = html.Div(className='main', children=[
    html.Div(className='gfg0', children=[
        html.H1(children='Etude de la mortalité en France en 2020'),

        html.Div(children='''
        C'est une étude de la mortalité en France selon l'âge et le sexe. Source INSEE.
    ''')]),
    # Figure Bar
    html.Div(className='gfg1', children=[
        dcc.Graph(
            id='example-graph',
            figure=fig
        )]),
    # Figure Pie
    html.Div(className='gfg2', children=[
        dcc.Graph(
            id='example-graph2',
            figure=fig2
        )]),

    # Courbe linéaire de la mortalité des femmes selon l'âge
    html.Div(className='gfg3', children=[
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data1["Date_evenement"],
                        "y": f_m_24,
                        "type": "lines",
                        "name": "Femme de 0 à 24",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": f_25_49,
                        "type": "lines",
                        "name": "Femme de 25 à 49",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": f_50_64,
                        "type": "lines",
                        "name": "Femme de 0 à 24",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": f_65_74,
                        "type": "lines",
                        "name": "Femme de 0 à 24",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": f_75_84,
                        "type": "lines",
                        "name": "Femme de 0 à 24",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": f_75_84,
                        "type": "lines",
                        "name": "Femme de 75 à 84",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": f_85,
                        "type": "lines",
                        "name": "Femme de 0 à 24",
                    },

                    ],
                "layout": {"title": "Mortalité des femmes selon l'âge jour par jour"},
            },
        )]
             ),
    html.P("La mortalité des femmes est proportionnelle au temps. On pourra comparer cela à celle des hommes."),
    # Courbe linéaire de la mortalité des hommes selon l'âge
    html.Div(className='gfg4', children=[
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data1["Date_evenement"],
                        "y": h_m_24,
                        "name": "Hommes de 0 à 24",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": h_25_49,
                        "name": "Hommes de 25 à 49",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": h_50_64,
                        "name": "Hommes de 50 à 64",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": h_65_74,
                        "name": "Hommes de 65 à 74",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": h_75_84,
                        "name": "Hommes de 75 à 84",
                    },
                    {
                        "x": data1["Date_evenement"],
                        "y": h_85,
                        "name": "Hommes de 85 à plus",
                    }
                ],
                "layout": {"title": "Mortalité des hommes selon l'âge jour par jour"},
            },
        )]),
    html.P("On peut voir comment la mortalité des hommes est proportionnelle au temps, peu importe l'âge. Ces courbes semblent pratiquement similaires à celle des femmes.")
])

# Lancement de l'application
if __name__ == '__main__':
    app.run_server(debug=True)
