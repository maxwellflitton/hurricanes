from enum import Enum


class DataInputDescriptions(Enum):
    """
    This class defines the different types of inputs available.
    """
    FLORIDA_MEAN = "A LogNormal parameter that describes the economic loss of a land falling hurricane in Florida"
    FLORIDA_STDDEV = "A LogNormal parameter that describe the economic loss of a land falling hurricane in Florida"
    FLORIDA_LANDFALL_RATE = "The annual rate of landfalling hurricanes in Florida"
    GULF_MEAN = "A LogNormal parameter that describe the economic loss of a land falling hurricane in the Gulf"
    GULF_STDDEV = "A LogNormal parameter that describe the economic loss of a land falling hurricane in the Gulf"
    GULF_LANDFALL_RATE = "The annual rate of landfalling hurricanes in the Gulf states"
