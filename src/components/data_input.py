from components.errors import DataInputError
from enums.data_inputs import DataInputs


class DataInput:
    """
    This class is responsible for holding a parameter that has been given by the user, labelling it, and checking it.

    Attributes:
        input_type (DataInputs): the type of parameter being input
        value (float): the value assigned to the variable given by the user
    """
    def __init__(self, input_type: DataInputs, value: float) -> None:
        """
        The constructor for the DataInput class.

        :param input_type: (DataInputs) the type of parameter being input
        :param value: (float) the value assigned to the variable given by the user
        """
        self.input_type: DataInputs = input_type
        self.value: float = value
        self.check_float_input()

    def check_float_input(self) -> None:
        """
        Checks the self.value to ensure that is is a float, raising an error if not.

        :return: None
        """
        if not isinstance(self.value, float):
            raise DataInputError(
                message=f"input value for {self.input_type} needs to be a float, not a {type(self.value)}")
