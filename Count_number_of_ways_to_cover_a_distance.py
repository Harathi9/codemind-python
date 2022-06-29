def PrintCountRec(dist):
    if dist<0:
        return 0
    if dist==0:
        return 1
    return(PrintCountRec(dist-1)+PrintCountRec(dist-2)+PrintCountRec(dist-3))
dist=int(input())
print(PrintCountRec(dist))