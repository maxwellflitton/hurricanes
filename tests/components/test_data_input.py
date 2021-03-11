from unittest import main, TestCase
from unittest.mock import patch

from components.data_input import DataInput, DataInputs, DataInputError


class DataInputTest(TestCase):

    @patch("components.data_input.DataInput.__init__")
    def setUp(self, mock_init) -> None:
        mock_init.return_value = None
        self.test = DataInput(input_type=DataInputs.FLORIDA_MEAN, value=5.6)
        self.test.value = 5.6
        self.test.input_type = DataInputs.FLORIDA_MEAN

    def tearDown(self) -> None:
        pass

    @patch("components.data_input.DataInput.check_float_input")
    def test___init__(self, mock_check_float_input):
        test: DataInput = DataInput(input_type=DataInputs.FLORIDA_MEAN, value=5.6)

        self.assertEqual(5.6, test.value)
        self.assertEqual(DataInputs.FLORIDA_MEAN, test.input_type)
        mock_check_float_input.assert_called_once_with()

    def test_check_float_input(self):
        self.test.check_float_input()

        self.test.value = "test"

        with self.assertRaises(DataInputError) as context:
            self.test.check_float_input()
        self.assertEqual("input value for DataInputs.FLORIDA_MEAN needs to be a float, not a <class 'str'>",
                         str(context.exception))


if __name__ == "__main__":
    main()
