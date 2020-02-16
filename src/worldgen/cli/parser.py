import sys
import optparse

from worldgen.configuration import Configuration

class ConfigOptionParser(CustomOptionParser):

    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name')

        self.config = Configuration()

        assert self.name
        optparse.OptionParser.__init__(self, *args, **kwargs)