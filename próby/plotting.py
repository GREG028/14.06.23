import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

# X = np.linspace(0, 2*np.pi, 100)
# Y = np.cos(X)

# fig, ax = plt.subplots()
# ax.plot(X, Y, color='green')

# fig.savefig("figure.pdf")
# plt.show()


aapl =  pd.read_csv("./data/AAPL.csv")

mpl.use('MacOSX')
aapl['Close'].plot(figsize=(8,8), label='Apple')
plt.show()

