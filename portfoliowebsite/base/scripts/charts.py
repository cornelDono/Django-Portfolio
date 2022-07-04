import pandas as pd
import plotly.express as px

def create_chart(list, time):
    data = [
            {
                f'{time}' : x.get(f'{time}'),
                'Count' : x.get('c')
            } for x in list
        ]

    df = pd.DataFrame(data)
    fig = px.bar(df, x=f'{time}', y='Count',
                 text_auto='.2s', title=f'Amount of articles per {time}')
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    plot = fig.to_html()
    return plot