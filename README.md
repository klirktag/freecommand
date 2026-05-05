# freecommand

Find short, two-letter command names that don't collide with anything already on your `$PATH`.

## What it does

`freecommad.py` iterates over every two-letter lowercase combination from `aa` to `zz` (676 in total) and prints the ones that are **not** a prefix of any executable found on your `$PATH`.

The output is a list of short command names that are "free" — safe to use as new aliases or script names without shadowing or colliding with an existing command.

## Usage

```bash
python3 freecommad.py
```

Or, since the script is executable:

```bash
./freecommad.py
```

## Example

```bash
$ ./freecommad.py | head
bq
bv
ck
...
```

Each printed combination is a candidate for a new alias, function, or script name.

## How it works

1. Reads the `PATH` environment variable and splits it into directories.
2. Collects the names of all entries in those directories into a set.
3. For each two-letter combination `aa`..`zz`, prints it if no collected command starts with that prefix.
