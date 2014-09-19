def dividePage (pageNo, pageCount, item = 10):
    if pageCount <= item:
            first = 1
            last = pageCount
    elif pageNo < item // 2:
            first = 1
            last = item
    elif pageCount - pageNo > item // 2:
            first = pageNo - (item // 2 - 2)
            last = pageNo + (item // 2 + 1)
    else:
            first = pageCount - (item - 1)
            last = pageCount
    for i in range(first, last + 1):
        print(i, end=' ')
    print("")

for i in range(1, 11):
    print("***start pageNo="+str(i))
    dividePage(i, 10)
    print("***end pageNo="+str(i))
