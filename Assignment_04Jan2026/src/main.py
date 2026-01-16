
import commonfunction
menu ="""         Choose an Option\n         
          1. Log10 of a number. \n
          2. Square Root of a number.\n
          3. Base10 of number in a specified base. \n
          4. Find total number that can be generated in specified base and digits.\n
          5. Exit.\n"""
showmenu = True
while (showmenu):
    print('\n\n')
    print(menu)
    option = input("Enter any number from 1 to 5: ")
    if option.isdigit() and int(option) > 0:       
        if int(option) >= 1 and int(option) <= 2:
            num1 = input("Enter a number :")
            if num1.isdigit() and int(num1) > 0:
                if int(option) == 1:
                    #print("You selected Log10")
                    commonfunction.calbase10log(int(num1))
                elif int(option) == 2:
                    commonfunction.calsquareroot_guess(int(num1))
            else:
                print("Invalid input") 
            res= input("Do you want to exit?(y/n): ")
            if res.upper() == 'N':
                continue
            else:
                showmenu=False
                break
        elif int(option)==3:
            base= input("Enter base symbols:")
            num=  input("Enter number:")
            if num.isdigit() and int(num) > 0:        
                commonfunction.convert_num_todecimal(int(base),int(num))
            else:
                print("Invalid input")
            res= input("Do you want to exit?(y/n): ")
            if res.upper() == 'N':
                continue
            else:
                showmenu=False
                break
        elif int(option)==4:
            base= input("Enter base:")
            d=  input("Enter no. of digits in the number:")
            if base.isdigit() and int(base) > 0 and d.isdigit() and int(d) > 0:        
                commonfunction.total_nos_for_base_digit(int(base),int(d))
            else:
                print("Invalid input")
            res= input("Do you want to exit?(y/n): ")
            if res.upper() == 'N':
                continue
            else:
                showmenu=False
                break
        elif int(option)==5:
             showmenu=False
             break
    else:
        print("Wrong Option")
        res= input("Do you want exit?(y/n): ")
        if res.upper() == 'N':
                continue
        else:
                showmenu=False
                break
