import os
import re
import urllib.request as request
#import urllib.parse as parse

def gethtml(url):
    useragent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.58 Safari/537.36"
    headers = {"User-Agent": useragent}
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    return resp.read()

def downloadImage(src):
    try:
        name = src[src.rindex("/"):]
        image = gethtml(src)
        with open("F:/DownloadImages/"+name, "wb") as imageFile:
            imageFile.write(image)
    except Exception as e:
        print(e)
    finally:
        print(src)

url = "http://image.baidu.com/channel/info"
html = gethtml(url)
with open("c:/test.html", "wb") as testhtml:
    testhtml.write(html)
reg = re.compile("http://[^\s\(\)'\"]+\\.(?:jpg|png|jpeg)", re.I)
srcs = re.findall(reg, str(html))
for src in srcs:
    downloadImage(src)
    



