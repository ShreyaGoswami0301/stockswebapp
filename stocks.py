import streamlit as st
import pandas as pd
from PIL import Image


st.write(""" This is a Stock Market Web Application. 
**VISUALLY SHOWS STOCK DATA**
""")

image = Image.open('C:/Users/shrey.DESKTOP-O934829/PycharmProjects/stocks/stoc.jpg')
st.image(image, use_column_width=True)

st.sidebar.header('User Input:')

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-01-02")
    end_date = st.sidebar.text_input("End Date", "2020-08-04")
    stock_symbol = st.sidebar.text_input("Stock Symbol: \n AMZN \n TSLA \n AAPL \n GOOG \n MSFT \n NFLX", "AMZN")
    return start_date, end_date, stock_symbol


def get_company_name(symbol):
    if symbol == 'AMZN' :
        return 'Amazon'
    elif symbol == 'TSLA':
        return 'Tesla,Inc'
    elif symbol == 'AAPL' :
        return 'Apple,Inc'
    elif symbol == 'MSFT' :
        return 'Microsoft'
    elif symbol == 'GOOG' :
        return 'Alphabet'
    elif symbol == 'NFLX' :
        return 'Netflix'
    else :
        return 'None'


def get_data(symbol, start, end) :

    if symbol.upper() == 'AMZN' :
        df = pd.read_csv("C:/Users/shrey.DESKTOP-O934829/PycharmProjects/stocks/AMZN.csv")
    elif symbol.upper() == 'TSLA' :
        df = pd.read_csv("C:/Users/shrey.DESKTOP-O934829/PycharmProjects/stocks/TSLA.csv")
    elif symbol.upper() == 'AAPL' :
        df = pd.read_csv("C:/Users/shrey.DESKTOP-O934829/PycharmProjects/stocks/AAPL.csv")
    elif symbol.upper() == 'MSFT' :
        df = pd.read_csv("C:/Users/shrey.DESKTOP-O934829/PycharmProjects/stocks/MSFT.csv")
    elif symbol.upper() == 'GOOG' :
        df = pd.read_csv("C:/Users/shrey.DESKTOP-O934829/PycharmProjects/stocks/GOOG.csv")
    elif symbol.upper() == 'NFLX' :
        df = pd.read_csv("C:/Users/shrey.DESKTOP-O934829/PycharmProjects/stocks/NFLX.csv")
    else:
        df = pd.DataFrame(columns=['Date', 'Open', 'High' 'Low', 'Close', 'Adj Close', 'Volume'])


    start = pd.to_datetime(start)
    end = pd.to_datetime(end)


    start_row =0
    end_row =0

    #check for date from top of the list to match the input
    for i in range(0, len(df)) :
        if start <= pd.to_datetime(df['Date'][i]) :
            start_row = i
            break

    #start from bottom of dataset to up
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]) :
            end_row = len(df)-1-j
            break


    df =df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row+1, :]

start, end, symbol = get_input()
df = get_data(symbol, start, end)
company_name = get_company_name(symbol.upper())

st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

st.header('Data Statistics')
st.write(df.describe())


