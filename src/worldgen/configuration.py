import sys

class Configuration(object):

    def __init__(self, load_only=None):
        self.load_only = load_only

        self._ignore_env_names = ["version", "help"]

