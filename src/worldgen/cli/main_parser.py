import os
import sys

from worldgen.cli import cmdoptions
from worldgen.cli.parser import (
    ConfigOptionParser
)
from worldgen.commands import commands_dict
from worldgen.utils.misc import get_worldgen_version
from worldgen.exceptions import CommandError

def create_main_parser():

    parser_kw = {
        'add_help_option': False,
        'name': 'global',
    }

    parser = ConfigOptionParser(**parser_kw)
    parser.disable_interspersed_args()

    parser.version = get_worldgen_version()


    gen_opts = cmdoptions.make_option_group(cmdoptions.general_group, parser)
    parser.add_option_group(gen_opts)

    #create command listing for description
    description = [''] + [
        '{:27}{}\n'.format(name, command_info.summary)
        for name, command_info in commands_dict.items()
    ]
    parser.description = '\n'.join(description)

    return parser



def parse_command(args):
    # type: (List[str]) -> Tuple[str, List[str]]

    parser = create_main_parser()


    # Note: parser calls disable_interspersed_args(), so the result of this
    # call is to split the initial args into the general options before the
    # subcommand and everything else.
    # For example:
    #  args: ['--timeout=5', 'install', '--user', 'INITools']
    #  general_options: ['--timeout==5']
    #  args_else: ['install', '--user', 'INITools']
    general_options, args_else = parser.parse_args(args)

    ## --version
    if general_options.version:
        sys.stdout.write(parser.version) #type: ignore
        sys.stdout.write(os.linesep)
        sys.exit()

    if not args_else or (args_else[0] == 'help' and len(args_else) == 1):
        parser.print_help()
        sys.exit()

    #the subcommand name
    cmd_name = args_else[0]

    if cmd_name not in commands_dict:
        #guess = get_similar_commands(cmd_name)

        msg = ['unknown command "{}"'.format(cmd_name)]
        #if guess:
            #msg.append('maybe you mean "{}"'.format(guess))

        raise CommandError(' - '.join(msg))

    #all the args without the subcommand
    cmd_args = args[:]
    cmd_args.remove(cmd_name)

    return cmd_name, cmd_args