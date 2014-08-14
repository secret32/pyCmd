#!/usr/bin/python3
#coding=utf-8

import sys, os

path = "."
if len(sys.argv) > 1:
    path = sys.argv[1];
dirs = os.listdir(path)
for i in dirs:
    print(i)
