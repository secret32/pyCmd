import time, sys

def formatTimeStamp(ts):
    lt = time.localtime(ts)
    t = time.strftime("%Y-%m-%d %H:%M:%S", lt)
    return t

ts = 0
if len(sys.argv) >= 2:
    ts = int(sys.argv[1])
else:
    ts = time.time()
print(formatTimeStamp(ts))

