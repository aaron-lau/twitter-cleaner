# -*- coding: utf-8 -*-
import click


@click.group()
def cli():
    pass


@cli.command(help="This script shows reads your local Twitter data and displays your historical content in the Command Line")
@click.option("--path", required=True, help="Absolute path to where your downloaded Twitter data is")
def display_tweets(path):
    print (path)

if __name__ == "__main__":
    cli()
