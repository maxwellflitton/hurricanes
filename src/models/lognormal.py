from typing import List

from numpy.random import lognormal

from components.data_input import DataInput, DataInputs
from models.base import ModelBase
from models.errors import LogNormalModelError


class LogNormalModel(ModelBase):
    """
    This class is responsible for producing a lognormal distribution.

    Attributes:
        mean (DataInput): the mean of which the model is to be created from
        variance (DataInput): the variance of which the model is to be created from
        samples (int): the number of samples to simulate over
    """
    def __init__(self, mean: DataInput, variance: DataInput, samples: int = 12) -> None:
        """
        The constructor for the ModelBase class.

        :param mean: (DataInput) the mean of which the model is to be created from
        :param variance: (DataInput) the variance of which the model is to be created from
        :param samples: (int) the number of sames for the year
        """
        self.mean: DataInput = mean
        self.variance: DataInput = variance
        super().__init__(samples=samples)

    def check_input(self) -> None:
        """
        Performs basic input checks insuring that the mean and variance is given, throwing errors if not.

        :return: None
        """
        if self.mean.input_type not in [DataInputs.FLORIDA_MEAN, DataInputs.GULF_MEAN]:
            raise LogNormalModelError(message=f"the self.mean needs to be a mean not a {self.mean.input_type}")
        if self.variance.input_type not in [DataInputs.FLORIDA_STDDEV, DataInputs.GULF_STDDEV]:
            raise LogNormalModelError(message=f"the self.variance needs to be a mean not a {self.variance.input_type}")

    def _check_input(self) -> None:
        """No extra checks needed as float checks are done by the DataInput class"""
        pass

    def _calculate(self) -> List[float]:
        """
        Calculates the lognormal distribution.

        :return: (List[float]) the result of the lognormal distribution
        """
        return [float(i) for i in lognormal(self.mean.value, self.variance.value, self.samples)]
