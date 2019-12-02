#!/bin/python3

def converter(file_contents):
    return("```python \n" + file_contents + "\n```")


if __name__ == '__main__':
    # file dir
    data_input = ("files/data_plot.py")

    # load file
    with open(data_input) as f:
        file_contents = f.read()

    # convert into md python syntax
    converted = converter(file_contents)
    print(converted)

