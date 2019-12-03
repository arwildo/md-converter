#!/bin/python3

# SOLVED: 1, 2, 3, 4, 5

class TwoStr(object):
    def __init__(self):
        self.usrInput = ""

    def getString(self):
        self.usrInput = input()

    def printString(self):
        print((self.usrInput).upper())


tc = TwoStr()
tc.getString()
tc.printString()
