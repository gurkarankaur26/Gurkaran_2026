def next_number(symbols, n:str):
            base =len(symbols)
            str_n = n
            rev_n = str_n[::-1] #Reverse the number
            total_len = len(str_n)    
            next_num=''
            all_last_char=True 
            for char in rev_n:  
                if char != symbols[base-1]:
                    all_last_char=False  
                    
                index_char = symbols.find(char) 
                # if digit/char in the number is not the last symbol of the base then 
                # find the index of the char in symbols and increment it by one and get 
                # the next number
                if  char != symbols[base-1]:             
                    next_num = symbols[index_char+1]+next_num 
                    break
                else:
                    # if digit/char in the number is  the last symbol of the base then 
                    # next number will be the first symbol of the base concatenated with 
                    # the next number
                    next_num = symbols[0]+next_num
            result=''
            if all_last_char==True:
                # if all the char/digit in the number are last symbol of the base
                # then append the second symbol to the next number i.e. if BBB then 1000
                result = symbols[1]+ next_num
            else:
                # else append to next number value, the remaining char/digit of the number that 
                #  were not incremented.
                result = str_n[0:total_len - len(next_num)]+ next_num
            return(result)
            
# next_number("0123456789AB","1B")