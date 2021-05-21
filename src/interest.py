import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

from os import path

dVal = "assets/interest.csv"
if not path.isfile(dVal):
    dVal = "../assets/interest.csv"

interest = pd.read_csv(dVal)

x = interest.Record_Date
y = interest.Average_Interest_Rate_Amount


plt.scatter(x, y)
plt.gcf().autofmt_xdate()
plt.gca().set_xlim(left=0, right=10)
plt.gca().set_ylim(bottom=0, top=3.5)
plt.grid(True)
plt.show()