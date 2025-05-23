import sys
import os
import pytest

from unittest.mock import patch

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper_functions import remove_file
from spray.spray import Spray, main

def test_main_with_valid_param(capfd):
    """
    Test the main function with a valid parameter-set.
    """
    test_yaml_file = "test_file.yml"
    remove_file(test_yaml_file)
    # Patch sys.argv with valid arguments
    with patch("sys.argv", ["spray.py", "-y", test_yaml_file, "new", "a,b,c"]):
        main()

    # Check that the file was created
    assert os.path.exists(test_yaml_file)

    # remove YAML test-file
    remove_file(test_yaml_file)


def test_main_with_missing_input(capfd):
    """
    Test the main function when the input parameter is missing.
    """
    test_yaml_file = "test_file.yml"
    remove_file(test_yaml_file)
    # Mock sys.argv to simulate missing arguments
    with patch("sys.argv", ["spray.py", "-y", test_yaml_file, "new"]):
        with pytest.raises(SystemExit) as excinfo:  # Expecting sys.exit() due to error
            main()

        # Assert the exit code is 2 (error exit from argparse)
        assert excinfo.value.code == 2

    # Check that the file was not created
    assert (not os.path.exists(test_yaml_file))

    # Capture the output
    captured = capfd.readouterr()
    print("#"*30)
    print(captured)
    print("#"*30)
    assert "usage: " in captured.err  # Assert usage message is in stderr
