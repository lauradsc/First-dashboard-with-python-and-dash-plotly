from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
# a list to show with the ID especified
options = list(df['ID Loja'].unique())
options.append("Todos")

app.layout = html.Div(children=[
    html.H1(children='Produtos'),

    html.Div(children='''
        Faturamento de produtos
    '''),

    # dropdown with dash components
    dcc.Dropdown(options, value='all stores', id='dropdown'),

    dcc.Graph(
        id='graph',
        figure=fig
    )
])


@app.callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value')
)

def update_output(value):
    if value == "all stores":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df["ID Loja"]==value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
