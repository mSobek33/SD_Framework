import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from src.systemInput import Type

class GraphicalUserInterface:
    """
    Class to define the GUI to display the results.
    """

    def drawGraphic(self, model):
        """
        draw model-diagrams
        :param model: the current System dynamic model
        :return: nothing
        """

        x = list(range(model.starttime, model.endtime + 1, model.timestep))

        dict = {} #lists all Variable
        listName = list()
        listName.append('all')

        for variable in model.listSystemVariable:
            if variable.type != Type.Type.constant:
                dict[variable.name] = variable.valueHistoryList
                listName.append(variable.name)


        length = len(dict)
        column = 0
        if(length <= 6):
            column = 2
        else:
            column = 3
        row = int(length/2)

        diagramPositionCounter = 1

        def definitionAll(col, counter, dict, row, x):
            """
            define window, where all diagrams shown.
            :param col: column
            :param counter: diagram position counter
            :param dict: list of all systemVariables
            :param row: row
            :param x: x-values
            :return: 
            """
            for variale in dict:
                plt.subplot(col, row, counter)
                counter += 1
                plt.plot(x, dict[variale], visible=True, lw=1)
                plt.xlabel('Time')
                plt.title(variale)
                plt.tight_layout()
                plt.subplots_adjust(left=0.3)
                plt.grid()

        definitionAll(column, diagramPositionCounter, dict, row, x)

        #Radiobutton Bar
        rax = plt.axes([0.025, 0.5, 0.03*length, 0.04*length])
        radio = RadioButtons(rax, listName)

        def func(label):
            """
            define the diagram window depending on the selected label.
            :param label: 
            :return: 
            """
            if(label=='all'):
                definitionAll(column, diagramPositionCounter, dict, row, x)
                plt.draw()
            else:
                #needed because otherwise 2 lines in one figure
                plt.subplot(2,2,1)
                plt.draw()
                plt.subplot(1, 1, 1)
                plt.plot(x, dict[label], lw=1)
                plt.xlabel('Time')
                plt.title(label)
                plt.grid()
                plt.draw()

        radio.on_clicked(func)

        #window with maximum expansion
        wm = plt.get_current_fig_manager()
        wm.window.state('zoomed')

        plt.show()