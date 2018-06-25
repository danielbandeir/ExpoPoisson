# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class poisson(object):

    def __init__(self):
        stopTimes = []
        times = []
        self.stopTimes = stopTimes
        self.times = times

    def importPoisson(self, enterArchive):
        database = open('import/'+enterArchive+'.csv', 'r')

        for count in database:
            count = count.strip()
            stop, time = count.split(',')
            self.stopTimes.append(stop)
            self.times.append(time)
            self.stopTimes = sorted(self.stopTimes)

        return self.stopTimes, self.times

        database.close()

    def plotGraphic(self):

        fig = plt.figure(figsize=(10, 5))

        ax = fig.add_subplot(1, 1, 1)
        ax.step(self.times, self.stopTimes, label="Paradas")
        ax.legend
        ax.set_title("Poisson")
        ax.set_xlabel("Tempo")
        ax.set_ylabel("Paradas")
        plt.show()
