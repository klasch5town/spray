#
#
#
import os

def remove_file(file_to_remove):
    if os.path.exists(file_to_remove):
        os.remove(file_to_remove)
