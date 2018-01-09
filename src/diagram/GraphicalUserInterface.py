#See https://python-graph-gallery.com/line-chart/
#https://matplotlib.org/examples/widgets/buttons.html

# libraries

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from src.systemInput import Type


class GraphicalUserInterface:

    def onClick(self, variable):
        """
        Define on Click function for Button
        should draw diagram for clicked variable
        :param variable: 
        :return: 
        """
        self.window.set_ydata(variable.valueHistoryList)
        plt.draw()
        pass


    def drawGraphic(self, model):
        """
        draw model-diagrams
        :param model: 
        :return: 
        """
        fig, ax = plt.subplots()
        distance = 0.02
        plt.subplots_adjust(bottom=0.2)
        x = list(range(model.starttime, model.endtime+1, model.timestep))
        d = {} #https://stackoverflow.com/questions/6181935/how-do-you-create-different-variable-names-while-in-a-loop
        index = 0
        for variable in model.listSystemVariable:
            if index == 0 and variable.type != Type.Type.constant:
                self.window, = plt.plot(x, variable.valueHistoryList, lw=2)
                plt.title(variable.name)
                ax = plt.axes([distance, 0.05, 0.1, 0.075])
                distance += 0.111
                d["btn{0}".format(variable)] = Button(ax, variable.name)

                index += 1
            else:
                if variable.type != Type.Type.constant:
                    ax = plt.axes([distance, 0.05, 0.1, 0.075])
                    distance += 0.111
                    d["btn{0}".format(variable)] = Button(ax, variable.name)
                    #d["btn{0}".format(variable)].on_clicked(self.onClick(variable))
                    pass
        plt.show()





