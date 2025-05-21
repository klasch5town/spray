import sys
import os
import pytest

from unittest.mock import patch

# Prepare sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# 'Local' imports
from helper_functions import remove_file
from spray.spray import Spray, main

def test_create_yaml_file(capfd):
    """
    Test the creation of a yaml file
    """
    test_yaml_file = "./build/simple_table.yml"
    test_xls_file = "./examples/simple_table.xlsx"
    remove_file(test_yaml_file)
    # Patch sys.argv with valid arguments
    with patch("sys.argv", ["spray.py", "-y", test_yaml_file, "xls2yaml", "-x", test_xls_file]):
        main()

    # Check that the file was created
    assert os.path.exists(test_yaml_file)

    # remove YAML test-file
    remove_file(test_yaml_file)