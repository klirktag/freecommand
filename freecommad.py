#!/usr/bin/env python3
"""
Print every N-letter lowercase combination that is NOT a prefix of any
executable name found on the user's $PATH. The output is a list of short
command names that are "free" — safe to use as new aliases or script
names without shadowing or colliding with an existing command.

Usage: freecommad.py [length]   (length defaults to 2)
"""
import itertools
import os
import string
import sys

length = 2
if len(sys.argv) > 1:
    try:
        length = int(sys.argv[1])
    except ValueError:
        sys.exit(f"error: length must be an integer, got {sys.argv[1]!r}")
    if length < 1:
        sys.exit("error: length must be at least 1")

path_dirs = os.environ.get("PATH", "").split(os.pathsep)

commands = set()
for d in path_dirs:
    if not d or not os.path.isdir(d):
        continue
    try:
        for entry in os.listdir(d):
            commands.add(entry)
    except OSError:
        continue

for combo in itertools.product(string.ascii_lowercase, repeat=length):
    to_test = "".join(combo)
    if not any(cmd.startswith(to_test) for cmd in commands):
        print(to_test)
