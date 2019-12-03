#!/bin/python3
from argparse import ArgumentParser

FLAGS = None
output_content = ""

def converter(file_content):
    output = ("```python \n" + file_content + "\n```")


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
    with open(data_input) as file_content:
        #call the function
        converter(file_content)
        print(output_content)


