from contextlib import contextmanager

class CommandContextMixIn(object):
    def __init__(self):
        # type: () -> None
        super(CommandContextMixIn, self).__init__()
        self._in_main_context = False
        # self._main_context = ExitStack()
        #  Used to exit if not in main context, dont need for now

    @contextmanager
    def main_context(self):
        #type: () -> Iterator[None]
        assert not self._in_main_context

        self._in_main_context = True