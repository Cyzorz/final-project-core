import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

from os import path

from render import Render

class Plot:
    def __init__(self, title, xLabel, yLabel, file):
        self.file = file
        self.dVal = None
        plt.xlabel(title)
        plt.ylabel(xLabel)
        plt.title(yLabel)
        self.dVal = Render.load(file)
    
    def get_file(self):
        return self.dVal

    def plot(self, x, y, xMax, yMax, xMin=0, yMin=0):
        plt.scatter(x, y)
        plt.gcf().autofmt_xdate()
        plt.gca().set_xlim(left=xMin, right=xMax)
        plt.gca().set_ylim(bottom=yMin, top=yMax)
        plt.grid(True)
    
    def render_plot(self):
        return plt.show()
