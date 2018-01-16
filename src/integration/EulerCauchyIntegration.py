import pydoc

class EulerCauchyIntegration:

    def integrate(self, timestep, level):
        """
        calculate new state
        See Bossel Page 131
        :param levels: levels of the model
        :return: 
        """
        level.newValue = level.currentValue + level.calculateChange() * timestep
            




