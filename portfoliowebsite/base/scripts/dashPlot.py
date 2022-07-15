from dash import html, dcc, Input, Output, Dash
import pandas as pd
import plotly.express as px
from pytrends.request import TrendReq

def create_dash():
    pytrend = TrendReq()
    kw_list = ["Power BI", "Tableau", "Qlik", "Looker", "Microstrategy"] # list of keywords to get data 
    pytrend.build_payload(kw_list, cat=0, timeframe='today 5-y') 
    data = pytrend.interest_over_time() 
    data = data.reset_index() 

    data = data.melt(id_vars=['date','isPartial'])

    app = Dash()

    app.layout = html.Div(children=[
    html.H1(children='BI dash+'),
    dcc.Checklist(id='geo-dropdown',
                options=[{'label':i, 'value':i}
                        for i in data['variable'].unique()],
                inline=True),
    dcc.Graph(id='price-graph')
    ])

    @app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id='geo-dropdown', component_property='value')
    )

    def update_graph(selected_geography):
        print(selected_geography)
        # filterd_avocado = data[data['variable'] in selected_geography]
        filterd_avocado = data[data['variable'].isin(selected_geography)]
        line_fig = px.line(filterd_avocado,
                        x='date', y='value',
                        color='variable',
                        title=f'BI in {selected_geography}'
        )
        return line_fig
    return app


if __name__=='__main__':
    create_dash().run_server(debug=True)