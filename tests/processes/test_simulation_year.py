from unittest import main, TestCase
from unittest.mock import patch

from components.data_input import DataInput, DataInputs
from processes.simulation_year import SimulationYear


class SimulationYearTest(TestCase):

    def setUp(self) -> None:
        self.variance: DataInput = DataInput(input_type=DataInputs.FLORIDA_STDDEV, value=2.0)
        self.mean: DataInput = DataInput(input_type=DataInputs.FLORIDA_MEAN, value=2.0)
        self.test: SimulationYear = SimulationYear(variance=self.variance, mean=self.mean, samples=5)

    def tearDown(self) -> None:
        pass

    def test___init__(self):
        test: SimulationYear = SimulationYear(variance=self.variance, mean=self.mean, samples=5)

        self.assertEqual(self.variance, test.variance)
        self.assertEqual(self.mean, test.mean)
        self.assertEqual(5, test.samples)
        self.assertEqual(None, test._total_loss)

    @patch("processes.simulation_year.LogNormalModel")
    def test_simulate(self, mock_log_model):
        self.test.simulate()

        mock_log_model.assert_called_once_with(mean=self.mean, variance=self.variance, samples=5)
        mock_log_model.return_value.calculate.assert_called_once_with()
        self.assertEqual(mock_log_model.return_value.total, self.test._total_loss)

    @patch("processes.simulation_year.SimulationYear.simulate")
    def test_total_loss(self, mock_simulate):
        self.assertEqual(None, self.test.total_loss)
        self.test._total_loss = 50
        self.assertEqual(50, self.test.total_loss)
        mock_simulate.assert_called_once_with()


if __name__ == "__main__":
    main()
