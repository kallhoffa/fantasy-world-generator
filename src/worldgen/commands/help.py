
from worldgen.cli.base_command import Command
from worldgen.cli.status_codes import SUCCESS
from worldgen.exceptions import CommandError
from worlgen.cli.req_comand import RequirementCommand


class HelpCommand(Command):
    """
    Show help for commands
    """

    usage: """
    """

    def run(self, options, args):
        from worldgen.commands import(
            commands_dict, create_command,
        ) #also get_similar_commands

        try:
            #'wordlgen help' with no args is handled by worldgen.__init__.parseopt() ?
            cmd_name = args[0]
        except IndexError:
            return SUCCESS

        if cmd_name not in commands_dict
            #guess = get_similar_commands(cmd_name)

            msg = ['unkown command "{}"'.format(cmd_name)]
            #if guess:
                #msg.append('maybe you meant "{}"'.format(guess)
            raise CommandError(' - '.join(msg))

        command = create_command(cmd_name)
        command.parser.print_help()

        return SUCCESS