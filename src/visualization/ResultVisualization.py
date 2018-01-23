import csv
import copy
import importlib

try:
    importlib.import_module('matplotlib')
except ImportError:
    import pip
    pip.main(['install', 'matplotlib'])
finally:
    globals()['matplotlib'] = importlib.import_module('matplotlib')

if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    import matplotlib.pyplot as plt
    from matplotlib.widgets import RadioButtons
    from systemInput import Constant
else:
    import matplotlib.pyplot as plt
    from matplotlib.widgets import RadioButtons
    from systemInput import Constant

class ResultVisualization:
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
            if isinstance(variable, Constant.Constant) == False:
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
            :param counter: visualization position counter
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
            define the visualization window depending on the selected label.
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



    def __localize_floats(self, row):
        """
        Function to change decimal seperator
        Source: https://stackoverflow.com/questions/39833555/how-to-write-a-csv-with-a-comma-as-decimal-separator
        :param row: current row
        :return: updatet row
        """
        return [
            str(el).replace('.', ',') if isinstance(el, float) else el
            for el in row
        ]



    def createCSV(self, model, path):
        """
        prit results in CSV-File
        :param model: the current System dynamic model
        :param path: csv-path
        :return: 
        """
        with open(path, 'w', newline='') as output:
            writer = csv.writer(output, delimiter=";")
            for variable in model.listSystemVariable:
                if isinstance(variable, Constant.Constant) == False:
                    list = copy.copy(variable.valueHistoryList)
                    list.insert(0,variable.name)
                    writer.writerow(self.__localize_floats(list))
