#!/usr/bin/python
#

import argparse
import logging


def main():
    """main function of yaml2xls project.

    This function handles the command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--debug", action="store_true", dest="debug", default=False,
        help="show debug output at console"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", dest="verbose", default=False,
        help="show more console output"
    )
    parser.add_argument(
        "-y","--yaml_file",
        help="YAML based input file.",
        default=None
    )
    # Parser arguments
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    elif args.debug:
        logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    main()