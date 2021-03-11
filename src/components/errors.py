

class DataInputError(Exception):
    """
    This class is responsible for throwing errors inside a data input for a parameter.
    """
    def __init__(self, message: str) -> None:
        """
        The constructor for the DataInputError class.

        :param message: (str) the message that will be logged for the error
        """
        super().__init__(message)
