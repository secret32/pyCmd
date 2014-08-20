import sys, os

path = os.getcwd()
if len(sys.argv) > 1:
    arg1 = sys.argv[1]
    if arg1.endswith(":"):
        path = arg1
    elif not os.path.isabs(arg1):
        path += "\\%s"%arg1
    else:
        path = arg1
if not os.path.exists(path):
    print("specific directory or file is not exists")
    exit()
if os.path.isdir(path):
    os.system("explorer %s"%path)
else:
    os.system(path)
