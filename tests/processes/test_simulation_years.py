from unittest import main, TestCase
from unittest.mock import patch, MagicMock

from components.data_input import DataInput, DataInputs
from processes.simulation_years import SimulationYears, Locations


class SimulationYearsTest(TestCase):

    @patch("processes.simulation_years.SimulationYears._load_years")
    def setUp(self, mock__load_years) -> None:
        self.variance: DataInput = DataInput(input_type=DataInputs.FLORIDA_STDDEV, value=2.0)
        self.mean: DataInput = DataInput(input_type=DataInputs.FLORIDA_MEAN, value=2.0)
        self.landfall_rate: DataInput = DataInput(input_type=DataInputs.FLORIDA_LANDFALL_RATE, value=2.0)
        self.test: SimulationYears = SimulationYears(location=Locations.FLORIDA, variance=self.variance,
                                                     mean=self.mean, landfall_rate=self.landfall_rate, years=2)

    def tearDown(self) -> None:
        pass

    @patch("processes.simulation_years.SimulationYears._load_years")
    def test___init__(self, mock__load_years):
        test: SimulationYears = SimulationYears(location=Locations.FLORIDA, variance=self.variance,
                                                mean=self.mean, landfall_rate=self.landfall_rate, years=2)
        self.assertEqual([], test)
        self.assertEqual(Locations.FLORIDA, test.location)
        self.assertEqual(self.variance, test.variance)
        self.assertEqual(self.mean, test.mean)
        self.assertEqual(self.landfall_rate, test.landfall_rate)
        self.assertEqual(2, test.years)
        self.assertEqual(None, test._total_loss)
        mock__load_years.assert_called_once_with()

    @patch("processes.simulation_years.SimulationYear")
    def test__load_year(self, mock_simulation_year):
        self.test._load_year(samples=4)

        mock_simulation_year.assert_called_once_with(variance=self.variance, mean=self.mean, samples=4)
        self.assertEqual([mock_simulation_year.return_value], self.test)

    @patch("processes.simulation_years.SimulationYears._load_year")
    @patch("processes.simulation_years.PoissonModel")
    def test__load_years(self, mock_poisson_model, mock__load_year):
        mock_poisson_model.return_value.cached_results = [3, 7, 2]
        self.test._load_years()

        mock_poisson_model.assert_called_once_with(landfall_rate=self.landfall_rate, samples=2)

        self.assertEqual({"samples": 3}, mock__load_year.call_args_list[0][1])
        self.assertEqual({"samples": 7}, mock__load_year.call_args_list[1][1])
        self.assertEqual({"samples": 2}, mock__load_year.call_args_list[2][1])

    def test_total_and_average(self):
        one = MagicMock()
        two = MagicMock()
        three = MagicMock()

        one.total_loss = 1
        two.total_loss = 2
        three.total_loss = 3

        self.test.append(one)
        self.test.append(two)
        self.test.append(three)

        self.assertEqual(6, self.test.total)
        self.assertEqual(2, self.test.average)


if __name__ == "__main__":
    main()
