import numpy as np
import pandas as pd
# import numpy as np
def read():
    df=pd.read_csv("AAPL.csv")
    data = df["Close"]

    dane = list(df["Close"])

    print(dane)


def srednia():
    p = 0
    print("Aby rozpoczac, wpisz dlugosc serdnii, ktora ma obliczac program")
    l = int(input())
    m = np.zeros(l)
    s = 0
    print(f"Witaj w programie obliczajacym serdnie z {l} !!!\nDawaj {l}")
    while p < l:
        m[p] = float(input())
        s += m[p]
        p += 1
    print("Swietnie !!! Teraz mozemy liczyc nowa serdnie po kazdej wpisanej wartosci !!!\nDawaj NAN")
    while True:
        print(f"Twoja serdnia to {s/l} !!!")
        p = (p+1)%l
        s -= m[p]
        m[p] = float(input())
        s += m[p]
