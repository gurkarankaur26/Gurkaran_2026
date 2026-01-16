
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
def convert_num_todecimal(symbols,num):
    base =len(symbols)
    ln= len(num)
    res=0
    for i in num:
        if(ln<0):
         break
        val:int=0
        if str(i).isdigit()==True:
            val =int(i)
        else:
            val =symbols.find(i)
        print(type(val),type(ln))
        res=res+ val*(base**(ln-1))
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
# def calbase10log_1000(n):
#     if n <1000:
#      #print(n)
#      pow=3
#      while(pow>0):
#         #print('power',pow)
#         res=int(10**pow)
#         #print(res)
#         if res==n:
#          break
#         else:
#          pow = pow -.001
        
#      print(f"Log10({n}) is {pow}")    
#     else:
#      print('No. should not be greater than 1000')

#End: Python function to calculate log of a number upto 1000.***

#Start: Python function to calculate log of a number upto 10000.***
# def calbase10log_old(n):
#     if n <10000:
#      #print(n)
#      pow=4
#      while(pow>0):
#         #print('power',pow)
#         res=int(10**pow)
#         #print(res)
#         if res==n:
#          break
#         else:
#          pow = pow -.00001
        
#      print(f"Log10({n}) is {pow}")    
#     else:
#      print('No. should not be greater than 10000')  

#End Python function to calculate log of a number upto 10000.***

#Start Python function to calculate log10 of a number
def calbase10log(n):
    p = 0
    ctn = True
    step = 0.1

    while ctn:
        if 10 ** (p + step) <= n:
            p = p + step
        else:
            step = step / 10
            if step < 1e-6:
                ctn = False

    print(f"Log10({n}) is  {p:.6f}")   


#End Python function to calculate log10 of a number


#Start: Python function to calculate squareroot of a number ***
def calsquareroot(n:int):
    sqrt:float= n**(1/2)
    print(f"Square root of {n} is {sqrt}")
# End: Python function to calculate squareroot of a number ***

#Start: Python function to calculate square root of number by guessing the range
def calsquareroot_guess(n):
    #80
    lb = 1
    ub = 1    
    min_lb_diff =n
    max_ub_diff =n+1
    
    # find the lower bound
    while min_lb_diff > 0:
        lb = lb+1
        sq = lb*lb
        lb_diff = n-sq          
        if lb_diff < min_lb_diff:
            min_lb_diff = lb_diff  
        if min_lb_diff <0:lb=lb-1            
    #print(lb)
    
    #set upper bound to lower bound + 1
    ub =lb +1
    cont=True
    while cont:        
        sq = ub*ub  
        #print(sq)
        ub_diff = sq-n   
        if(ub_diff < max_ub_diff ):
            cont=False
            break
        else:
            ub = ub+1
    #print(ub)   
    # Logic to calculate the square root 
    guess = 0
    cnt=True
    comp_val=round(n**0.5,6)
    while cnt:
    #print(guess)
        guess = (lb + ub)/2
        #print(guess)
        if comp_val - round(guess,6) == 0:
            cnt=False 
        elif guess*guess < n :
            lb = guess
        else:
            ub = guess 
    sqrt=round(guess,6)       
    print(f"Square root of {n} is {sqrt}")


#End: Python function to calculate square root of number by guessing the range



#Command to execute
#1. Type Python
#2. from CommonFunction import calsquareroot
#3. calsquareroot(25)
        