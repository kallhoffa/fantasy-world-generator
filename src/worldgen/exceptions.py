"""Exceptions used throughout package"""


class WorldgenError(Exception):
    """Base worldgen Error""""

class CommandError(WorldgenError):
    """Raised when there is an error in command-line arguments"""