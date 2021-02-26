#!/usr/bin/env python
import click

@click.command()
@click.option("--height")
def hello(height):
    h = int(height)
    for i in range(0, h):
        for _ in range(0, i + 1):
            print("* ",end="")
        print("\r")

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()