#!/bin/python3
from argparse import ArgumentParser

FLAGS = None

def converter(file_contents):
    print("```python \n" + file_contents + "\n```")


if __name__ == '__main__':
    # read input flag
    parser = ArgumentParser()
    parser.add_argument(
        '-f',
        type=str,
        help='File'
    )
    FLAGS, unparsed = parser.parse_known_args()
    data_input = (str(FLAGS.f))

    # load file
    with open(data_input) as fr:
        file_contents = fr.read()

    # call the function
    converter(file_contents)

