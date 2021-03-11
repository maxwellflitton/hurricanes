from typing import Optional

from components.data_input import DataInput
from enums.locations import Locations
from models.poisson import PoissonModel
from processes.simulation_year import SimulationYear


class SimulationYears(list):
    """
    This class is responsible for simulating multiple years.

    Attributes:
        location (Locations): the location of the calculations
        variance (DataInput): the variance of hurricanes in the location
        mean (DataInput): the mean of hurricanes in the location
        years (int): the number of years of the simulations
    """
    def __init__(self, location: Locations, variance: DataInput,
                 mean: DataInput, landfall_rate: DataInput, years: int) -> None:
        """
        The constructor for the SimulationYears class.

        :param location: (Locations) the location of the calculations
        :param variance: (DataInput) the variance of hurricanes in the location
        :param mean: (DataInput) the mean of hurricanes in the location
        :param landfall_rate: (DataInput) the mean landfall rate for the poisson model
        :param years: (int) the number of years of the simulations
        """
        super().__init__()
        self.location: Locations = location
        self.variance: DataInput = variance
        self.mean: DataInput = mean
        self.landfall_rate: DataInput = landfall_rate
        self.years: int = years
        self._total_loss: Optional[float] = None
        self._load_years()

    def _load_year(self, samples: int) -> None:
        """
        Loads a SimulationYear and appends it to self.

        :param samples: (int) the number of samples needed for the LogNormalModel in the SimulationYear
        :return: None
        """
        year: SimulationYear = SimulationYear(variance=self.variance, mean=self.mean, samples=samples)
        self.append(year)

    def _load_years(self) -> None:
        """
        Fires the PoissonModel firing the self._load_year function for each year.

        :return: None
        """
        poisson: PoissonModel = PoissonModel(landfall_rate=self.landfall_rate, samples=self.years)
        poisson.calculate()

        # TODO => This is where we would implement multithreading to speed up the calculation process
        for year in poisson.cached_results:
            self._load_year(samples=int(year))

    @property
    def total(self) -> float:
        return sum([i.total_loss for i in self])

    @property
    def average(self) -> float:
        return self.total / len(self)
