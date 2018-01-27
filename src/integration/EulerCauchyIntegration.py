
class EulerCauchyIntegration:
    """
    EulerCauchyIntegration-Class for the system dynamic simulation model
    """

    def integrate(self, timestep, level):
        """
        calculate new state
        source: Bossel, Systeme Dynamik Simulation, Page 131
        :param levels: level to integrate
        :return: nothing
        """
        level.newValue = level.currentValue + level.calculateChange() * timestep
