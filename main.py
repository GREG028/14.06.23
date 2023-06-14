import yfinance as yf
import numpy as np
import requests
import multitasking
from datetime import date
from pandas_datareader import data as web
import pandas as pd


aapl= yf.Ticker("aapl")

today = date.today()

start = input("Wpisz date start: (format Y-m-d)")
end = input("Wpisz date end: (format Y-m-d)")

# interval = input("Wpisz interwal: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]")
start = "2023-06-01"
end="2023-06-14"
interval = "1d"
aapl_historical = aapl.history(start=start, end=end, interval=interval)

print(aapl_historical)

ap = aapl_historical

ap.to_csv('./data/AAPL.csv')

# df = pd.read_csv("./data/AAPL.csv")

# jo=pd.read_csv("./data/AAPL.csv",usecols=["Close"])


# li = list(df['Close'])



# print(li)
# srednia = np.zeros(len(li)) + 1
# p = 0
# i = 0
# t = 0
# print("Wpisz okres sredniej, ktora ma obliczac program")
# l = int(input())
# m = np.zeros(l)
# s = 0
# print(f"Witaj w programie obliczajacym srednie z {l}")
# while i < l:
#     s += li[i]
#     p += 1 
#     i += 1

# print("Recurrent")
# srednia[i] = s/l
# print(srednia[i])
# while i < len(li) - 1:
#     print("Srednia jest rowna")
#     print(s/l)
#     p = (p+1)%l 
#     i += 1
#     s -= li[p]
#     s += li[i]
#     print(p, i)
#     srednia[i] = s/l

# while t < len(li) - 1:

#     print(srednia[i])
#     t += 1

