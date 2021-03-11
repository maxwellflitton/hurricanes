from typing import List
from unittest import main, TestCase
from unittest.mock import patch

from components.data_input import DataInput, DataInputs
from models.base import ModelBaseError
from models.poisson import PoissonModel, PoissonModelError


class PoissonModelTest(TestCase):

    @patch("models.poisson.PoissonModel.check_input")
    def setUp(self, mock_check_input) -> None:
        self.landfall_rate: DataInput = DataInput(input_type=DataInputs.FLORIDA_LANDFALL_RATE, value=2.0)
        self.test: PoissonModel = PoissonModel(landfall_rate=self.landfall_rate)

    def tearDown(self) -> None:
        pass

    @patch("models.poisson.PoissonModel.check_input")
    def test___init__(self, mock_check_input):
        test: PoissonModel = PoissonModel(landfall_rate=self.landfall_rate)

        self.assertEqual(self.landfall_rate, test.landfall_rate)
        self.assertEqual(12, test.samples)
        mock_check_input.assert_called_once_with()

    def test_check_input(self):
        self.test.check_input()

        self.test.landfall_rate = DataInput(input_type=DataInputs.FLORIDA_MEAN, value=2.0)

        with self.assertRaises(PoissonModelError) as context:
            self.test.check_input()
        self.assertEqual(
            "the self.landfall_rate needs to be a landfall rate not a DataInputs.FLORIDA_MEAN", str(context.exception)
        )

    def test_calculate(self):
        """
        This test also checks the two properties of the base class and the meta action of the self.calculate
        which in-turn tests the self._calculate function.
        """
        with self.assertRaises(ModelBaseError) as context:
            self.test.cached_results
        self.assertEqual("trying to access cached results before actually caching results", str(context.exception))

        result: List[float] = self.test.calculate()

        self.assertEqual(12, len(result))
        self.assertEqual(12, len(self.test.cached_results))
        self.assertEqual(sum(result), self.test.total)

        for i in result:
            self.assertEqual(float, type(i))

        self.test.samples = 5
        self.assertEqual(5, len(self.test.calculate()))
        self.assertEqual(5, len(self.test.cached_results))


if __name__ == "__main__":
    main()
