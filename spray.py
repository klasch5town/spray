#!/usr/bin/python
#

import argparse
import logging
import os.path
import sys
import yaml

class Spray():
    """This class handles all 'spreadsheet' aspects.
    """
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
        if os.path.exists(self.yaml_file):
            with open(self.yaml_file, 'r') as yfh:
                self.yct = yaml.safe_load(yfh)
        else: self.yct = None

    def create(self, header):
        """Create a 'table' by creating the very first yaml entry as table header.

        Args:
            header (list): list with header content
        """
        if os.path.exists(self.yaml_file):
            sys.exit(f"YAYML file {self.yaml_file} already exists")
        tbl_header = [{}]
        for item in header.split(","):
            tbl_header[0][item]=item
        self.yct = yaml.dump(tbl_header)
        with open(self.yaml_file, "w") as yfh:
            yaml.dump(tbl_header, yfh, sort_keys=False)


def main():
    """main function of spray project.

    The main function handles the command line arguments.
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
        'input',
        help="input to handle with the given task"
    )
    parser.add_argument(
        "-t","--task",
        help="the task to do, like:" \
        "- create",
        default=None
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

    spray = Spray(args.yaml_file)

    if args.task == "create":
        spray.create(args.input)


if __name__ == '__main__':
    main()