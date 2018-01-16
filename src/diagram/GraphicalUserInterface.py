#See https://python-graph-gallery.com/line-chart/
#https://matplotlib.org/examples/widgets/buttons.html

# libraries

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons
from src.systemInput import Type
from matplotlib.widgets import CheckButtons


class GraphicalUserInterface:

    def drawGraphic(self, model):
        """
        draw model-diagrams
        :param model: 
        :return: 
        
        """
        x = list(range(model.starttime, model.endtime + 1, model.timestep))
        dict = {}
        listName = list()
        listName.append('all')


        counter = 0

        for variable in model.listSystemVariable:
            if variable.type != Type.Type.constant:
                dict[variable.name] = variable.valueHistoryList
                listName.append(variable.name)



        length= len(dict)
        col = 0
        if(length <= 6):
            col = 2
        else:
            col = 3
        row = int(length/2)

        counter = 1

        def definitionAll(col, counter, dict, row, x):
            for i in dict:
                plt.subplot(col, row, counter)
                counter += 1
                plt.plot(x, dict[i], visible=True, lw=1)
                plt.xlabel('Time')
                plt.title(i)
                plt.tight_layout()
                plt.subplots_adjust(left=0.3)
                plt.grid()

        definitionAll(col, counter, dict, row, x)

        rax = plt.axes([0.025, 0.5, 0.03*length, 0.04*length])
        radio = RadioButtons(rax, listName)

        def func(label):
            if(label=='all'):
                definitionAll(col, counter, dict, row, x)
                plt.draw()
            else:
                #needed because otherwith 2 lines in one figure
                plt.subplot(2,2,1)
                plt.draw()
                plt.subplot(1, 1, 1)
                plt.plot(x, dict[label], lw=1)
                plt.xlabel('Time')
                plt.title(label)
                plt.grid()
                plt.draw()


        radio.on_clicked(func)

        wm = plt.get_current_fig_manager()
        wm.window.state('zoomed')

        plt.show()