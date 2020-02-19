#!/usr/bin/env python3
import sys
from worldgen.commands import create


def main (args=None):
    if args is None:
        args = sys.argv

    if args[1] == "create":
        create()


