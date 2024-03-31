from Invoice import invoice

def sellLaptopStore(sellLaptopList):
    customerName = input("Please write Customer's Name: ")
    try:
        laptopNumber = int(input("Please choose the number of laptop: "))
        laptopQuantity = int(input("Please enter the quantity of laptop: "))
    except ValueError:
        print("Please input integer value for number of laptops and quantity.")
        return
    
    if laptopNumber < 1 or laptopNumber > len(sellLaptopList):
        print("Invalid laptop number. Please try again.")
        return
    
    availableQuantity = int(sellLaptopList[laptopNumber-1][3]) 
    if laptopQuantity > availableQuantity:
        print("We lack that much quantity. Please try again.")
        return
    
    elif laptopQuantity <= 0:
        print("Invalid number, please try again !!")
        return
    
    sellLaptopList[laptopNumber-1][3] = str(availableQuantity - laptopQuantity)
    updateLaptopStore(sellLaptopList)
    invoice(laptopNumber, customerName, sellLaptopList, laptopQuantity)
    print("======================================================================")
    print("Congratulations, the "+sellLaptopList[laptopNumber-1][0]+" laptop(s) have been sold successfully!")
    print("Please check your invoice.")
    print("======================================================================")
    
def updateLaptopStore(updateLaptopList):
    with open("Store.txt","w") as update:
        for i in range(len(updateLaptopList)):
            for j in range(6):
                if j == 5:
                    update.write(str(updateLaptopList[i][j]))
                else:
                    update.write(str(updateLaptopList[i][j]) + ",")              
        update.close()
