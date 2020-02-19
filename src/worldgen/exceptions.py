"""Exceptions used throughout package"""


class WorldgenError(Exception):
    """Base worldgen Error"""

class CommandError(WorldgenError):
    """Raised when there is an error in command-line arguments"""

class BadCommand(WorldgenError):
    """Raised when a command is not found"""