#!/usr/bin/python3
#coding=utf-8

import sys
import urllib.request

if len(sys.argv) < 2:
    print("less argument...")
    exit()

url = sys.argv[1]
if url.find("://") == -1:
    url = "http://" + url
print("connect to %s"%url);
try:
    response = urllib.request.urlopen(url)
    html = response.read()
    print(html)
except Exception as e:
    print("cannot connect to %s"%url)
    exit()
    

