import logging
import sys
from argparse import ArgumentParser

sys.path.insert(0, './src')

from enums.data_inputs import DataInputs
from enums.input_descriptions import DataInputDescriptions
from processes import simulation_years_factory


if __name__ == "__main__":
    parser = ArgumentParser(description='inputs for models')
    logger = logging.getLogger(__file__)

    parser.add_argument(DataInputs.FLORIDA_LANDFALL_RATE.value, type=float, help=DataInputDescriptions.FLORIDA_LANDFALL_RATE.value)
    parser.add_argument(DataInputs.FLORIDA_MEAN.value, type=float, help=DataInputDescriptions.FLORIDA_MEAN.value)
    parser.add_argument(DataInputs.FLORIDA_STDDEV.value, type=float, help=DataInputDescriptions.FLORIDA_STDDEV.value)

    parser.add_argument(DataInputs.GULF_LANDFALL_RATE.value, type=float, help=DataInputDescriptions.GULF_LANDFALL_RATE.value)
    parser.add_argument(DataInputs.GULF_MEAN.value, type=float, help=DataInputDescriptions.GULF_MEAN.value)
    parser.add_argument(DataInputs.GULF_STDDEV.value, type=float, help=DataInputDescriptions.GULF_STDDEV.value)
    parser.add_argument("n", type=int, help="Number of years for the simulation (optional default = 1)", default=1)

    args = parser.parse_args()

    try:
        result = simulation_years_factory(
            florida_mean=args.fm,
            florida_stddev=args.fv,
            flordia_landfall=args.flr,
            gulf_mean=args.gm,
            gulf_stddev=args.gv,
            gulf_landfall=args.glr,
            years=args.n
        )
        print("\n\n\n\nhere is the results")
        print(result)
        print("\n\n\n\n")

    except Exception as error:
        logger.error(error)
        print(error)
