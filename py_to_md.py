#!/bin/python3
import pandas as pd

def converter(markdown):
    print(markdown)


if __name__ == '__main__':
    markdown = pd.read_csv('files/data_plot.py')
    converter(markdown)
