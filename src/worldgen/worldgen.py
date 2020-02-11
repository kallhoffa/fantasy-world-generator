#!/usr/bin/env python3
import sys
from src.worldgen import commands as commands



def main (args=None):
    if args is None:
        args = sys.argv

    if args[1] == "create":
        commands.create()


