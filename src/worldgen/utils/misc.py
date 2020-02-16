import os

from worldgen import __version__
from worldgen.locations import (
    get_major_minor_version,
)

def get_worldgen_version():
    worldgen_pkg_dir = os.path.join(os.path.dirname(__file__), "..", "..")
    worldgen_pkg_dir = os.path.abspath(worldgen_pkg_dir)

    return (
        'worldgen {} from {} (python {})'.format(
            __version__, worldgen_pkg_dir, get_worldgen_version(),
        )
    )