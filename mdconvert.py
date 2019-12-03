#!/bin/python3
from argparse import ArgumentParser

FLAGS = None
SAVED_DIR = "C:\My App\converted-files\/"

def converter(file_content):
    output_content = ""
    output_content += ("```python \n" + file_content + "\n```")
    return output_content


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
        file_content = fr.read()

    # call the function
    converted = converter(file_content)

    # save the file
    # TODO: add regex to filter get_name for win tab
    get_name = data_input
    te = open(SAVED_DIR + data_input +  ".md", "x")
    te.write(converted)

    te.close()

