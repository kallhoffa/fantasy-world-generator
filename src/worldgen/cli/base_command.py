import logging
import optparse

from worldgen.cli import cmdoptions
from worldgen.cli.command_context import CommandContextMixIn
from worldgen.cli.parser import ConfigOptionParser
from worldgen.exceptions import (
    CommandError,
    BadCommand
)
from worldgen.cli.status_codes import (
    ERROR,
    SUCCESS,
)

logger = logging.getLogger(__name__)

class Command(CommandContextMixIn):

    usage = None #type: str
#     ignore_require_

    def __init__(self, name, summary):
        #type: (str, str, bool) -> None
        super(Command, self).__init__()
        parser_kw = {
            'usage': self.usage,
            'add_help_option': False,
            'name': name,
            'description':self.__doc__,
        } #'prog':'{}.{}'.format(get_prog(),name),

        self.name = name
        self.summary = summary
        self.parser = ConfigOptionParser(**parser_kw)

        self.tempdir_registry = None

        #Commands should add options to this option group
        optgroup_name = '{} Options'.format(self.name)
        self.cmd_opts = optparse.OptionGroup(self.parser, optgroup_name)

        #Add the general options
        gen_opts = cmdoptions.make_option_group(
            cmdoptions.general_group,
            self.parser,
        )
        self.parser.add_option_group(gen_opts)

    def parse_args(self, args):
        # type: (List[str]) -> Tuple[Any, Any]
        # factored out for testability
        return self.parser.parse_args(args)

    def main(self, args):
        #type: (List[str]_ -> int)
        try:
            #Cant get this to work properly
            #with self.main_context():
            return self._main(args)
        finally:
            logging.shutdown()

    def _main(self, args):
        options, args = self.parse_args(args)

        try:
            status = self.run(options, args)

            if isinstance(status, int):
                return status
        except CommandError as exc:
            logger.critical('%s', exc)
            logger.debug('Exception information:', exc_info=True)

            return ERROR
        except BadCommand as exc:
            logger.critical(str(exc))
            logger.debug('Exception information:', exc_info=True)

            return ERROR
        return SUCCESS
