from enum import Enum


class DataInputs(Enum):
    """
    This class defines the different types of inputs available.
    """
    FLORIDA_MEAN = "fm"
    FLORIDA_STDDEV = "fv"
    FLORIDA_LANDFALL_RATE = "flr"
    GULF_MEAN = "gm"
    GULF_STDDEV = "gv"
    GULF_LANDFALL_RATE = "glr"
