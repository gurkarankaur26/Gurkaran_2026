import  add
import  numtodecimal
def multiply_two_numbers(symbols,num1:str,num2:str):
     res=0
     n1=num1
     ctr = int(numtodecimal.convert_num_todecimal(symbols,num2))
     #print('ctr:',ctr)
     for i in range(ctr-1):
          res= add.add_two_numbers(symbols,num1,n1) # 2+2+2+2+2+2          
          num1=res
          #print('i:'+str(i),'res:',str(res))
     return(res)
     
    