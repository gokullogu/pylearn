import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('py_pandas/data.csv')

df.plot()

plt.show()

