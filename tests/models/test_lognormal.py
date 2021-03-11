from typing import List
from unittest import main, TestCase
from unittest.mock import patch

from components.data_input import DataInput, DataInputs
from models.lognormal import LogNormalModel, LogNormalModelError


class LogNormalModelTest(TestCase):

    @patch("models.lognormal.LogNormalModel.check_input")
    def setUp(self, mock_check_input) -> None:
        self.mean: DataInput = DataInput(input_type=DataInputs.FLORIDA_MEAN, value=2.0)
        self.variance: DataInput = DataInput(input_type=DataInputs.FLORIDA_STDDEV, value=2.0)
        self.test: LogNormalModel = LogNormalModel(mean=self.mean, variance=self.variance)

    def tearDown(self) -> None:
        pass

    @patch("models.lognormal.LogNormalModel.check_input")
    def test___init__(self, mock_check_input):
        test: LogNormalModel = LogNormalModel(mean=self.mean, variance=self.variance)

        self.assertEqual(self.mean, test.mean)
        self.assertEqual(self.variance, test.variance)
        self.assertEqual(12, test.samples)
        mock_check_input.assert_called_once_with()

    def test_check_input(self):
        self.test.check_input()

        self.test.mean = self.variance

        with self.assertRaises(LogNormalModelError) as context:
            self.test.check_input()
        self.assertEqual("the self.mean needs to be a mean not a DataInputs.FLORIDA_STDDEV", str(context.exception))

        self.test.mean = self.mean
        self.test.variance = self.mean

        with self.assertRaises(LogNormalModelError) as context:
            self.test.check_input()
        self.assertEqual("the self.variance needs to be a mean not a DataInputs.FLORIDA_MEAN", str(context.exception))

    def test_calculate(self):
        """
        Basic tests for the meta around self.calculate() is tested in the PoissonModelTest as well as the dynamic
        properties in the base class.
        """
        result: List[float] = self.test.calculate()

        for i in result:
            self.assertEqual(float, type(i))

        self.assertEqual(self.test.samples, len(result))


if __name__ == "__main__":
    main()
