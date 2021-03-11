from typing import Optional

from components.data_input import DataInput
from models.lognormal import LogNormalModel


class SimulationYear:
    """
    This class is responsible for simulating the entire loss for the year.

    Attributes:
        variance (DataInput): the variance to configure the LogNormalModel
        mean (DataInput): the mean to configure the LogNormalModel
        samples (int): the number of samples for the LogNormalModel
    """
    def __init__(self, variance: DataInput, mean: DataInput, samples: int) -> None:
        """
        The constructor for the SimulationYear.

        :param variance: (DataInput) the variance to configure the LogNormalModel
        :param mean: (DataInput) the mean to configure the LogNormalModel
        :param samples: (int) the number of samples for the LogNormalModel
        """
        self.variance: DataInput = variance
        self.mean: DataInput = mean
        self.samples: int = samples
        self._total_loss: Optional[float] = None

    def simulate(self) -> None:
        """
        Runs the lognormal simulation storing the total of the results in self._total_loss.

        :return: None
        """
        lognormal: LogNormalModel = LogNormalModel(mean=self.mean, variance=self.variance, samples=self.samples)
        lognormal.calculate()
        self._total_loss = lognormal.total

    @property
    def total_loss(self) -> float:
        if self._total_loss is None:
            self.simulate()
        return self._total_loss
