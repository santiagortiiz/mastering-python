"""Running instructions.

py services/conversion.py '{"a": "A"}'
"""
import click


@click.command()
@click.argument("file_metadata")
def convert(file_metadata):
    print("METADATA:")
    print(file_metadata)


if __name__ == "__main__":
    convert()
