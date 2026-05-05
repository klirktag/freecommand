#!/usr/bin/env python3
"""
Print every two-letter lowercase combination (aa..zz) that is NOT a prefix
of any executable name found on the user's $PATH. The output is a list of
short command names that are "free" — safe to use as new aliases or script
names without shadowing or colliding with an existing command.
"""
import os
import string

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

for first in string.ascii_lowercase:
    for second in string.ascii_lowercase:
        to_test = first + second
        if not any(cmd.startswith(to_test) for cmd in commands):
            print(to_test)

