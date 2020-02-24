from worldgen.cli.base_command import Command
import numpy as np
import datetime

class CreateCommand(Command):
    """
    Create a new world to run simulations on.
    """

    usage = """worldgen create [options] ..."""
    def __init__(self, *args, **kwargs):
        super(CreateCommand, self).__init__(*args, **kwargs)

        cmd_opts = self.cmd_opts

        cmd_opts.add_option(
            '--width',
            action='store',
            dest='item_width',
            default='10',
            help="Set the width of the world. "
                 "Currently in matrix width. ",
        )

        cmd_opts.add_option(
            '--height',
            action='store',
            dest='item_height',
            default='10',
            help="Set the height of the world. "
                 "Currently in matrix height. ",
        )

        cmd_opts.add_option(
            '--name',
            action='store',
            dest='item_name',
            default=''.join(['worldgen_world_', datetime.now()]),
            help="Set the name for your new world.",
        )

        cmd_opts.add_option(
            '--path',
            action='store',
            dest='file_path',
            default='..'
        )

        print("Int Create")

    def run(self, options, args):
        print("Running create. Your string is {}".format(args))

        if (args[0].lower() == "world") :

            self.height = int(options.item_height)
            self.width = int(options.item_width)
            self.name = int(options.item_name)

            a = np.arange( self.width * self.height ).reshape( self.width, self.height )
            np.save(self.name, a)

            print(a)
        else :
            print("{} is not an option for create".format(args[0]))
