from abc import ABC, abstractmethod
from typing import List, Optional

from components.data_input import DataInput, DataInputs
from models.errors import ModelBaseError


class ModelBase(ABC):
    """
    This class is responsible for defining the base template for a basic model.

    inherited by:
        models.PoissonModel
        models.LogNormalModel

    Attributes:
        samples (int): the number of samples to simulate over
    """
    def __init__(self, samples: int = 12) -> None:
        """
        The constructor for the ModelBase class.

        :param samples: (int) the number of samples for the distribution
        """
        self.samples: int = samples
        self._cached_results: Optional[List[float]] = None
        self.check_input()

    @abstractmethod
    def _calculate(self) -> List[float]:
        pass

    def calculate(self) -> List[float]:
        """
        Executes the calculation caching the results in the process.

        :return: (List[float]) the result of the simulation
        """
        self._cached_results = self._calculate()
        return self._cached_results

    def check_input(self) -> None:
        pass

    @property
    def cached_results(self) -> List[float]:
        if self._cached_results is None:
            raise ModelBaseError(message="trying to access cached results before actually caching results")
        return self._cached_results

    @property
    def total(self) -> float:
        return sum(self.cached_results)
