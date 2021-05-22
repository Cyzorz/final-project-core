import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

    def date_plot(self, xMax, yMax, xMin=0, yMin=0):
        plt.gcf().autofmt_xdate()
        plt.gca().set_xlim(left=xMin, right=xMax)
        plt.gca().set_ylim(bottom=yMin, top=yMax)

    def add_style(self, style):
        try:
            plt.style.use(style)
        except FileNotFoundError and OSError:
            print("ERROR: Invalid Style!")
            return

    def scatter(self, x, y):
        plt.scatter(x, y)
        plt.grid(True)

    def plot(self, x, y):
        plt.plot(x, y)  
        plt.grid(True)

    def render_plot(self):
        return plt.show()