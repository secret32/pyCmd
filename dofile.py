#!/usr/bin/python3

import sys, os

if len(sys.argv) < 2:
	print("there is no input param")
	exit()

filepath = sys.argv[1]

if not os.path.isabs(filepath):
	filepath = os.path.getcwd() + filepath
	
if not os.path.isfile(filepath):
	print("the param is not a file")
	exit()
	
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
