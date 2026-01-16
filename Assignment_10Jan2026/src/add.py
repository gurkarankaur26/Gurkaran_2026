import next_number
import numtodecimal
def add_two_numbers(symbols,num1:str,num2:str): #1119 BB
    result=''
    n2=num1
    ctr = int(numtodecimal.convert_num_todecimal(symbols,num2))
    for i in range(ctr):
        result= next_number.next_number(symbols,n2)
        n2=result
    return(result)