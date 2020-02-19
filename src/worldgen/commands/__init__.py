import importlib
from collections import OrderedDict, namedtuple

CommandInfo = namedtuple('CommandInfo', 'module_path, class_name, summary')

# The ordering matters for help display.
#    Also, even though the module path starts with the same
# "worldgen.commands" prefix in each case, we include the full path
# because it makes testing easier (specifically when modifying commands_dict
# in test setup / teardown by adding info for a FakeCommand class defined
# in a test-related module).
#    Finally, we need to pass an iterable of pairs here rather than a dict
# so that the ordering won't be lost when using Python 2.7.
commands_dict = OrderedDict([
    ('create', CommandInfo(
        'worldgen.commands.create', 'CreateCommand',
        'Create a new world.',
    )),
    ('help', CommandInfo(
            'worldgen.commands.help', 'HelpCommand',
            'Show help for commands.',
    )),
]) #type: OrderedDict[str, CommandInfo]

def create_command(name, **kwargs):
    #type: (str, **Any) -> Command
    """
    Create an instance of the Command class with the given name.
    """
    module_path, class_name, summary = commands_dict[name]
    module = importlib.import_module(module_path)
    command_class = getattr(module, class_name)
    command = command_class(name=name, summary=summary, **kwargs)

    return command