""" Primary application entrypoint
"""

import sys

# unfinished
from worldgen.cli.main_parser import parse_command
# unfinished
from worldgen.commands import create_command

def main(args=None):

    if args is None:
        args = sys.argv[1:]

#      insert autocompeletion

    try:
        cmd_name, cmd_args = parse_command(args)
    except:
#         create worldgen error

    command = create_command(cmd_name)

    return command.main(cmd_args)