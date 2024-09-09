from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporer les données
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialiser l'application
app = Dash(__name__)

# Mise en page de l'application
app.layout = html.Div([
    html.H1("Tableau de bord avec Dash"),
    html.Div(children='Ma première application avec des données, un graphique et des contrôles'),
    html.Hr(),
    dcc.RadioItems(
        options=['pop', 'lifeExp', 'gdpPercap'], 
        value='lifeExp', 
        id='controls-and-radio-item'
    ),
    dash_table.DataTable(
        data=df.to_dict('records'), 
        page_size=6
    ),
    dcc.Graph(id='controls-and-graph'),
    dcc.Slider(
        id='slider',
        min=1,
        max=5,
        value=2,  # valeur initiale
        marks={str(num): str(num) for num in range(1, 6)},
        step=None
    ),
    dcc.Graph(id='line-graph')
])

# Callback pour mettre à jour le premier graphique en fonction du bouton radio
@callback(
    Output('controls-and-graph', 'figure'),
    Input('controls-and-radio-item', 'value')
)
def update_histogram(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Callback pour mettre à jour le graphique en ligne en fonction de la valeur du slider
@callback(
    Output('line-graph', 'figure'),
    Input('slider', 'value')
)
def update_line_graph(slider_value):
    # Exemple de données pour le graphique en ligne
    data = {'x': [1, 2, 3, 4, 5], 'y': [10, 11, 12, 13, 14]}
    df_line = pd.DataFrame(data)
    filtered_df = df_line[df_line['x'] <= slider_value]
    fig = px.line(filtered_df, x='x', y='y', title='Graphique Simple')
    return fig

# Exécuter l'application
if __name__ == '__main__':
    app.run(debug=True)
