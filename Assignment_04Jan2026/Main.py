
import CommonFunction
menu ="""         Choose an Option\n
          1. Add two numbers in Base4. \n
          2. Subtract two numbers in Base4. \n
          3. Multiply two numbers in Base4.\n
          4. Log10 of a number. \n
          5. Square Root of a number.\n
          6. Base10 of number in a specified base. \n
          7. Find total number that can be generated in specified base and digits.\n
          8. Exit.\n"""

showmenu = True
while (showmenu):
    print('\n\n')
    print(menu)
    option = input("Enter any number from 1 to 8: ")
    if option.isdigit() and int(option) > 0:
    
        if int(option) >= 1 and int(option) <= 3:
            num1 = input("Enter number 1:")
            num2 = input("Enter number 2:")
            if num1.isdigit() and int(num1) > 0 and num1.isdigit() and int(num1) > 0:
                 #print("You selected Calculator")
                 if int(option) == 1: #Add
                    CommonFunction.base4_calc('+', int(num1),int(num2))
                 if int(option) == 2: #Subtraction
                     CommonFunction.base4_calc('-', int(num1),int(num2))
                 if int(option) == 3: #Multiplication
                    CommonFunction.base4_calc('*', int(num1),int(num2))
            else:
                print("Invalid input")
            res= input("Do you want to go to main menu or exit?(y/n): ")
            if res.upper() == 'Y':
                continue
            else:
                showmenu=False
                break
        elif int(option) >= 4 and int(option) <= 5:
            num1 = input("Enter a number :")
            if num1.isdigit() and int(num1) > 0:
                if int(option) == 4:
                    #print("You selected Log10")
                    CommonFunction.calbase10log(int(num1))
                elif int(option) == 5:
                    CommonFunction.calsquareroot(int(num1))
            else:
                print("Invalid input") 
            res= input("Do you want to go to main menu or exit?(y/n): ")
            if res.upper() == 'Y':
                continue
            else:
                showmenu=False
                break
        elif int(option)==6:
            base= input("Enter base:")
            num=  input("Enter number:")
            if base.isdigit() and int(base) > 0 and num.isdigit() and int(num) > 0:        
                CommonFunction.convert_num_todecimal(int(base),int(num))
            else:
                print("Invalid input")
            res= input("Do you want to go to main menu or exit?(y/n): ")
            if res.upper() == 'Y':
                continue
            else:
                showmenu=False
                break
        elif int(option)==7:
            base= input("Enter base:")
            d=  input("Enter no. of digits in the number:")
            if base.isdigit() and int(base) > 0 and d.isdigit() and int(d) > 0:        
                CommonFunction.total_nos_for_base_digit(int(base),int(d))
            else:
                print("Invalid input")
            res= input("Do you want to go to main menu or exit?(y/n): ")
            if res.upper() == 'Y':
                continue
            else:
                showmenu=False
                break
        elif int(option)==8:
             showmenu=False
             break
    else:
        print("Wrong Option")
        res= input("Do you want to go to main menu or exit?(y/n): ")
        if res.upper() == 'Y':
                continue
        else:
                showmenu=False
                break
