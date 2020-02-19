import sys
import optparse

from worldgen.configuration import Configuration

class CustomOptionParser(optparse.OptionParser):
    """Used in instantiation"""
#     Don't think this is needed yet
#     def insert_option_group(self, idx, *args, **kwargs):
#         """Insert an Option Group at a given position."""
#         group = self.add_option_group(*args,**kwargs)
#
#         self.add_option_group.pop()
#         self.option_groups.insert(idx, group)
#
#         return group

class ConfigOptionParser(CustomOptionParser):

    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name')

        self.config = Configuration()

        assert self.name
        optparse.OptionParser.__init__(self, *args, **kwargs)