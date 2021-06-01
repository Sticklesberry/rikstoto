# Rikstoto

## Packaging help (reminder)

export PYTHONPATH=$(pwd)

When pwd is the directory of this readme file.

See https://stackoverflow.com/a/54114511

## Testing

Currently have only made all tests run by being in this directory and running ```python -m unittest```.

As a simple command to achieve this, add the following to .bashrc:

```alias rikstest="cd /path/to/rikstoto-something/rikstoto-data-collector/; python3 -m unittest"```

