
#Start: Pyhton Function for single and multiple digit Addition, Subtraction and Multiplication***
def base4_calc(operation, num1,num2):
    res=0
    if(operation=='+'):
        res =num1+num2
    elif(operation == '-'):
        if(num1 > num2):
            res= num1 - num2
        else:
            res= num2 -num1
    elif(operation == '*'):
        res= num1 * num2
    quotient=9
    remainder =9
    base4_res=''
    loop = True
    #print(quotient)
    while(loop):       
        quotient  = int(res/4)       
        remainder = res%4
        res =quotient
        #print(remainder)
        if(base4_res != ''):
         base4_res = str(remainder)+base4_res
         #print(base4_res)
        else:
         base4_res = str(remainder)
         #print(base4_res)
        if(quotient == 0):
            loop=False
        
    if(operation =='+'):
        #print(base4_res)
        print(f"{num1}+{num2}={base4_res}")
    elif(operation == '-'):
        if(num1 > num2):
            print(f"{num1}-{num2}={base4_res}")
        else:
            print(f"{num2}-{num1}={base4_res}")
    elif(operation == '*'):
         print(f"{num1}*{num2}={base4_res}")
         
#End: Pyhton Function for single and multiple digit Addition, Subtraction and Multiplication***

#Start: Python Function to convert anumber from a specified base to decimal***
def convert_num_todecimal(base,num):
    ln= int(len(str(num)))
    res=0
    str_num=str(num)
    for i in str_num:
        if(ln<0):
         break
        res=res+ int(i)*(base**(ln-1))
        ln=ln-1
    print(res)
#End: Python Function to convert anumber from a specified base to decimal***

#Start: Python function to find to total numbers for specified base and digit***
def total_nos_for_base_digit(b,d):
      #res = (b-1)*((b**(d-1)))
      res = b**d
      return res
#End: Python function to find to total numbers for specified base and digit***

#Start: Python function to calculate log of a number upto 1000.***
def calbase10log_1000(n):
    if n <1000:
     #print(n)
     pow=3
     while(pow>0):
        #print('power',pow)
        res=int(10**pow)
        #print(res)
        if res==n:
         break
        else:
         pow = pow -.001
        
     print(f"Log10({n}) is {pow}")    
    else:
     print('No. should not be greater than 1000')

#End: Python function to calculate log of a number upto 1000.***

#Start: Python function to calculate log of a number upto 10000.***
def calbase10log(n):
    if n <10000:
     #print(n)
     pow=4
     while(pow>0):
        #print('power',pow)
        res=int(10**pow)
        #print(res)
        if res==n:
         break
        else:
         pow = pow -.00001
        
     print(f"Log10({n}) is {pow}")    
    else:
     print('No. should not be greater than 10000')  

#End Python function to calculate log of a number upto 1000.***

#Start: Python function to calculate squareroot of a number ***
def calsquareroot(n:int):
    sqrt:float= n**(1/2)
    print(f"Square root of {n} is {sqrt}")
# End: Python function to calculate squareroot of a number ***



#Command to execute
#1. Type Python
#2. from CommonFunction import calsquareroot
#3. calsquareroot(25)
        