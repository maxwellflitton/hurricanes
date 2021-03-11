from enum import Enum


class DataInputs(Enum):
    """
    This class defines the different types of inputs available.
    """
    FLORIDA_LANDFALL_RATE = "The annual rate of land falling hurricanes in Florida"
    FLORIDA_MEAN = "A LogNormal parameter that describe the economic loss of a land falling hurricane in Florida"
    FLORIDA_STDDEV = "A LogNormal parameter that describe the economic loss of a land falling hurricane in Florida"
    GULF_LANDFALL_RATE = "The annual rate of land falling hurricanes in the Gulf states"
    GULF_MEAN = "A LogNormal parameter that describe the economic loss of a land falling hurricane in the Gulf"
    GULF_STDDEV = "A LogNormal parameter that describe the economic loss of a land falling hurricane in the Gulf"