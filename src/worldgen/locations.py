import sys

def get_major_minor_version():
    # type: () -> str
    """
    Return the major-minor version of the current Python as a string, e.g.
    "3.7"
    """

    return '{}.{}'.format(*sys.version_info)