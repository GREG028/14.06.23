import yfinance as yf
import numpy as np
import requests
from datetime import date
from pandas_datareader import data as web
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt



def sciaganiedanych():
    aapl= yf.Ticker("aapl")

    today = date.today()

    start = input("Wpisz date poczatkowa: (format Y-m-d) : ") # dataframe start

    interval = input("Wybierz interwal: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]") # inpput interval
    end=today.strftime('%Y-%m-%d')

    aapl_historical = aapl.history(start=start, end=end, interval=interval)

    ap = aapl_historical

    ap.to_csv('./data/AAPL.csv') # Konwersja dataframe do csv

    df = pd.read_csv("./data/AAPL.csv")

    # li = list(df['Close']) # Wydzielenie kolumny do listy

sciaganiedanych()














# ARCHIWUM Ponizej 

# def tworzeniewykresu():

#     aapl =  pd.read_csv("./data/AAPL.csv")

#     mpl.use('MacOSX')
#     aapl['Close'].plot(figsize=(8,8), label='Apple')
#     plt.show()




    # srednia = np.zeros(len(li)) + 1
    # p = 0
    # i = 0
    # t = 0
    # e = 0
    # print("Wpisz okres sredniej, ktora ma obliczac program")
    # l = int(input())
    # m = np.zeros(l)
    # s = 0
    # array = np.zeros(l)

    # while i < len(li) - len(array):



    # while e < l:
    #     array[e] = li[e]
    #     e += 1

    # i = l
    # while i < len(li) - l:
    #     p = (p+1)%l
    #     array[p] -= li[abs(i - l)]
    #     array[p] += li[i]
    #     i += 1

    # print(array)


# PONIZEJ STARY KOD
# while p < l:
#     s += li[p]
#     p += 1 

# p -= 1 # ważny element









# srednia[i] = s/l
# print(f"Witaj w programie obliczajacym srednie z {l}")
# while i < len(li) - 1:
#     p = (p+1)%l
#     print(i)
#     print(p)
#     print(srednia[i]) 
#     i += 1
#     s -= li[p]
#     s += li[i]
#     srednia[i] = s/l
    
# print("Recurrent")

# while t < len(li) - 1:
#     print(t)
#     print(srednia[t])
    
#     t += 1

