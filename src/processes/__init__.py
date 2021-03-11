from typing import Dict

from components.data_input import DataInput, DataInputs
from enums.locations import Locations
from processes.simulation_years import SimulationYears


def simulation_years_factory(florida_mean: float, florida_stddev: float, gulf_mean: float, gulf_stddev: float,
                             gulf_landfall: float, flordia_landfall: float, years: int = 1) -> Dict[str, float]:
    """
    This factory takes the inputs from the command line and packages them in DataInput objects, passing them through
    to the SimulationYears objects to calculate the averages of the loss over a number of years for each location.

    :param florida_mean: (float) the mean economic loss of a land falling hurricane in Florida
    :param florida_stddev: (float) the variance of the economic loss of a land falling hurricane in Florida
    :param gulf_mean: (float) the mean economic loss of a land falling hurricane in the Gulf
    :param gulf_stddev: (float) the variance of the economic loss of a land falling hurricane in the Gulf
    :param gulf_landfall: (float) The annual rate of landfalling hurricanes in the Gulf states
    :param flordia_landfall: (float) The annual rate of landfalling hurricanes in Florida
    :param years: (int) number of years for the simulation
    :return: (Dict[str, float]) the average loss over the years for florida and gulf
    """
    florida_mean: DataInput = DataInput(input_type=DataInputs.FLORIDA_MEAN, value=florida_mean)
    florida_stddev: DataInput = DataInput(input_type=DataInputs.FLORIDA_STDDEV, value=florida_stddev)
    gulf_mean: DataInput = DataInput(input_type=DataInputs.GULF_MEAN, value=gulf_mean)
    gulf_stddev: DataInput = DataInput(input_type=DataInputs.GULF_STDDEV, value=gulf_stddev)
    flordia_landfall: DataInput = DataInput(input_type=DataInputs.FLORIDA_LANDFALL_RATE, value=flordia_landfall)
    gulf_landfall: DataInput = DataInput(input_type=DataInputs.GULF_LANDFALL_RATE, value=gulf_landfall)

    florida_year = SimulationYears(location=Locations.FLORIDA, variance=florida_stddev, mean=florida_mean,
                                   landfall_rate=flordia_landfall, years=years)
    gulf_year = SimulationYears(location=Locations.GULF, variance=gulf_stddev, mean=gulf_mean,
                                landfall_rate=gulf_landfall, years=years)

    billion = 1000000000

    return {
        "florida average": florida_year.average / billion,
        "gulf average": gulf_year.average / billion,
        "total average": ((florida_year.average + gulf_year.average) / 2) / billion
    }
