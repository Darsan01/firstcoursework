
def displayStore(list):
    print('''
                            ========================================
                                ||WELCOME TO LAPTOP RENTAL SHOP|| 
                            ========================================       ''')
    for i in range(len(list)):
        print((str(i+1))+")"+"  "+"Laptop Name:"+list[i][0]+"   "+ "Laptop Brand:"+list[i][1]+"   "+ "Laptop price:"
        +list[i][2]+"   "+" Quantity:"+list[i][3]+"   "+" Processor:"+list[i][4]+"  "+ "Graphics:"+list[i][5])
    