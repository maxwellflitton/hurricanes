from typing import List

from numpy.random import poisson

from components.data_input import DataInput, DataInputs
from models.base import ModelBase
from models.errors import PoissonModelError


class PoissonModel(ModelBase):
    """
    This class is responsible for producing a poisson distribution.

    Attributes:
        landfall_rate (DataInput): the mean landfall rate for the poisson model
    """
    def __init__(self, landfall_rate: DataInput, samples: int = 12) -> None:
        """
        The constructor for the PoissonModel class.

        :param landfall_rate: (DataInput) the mean landfall rate for the poisson model
        :param samples: (int) the number of years to simulate over
        """
        self.landfall_rate: DataInput = landfall_rate
        super().__init__(samples=samples)

    def check_input(self) -> None:
        """
        Performs basic input checks insuring that the landfall rate was given, throwing errors if not.

        :return: None
        """
        if self.landfall_rate.input_type not in [DataInputs.FLORIDA_LANDFALL_RATE, DataInputs.GULF_LANDFALL_RATE]:
            raise PoissonModelError(
                message=f"the self.landfall_rate needs to be a landfall rate not a {self.landfall_rate.input_type}"
            )

    def _calculate(self) -> List[float]:
        """
        Calculates the poisson distribution.

        :return: (List[float]) the result of the poisson distribution
        """
        return [float(i) for i in poisson(lam=self.landfall_rate.value, size=self.samples)]
