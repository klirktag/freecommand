# freecommand

Find short, two-letter command names that don't collide with anything already on your `$PATH`.

## What it does

`freecommad.py` iterates over every N-letter lowercase combination and prints the ones that are **not** a prefix of any executable found on your `$PATH`. The default length is 2 (so it checks `aa`..`zz`, 676 combinations in total).

The output is a list of short command names that are "free" — safe to use as new aliases or script names without shadowing or colliding with an existing command.

## Usage

```bash
./freecommad.py           # default: 2-letter combinations
./freecommad.py 3         # 3-letter combinations (aaa..zzz)
./freecommad.py 4         # 4-letter combinations
```

Or via the interpreter:

```bash
python3 freecommad.py [length]
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
3. For each N-letter combination (where N defaults to 2 or comes from the command-line argument), prints it if no collected command starts with that prefix.
