
def readStore():
    laptopList=[]
    file=open("Store.txt","r")
    lines=file.readlines()
    for line in lines:
        x=line.split(',')
        laptopList.append(x)
    file.close()
    return laptopList

