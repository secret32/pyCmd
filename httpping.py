import sys, urllib.request

def urlPing():
    url = ""
    if len(sys.argv) < 2:
        url = "http://www.baidu.com"
    else:
        url = sys.argv[1]

    if url[:7] != "http://" and url[:8] != "https://":
        url = "http://" + url
    try:
        response = urllib.request.urlopen(url)
        if response.status == 200:
            print("success")
        else:
            print("failed, status=%d"%response.status)
    except TimeoutError as e:
        print("timeout")

if __name__ == '__main__':
    urlPing()


    




