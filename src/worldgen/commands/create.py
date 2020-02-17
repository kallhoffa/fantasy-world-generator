from worldgen.cli.base_command import Command
import numpy as np

class CreateCommand(Command):
    """
    Create a new world to run simulations on.
    """

    usage = """worldgen create [options] ..."""
#     def __init__(self, *args, **kwargs):
#
#         cmd_opts = self.cmd_opts
#
#         print("Int Create")

    def run(self, options, args):
        print("Running create. Your string is {}".format(args))