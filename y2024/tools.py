import os


def get_lines_in_file(filename) -> list[str]:
    """
    Function that opens the file passed as a parameter.
    Then puts all the lines in an array.
    """
    if os.path.exists(filename):
        with open(filename) as fp:
            return fp.read().splitlines()
    raise Exception('No input file !!')
