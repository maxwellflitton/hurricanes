

class PoissonModelError(Exception):
    """
    This class is responsible for raising errors in the Poisson model.
    """

    def __init__(self, message: str) -> None:
        """
        The constructor for the PoissonModelError class.

        :param message: (str) the message that will be logged for the error
        """
        super().__init__(message)


class ModelBaseError(Exception):
    """
    This class is responsible for raising errors in the base class of basic models.
    """

    def __init__(self, message: str) -> None:
        """
        The constructor for the ModelBaseError class.

        :param message: (str) the message that will be logged for the error
        """
        super().__init__(message)


class LogNormalModelError(Exception):
    """
    This class is responsible for raising errors in the lognormal model.
    """

    def __init__(self, message: str) -> None:
        """
        The constructor for the LogNormalModelError class.

        :param message: (str) the message that will be logged for the error
        """
        super().__init__(message)
