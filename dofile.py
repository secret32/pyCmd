#!/usr/bin/python3

import sys, os

def deleteBlankLine(filepath):
        if os.path.isdir(filepath):
                print("Not support for directory.")
                return -1
        bakpath = filepath + ".bak"
        f = open(filepath, "r")
        bak = open(bakpath, "w")
        for line in f.readlines():
                if len(line) > 1:
                        bak.write(line)
        bak.close()
        f.close()
        os.remove(filepath)
        os.rename(bakpath, filepath)

def deleteEnter(filepath):
        print("hahaha")

def usage():
        print("usage: dofile <-option> <file>")
        print("options:")
        print("\tdbl \tdelete blank line of the file")

if len(sys.argv) < 3:
        usage()
        exit()

dics = {"dbl" : deleteBlankLine, "de" : deleteEnter}
	
filepath = sys.argv[2]

if not os.path.isabs(filepath):
	filepath = os.path.getcwd() + filepath
	
if not os.path.isfile(filepath):
	print("the param is not a file")
	exit()

option = sys.argv[1]
try:
        dics[option](filepath)
except KeyError as e:
        print("the useless option: [%s]"%option)
	
