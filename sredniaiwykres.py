import yfinance as yf
import numpy as np
import requests
from datetime import date
from pandas_datareader import data as web
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


df = pd.read_csv("./data/AAPL.csv")

li = list(df['Close'])



print("Wpisz czulosc srednii (bez jednostki)")
l=int(input(">> "))
m=[]
s=0
i=0
sredniakroczaca = []
sygnaly = []
czassygnal = []
while i<l:
    m.append(li[i]) # W wersji pierwotnej - m.append(float(input(">> ")))
    sredniakroczaca.append(li[i])
    s+=m[i]
    i+=1
m.reverse()
q=(s<m[0]*l)
# W wersji pierwotnej - print("Swietnie! Od tej pory po kazdym wpisaniu dostaniesz nowa serdnie i, ewentualnie, sygnal kupna lub sprzedazy.\nTwoja pierwsza serdnia to ", s/l)
i=l-1
t = i
u = 0

while t < len(li)-1:
    s-=m[i]
    m[i]=li[t]
    s+=m[i]
    sredniakroczaca.append(s/l)
    # W wersji pierwotnej - print("Twoja serdnia to ", s/l)
    if q:
        if s>m[i]*l:
            print("SPRZEDAJ")
            sygnaly.append(li[t])
            czassygnal.append(t)
            q=False
    else:
        if s<m[i]*l:
            print("KUP")
            sygnaly.append(li[t])
            czassygnal.append(t)
            q=True
    i=(i+l-1)%l
    t += 1

print(sygnaly)
print(czassygnal)
dict = {'wartosc': sredniakroczaca}


df = pd.DataFrame(dict)

df.to_csv('./data/srednia.csv')

srednia = pd.read_csv("./data/srednia.csv")
aapl =  pd.read_csv("./data/AAPL.csv")

mpl.use('MacOSX')

aapl['Close'].plot(figsize=(8,8), label='Cena AAPL')
srednia['wartosc'].plot(figsize=(8,8), label="Wartosc Sredniej Kroczacej")
plt.title('Wykres indeksu AAPL z srednia kroczaca')
plt.legend(loc='lower right')
plt.plot(czassygnal, sygnaly, marker='s')
plt.show()