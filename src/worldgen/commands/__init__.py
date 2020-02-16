from collections import OrderedDict, named tuple

CommandInfo = namedtuple('CommandInfo', 'module_path, class_name, summary')

commands_dict = OrderedDict([
    ('create', CommandInfo(
        'worldgen.commands.create', 'CreateCommand',
        'Create a new world.',
    )),
]) #type: OrderedDict[str, CommandInfo]