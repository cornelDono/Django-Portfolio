from operator import ge
import pandas as pd
import plotly.express as px
from pytrends.request import TrendReq

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


def google_trends_data():
    pytrend = TrendReq()
    kw_list = ["power bi", "tableau", "qlik"] # list of keywords to get data 
    pytrend.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='RU') 
    data = pytrend.interest_over_time() 
    data = data.reset_index() 
    return data

def google_trends():
    pytrend = TrendReq()
    kw_list = ["power bi", "tableau", "qlik"] # list of keywords to get data 
    pytrend.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='RU') 
    data = pytrend.interest_over_time() 
    data = data.reset_index() 
    fig = px.line(data, x="date", y=["power bi", "tableau", "qlik"], title='Keyword Web Search Interest Over Time')
    plot = fig.to_html()
    return plot

def google_trends_create_plot(data):
    fig = px.line(data, x="date", y=["power bi", "tableau", "qlik"], title='Keyword Web Search Interest Over Time')
    plot = fig.to_html()
    return plot
    
if __name__=='__main__':
    data = google_trends_data()
    for index, row in data.iterrows():
        print(row['date'], row['power bi'] )