#!/usr/bin/python3
#coding=utf-8

import io, sys, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

path = "."
if len(sys.argv) > 1:
    path = sys.argv[1];
if os.path.isdir(path):    
    dirs = os.listdir(path)
    for i in dirs:
        #if i[0] != "." and i[0] != "~":
        print(i)
