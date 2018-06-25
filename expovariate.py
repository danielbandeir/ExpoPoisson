# -*- coding: utf-8 -*-

import matplotlib.pyplot as plot
import random
import math

class expovariate(object):

    def __init__(self):
        numbers = []
        mtiExp = []
        self.numbers = numbers
        self.mtiExp = mtiExp


    def calcExpovariate(self, lambd, sampleSpace):
        for count in range(sampleSpace):
            self.numbers.append(random.expovariate(lambd))

        return self.numbers

    def calcExpovariateSimulation(self, lambd, sampleSpace):
        for count in range(sampleSpace):
            calcMtiExp = -(math.log(random.uniform(0,1))) / lambd
            self.mtiExp.append(calcMtiExp)
            calcMtiExp = 0

        return self.mtiExp

    def plotHist(self):
        fig = plot.figure(figsize=(10, 5))

        ax = fig.add_subplot(1, 2, 1)
        ax.hist(self.numbers)
        ax.set_title("Exponencial do Python")

        ax1 = fig.add_subplot(1, 2, 2)
        ax1.hist(self.mtiExp)
        ax1.set_title("Exponencial do Método da transformação inversa")

        plot.show()
