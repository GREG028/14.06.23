import pandas as pd
# import numpy as np

df=pd.read_csv("./data/AAPL.csv")
data = df["Close"]

dane = list(df["Close"])

print(dane)