import datetime
import os.path
a=datetime.datetime.now()
def invoice(laptopNumber,customerName,invoiceLaptopList,laptopQuantity):
    for i in range(len(invoiceLaptopList)):
        if(i+1==laptopNumber):
            laptopName=invoiceLaptopList[i][0]
            laptopBrand=invoiceLaptopList[i][1]
            laptopPrice=invoiceLaptopList[i][2]
            laptopProcessor=invoiceLaptopList[i][4]
            GraphicsCard=invoiceLaptopList[i][5]
            
    p=laptopPrice.split('$')
    price=p[1]
    
    if not os.path.exists(customerName+".txt"):
        f=customerName+".txt"
        f=open(f,"w")
        f.write("\n"+"      =============================================================================")
        f.write("\n"+"                                              Date:"+str(a.year)+" / "+str(a.month)+" / "+str(a.day))
        f.write("\n"+"                                              PAN No. 21389423409")
        f.write("\n"+"                                              ------------------------------------")
        f.write("\n"+"         LAPTOP RENTAL SHOP")
        f.write("\n"+"         Dulari, Morang  ")
        f.write("\n"+"      -----------------------------")
        f.write("\n"+"                                                  Contact No.: 024411071")
        f.write("\n"+"      ==============================================================================")
        f.write("\n"+"              Customer's Name      :\t\t "+ str(customerName))
        f.write("\n"+"              Laptop Name          :\t\t "+laptopName)
        f.write("\n"+"              Laptop Brand         :\t\t"+laptopBrand)
        f.write("\n"+"              Price                :\t\t"+laptopPrice)
        f.write("\n"+"              Quantity             :\t\t "+ str(laptopQuantity))
        f.write("\n"+"              Processor            :\t\t"+laptopProcessor)
        f.write("\n"+"              GraphicsCard         :\t\t"+GraphicsCard)
        f.write("\n"+"      __________________________________________________________________________")
        f.write("\n"+"              Total Price        :\t\t  $"+str(int(price)*laptopQuantity))
        f.write("\n"+"      ==============================================================================")
        f.write("\n"+"                     ***********   CONGRATULATION    ***********")
        f.write("\n"+"                         ***     Please Check Your Invoice   ***  ")
        f.write("\n"+"                     *******      Please Visit Again    ******")
        f.write("\n"+"      ==============================================================================="+"\n"+"\n")    
        f.close()  
    else:
        f=customerName+".txt"
        f=open(f,"a")
        f.write("\n"+"\n"+"\n"+"------------------------------------------------------------------------------------------------------")
        f.write("\n"+"      =================================================================================")
        f.write("\n"+"                                              Date:"+str(a.year)+" / "+str(a.month)+" / "+str(a.day))
        f.write("\n"+"                                              PAN No. 21389423409")
        f.write("\n"+"                                              -----------------------------------------")
        f.write("\n"+"      LAPTOP RENTAL SHOP")
        f.write("\n"+"      Dulari,Morang   ")
        
        f.write("\n"+"                                                  Contact No.: 024411071")
        f.write("\n"+"      =================================================================================")
        f.write("\n"+"              Customer's Name       :\t\t "+str(customerName))
        f.write("\n"+"              Laptop Name           :\t\t "+laptopName)
        f.write("\n"+"              Laptop Brand          :\t\t"+laptopBrand)
        f.write("\n"+"              Price                 :\t\t"+laptopPrice)
        f.write("\n"+"              Quantity              :\t\t "+str(laptopQuantity))
        f.write("\n"+"              processor             :\t\t"+laptopProcessor)
        f.write("\n"+"              GraphicsCard          :\t\t"+GraphicsCard)
        f.write("\n"+"      __________________________________________________________________________")
        f.write("\n"+"              Total Price         :\t\t  $"+str(int(price)*laptopQuantity))
        f.write("\n"+"      =================================================================================")
        f.write("\n"+"                     ***********   CONGRATULATION    ***********")
        f.write("\n"+"                         ***     Please Check Your Invoice   ***  ")
        f.write("\n"+"                     *******      Please Visit Again    ******")
        f.write("\n"+"      ================================================================================="+"\n"+"\n")     
        f.close()

