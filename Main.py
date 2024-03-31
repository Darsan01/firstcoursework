from Display import displayStore
import Sell
from Read import readStore
import Add

def selectOptions():

    try:
        check=True
        while check:
            print('''
                            ====================================================
                                    ||WELCOME TO LAPTOP RENTAL SHOP||                              
                            ====================================================
                            _____________________________________________________
                            _____________________________________________________

                                        Press 1 : Display available laptops 
                                        Press 2 : Sell a laptops
                                        Press 3 : Add laptops 
                                        Press 4 : Exit
                            ____________________________________________________
                            ____________________________________________________

                                    ''')
            selectOption = input('''Please select the number between 1 to 4 : \t''')
            if selectOption == "1":
                displayStore(readStore())
                print(''' 
                        ___________________________________________
                                    Press 1: For selling laptops
                                    Press 0: Exit
                        ______________________________________________''')
                ask=input( "Please enter value:\t ")
                
                if ask=="1":
                    Sell.sellLaptopStore(readStore())
                elif ask=="0":
                    print('''                   ******* ----  Thank you for visiting ---- ********
                        -------- Please visit again---------       ''')
                else:
                    print("Please enter only 0 or 1.")

                
                
            elif selectOption == "2":
                Sell.sellLaptopStore(readStore())
                
            elif selectOption=="3":
                Add.addLaptopStore(readStore())
                

            elif selectOption == "4":
                check=False
                print('''
                      * * * * * * * * * *Thank you for visiting * * * * * * * * * *
                                *********  Please vist again   ***********
                        ''')
                

            else:
                print(''''
                      **** **** **** Please enter the valid input **** **** ****
                        ''')

    except ValueError:
        print("Error: Please make a valid choice from 1 to 4.")
        
selectOptions()