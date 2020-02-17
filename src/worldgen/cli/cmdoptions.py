"""
shared options and groups
The principle here is to define options once, but *not* instantiate them
globally. One reason being that options with action='append' can carry state
between parses. worldgen parses general options twice internally, and shouldn't
pass on state. To be consistent, all options will follow this design.
"""
from functools import partial
from optparse import OptionGroup, Option

def make_option_group(group, parser):

    #type: (Dict[str, Any], ConfigOptionParser) -> OptionGroup
    """
    Return an OptionGroup object
    group  -- assumed to be dict with 'name' and 'options' keys
    parser -- an optparse Parser
    """
    option_group = OptionGroup(parser, group['name'])
    for option in group['options']:
        option_group.add_option(option())
    return option_group


###########
# options #
###########

help_ = partial(
    Option,
    '-h', '--help',
    dest='help',
    action='help',
    help='Show help.',
) # type : Callable[..., Option]

version = partial(
    Option,
    '-V', '--version',
    dest='version',
    action='store_true',
    help='Show version and exit.',
)  # type: Callable[..., Option]

##########
# groups #
##########

general_group = {
    'name': 'General Options',
    'options': [
        help_,
        version,
    ]
} # type: Dict[str, Any]