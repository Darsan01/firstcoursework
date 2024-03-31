import datetime
from Sell import updateLaptopStore

def addLaptopStore(adddLaptopListt):
    laptopNumber=int(input("Enter number of laptop: \t"))
    laptopStore=int(input("Enter quantity of laptop : \t"))
    shippingCompany=input("Enter shipping company: \t")
    shippingCost=input("Enter total cost of shipping: \t")
    for i in range(len(adddLaptopListt)):
        if(i+1==laptopNumber):
            a=int(adddLaptopListt[i][3])
            a += laptopStore
            adddLaptopListt[i][3]=a
            updateLaptopStore(adddLaptopListt)
            addLaptopStoreDetails(adddLaptopListt,laptopNumber,laptopStore,shippingCompany,shippingCost)
            print("             =======================================================================")
            print("                     ******      "+adddLaptopListt[i][0]+" is added Successfully!   ******")
            print("             ========================================================================")
            
            
def addLaptopStoreDetails(addlaptopList,laptopNumber,stockAmount,laptopShippingCompany,laptopShippingCost):
    k=datetime.datetime.now()
    for i in range(len(addlaptopList)):
        if(i+1==laptopNumber):
            laptopName=addlaptopList[i][0]
            laptopBrand=addlaptopList[i][1]
            laptopprice=addlaptopList[i][2].replace('$','')
            laptopQuantity=addlaptopList[i][3]
            laptopprocessor=addlaptopList[i][4]
            vat = float(laptopprice) * (13/100)
            laptopVat = float(laptopprice) + vat
            laptopGraphics=addlaptopList[i][5]

    f="add"+laptopName+".txt"
    f=open(f,"w")
    f.write("\n")
    f.write('''
        ==============================================================================================
                            ********        STOCK ADDED       ********
        ==============================================================================================''')

    f.write("\n"+"                     laptop Name          : \t\t"+laptopName)
    f.write("\n"+"                     laptop Brand         : \t\t"+laptopBrand)
    f.write("\n"+"                     laptop Price         : \t\t"+laptopprice)
    f.write("\n"+"                     laptop Quantity      : \t\t"+str(laptopQuantity))
    f.write("\n"+"                     laptop processor     : \t\t"+laptopprocessor)
    f.write("\n"+"                     laptop Graphics      : \t\t"+laptopGraphics)
    f.write("\n"+"                     Store added          : \t\t"+str(stockAmount))
    f.write("\n"+"                     Shipping Company     : \t\t"+laptopShippingCompany)
    f.write("\n"+"                     Shipping Cost        : \t\t$"+laptopShippingCost)
    f.write("\n"+"                     Total Cost with VAT  :\t\t $ " +str(laptopVat))
    f.write("\n"+"                     Delivery Date        : \t\t"+str(k.year)+" - "+str(k.month)+" - "+str(k.day))
    f.write("\n"+"                     Delivery Time        : \t\t"+str(k.hour)+" : "+str(k.minute))
    f.write("\n"+"      =================================================================================================")
    f.close()
