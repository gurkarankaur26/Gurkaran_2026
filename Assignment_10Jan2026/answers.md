1. Choose you base between 3 to 13
Done in Assignment_04Jan2026

2. Choose your symbols
Done in Assignment_04Jan2026

3. Write upto 3 digits in your base
Done in Assignment_04Jan2026

4. Add/subtract single digit in your base
Done in Assignment_04Jan2026

5. Base64
0-9, A-Z, a-z, =, +

6. a. Write strategy to print next number in a number system. A system is a sequence of symbols
        next_number(symbols="0123456789AB", "1") -> 2
        next_number(symbols="0123456789AB", "B") -> 10
        next_number(symbols="0123456789AB", "111") -> 112
        next_number(symbols="0123456789AB", "BB") -> 100
        next_number(symbols="0123456789AB", "ABAB") -> ABB0

        def next_number(symbols, n):
            base =len(symbols)
            str_n = str(n)
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
            print(result)
            

        
    b. Print first n digits in symbols="0123456789AB"

      ### Start: Function to print n digit for the given base

      def print_ndigit_no_in_base(symbols,n):
            base = len(symbols)
            total_digit = n   
            total_num = base ** total_digit    
            num = ""
            str_loop=''
            symbols_str = ''
            indent=""
            for n in range(total_digit):   
                loop_variable = "v_"+str(n)
                symbols_str = symbols_str + ' + symbols['+loop_variable+']' 
                str_loop = str_loop+ indent+ 'for '+loop_variable+' in range(base):\n' 
                indent+="\t"
                if n == total_digit-1:
                    str_loop = str_loop+  indent+'num= num '+symbols_str+ '+" "\n'
                    indent_len =len(indent)
                    str_indent=indent
                    for j in range(total_digit):
                        if j>0:
                            str_loop = "\n"+str_loop + indent[0:indent_len-j] + 'num =num +"\\n"\n'
                    str_loop= "\n"+str_loop+ indent[0:indent_len-total_digit]+'print(num," ")'

            #print(str_loop)
            exec(str_loop)
       ### End: Function to print n digit for the given base


7. Add two numbers at least 5 pairs.
Done in Assignment_04Jan2026

8. Write an strategy to add two numbers of multiple digits in your base.
   Code TBS

Prompt: 
    Write an code to add two numbers of multiple digits in any base represented by symbols
    add_two_numbers(symbols="0123456789AB", "11", "1B") -> "30"
    add_two_numbers(symbols="0123456789AB", "1119", "BB") -> "1218"

add_two_numbers(symbols="0123456789AB", "11", "1B") -> "30"
add_two_numbers(symbols="0123456789AB", "1119", "BB") -> "1218"

# Base4
add_two_numbers(symbols="0123", "11", "12") -> "23"
add_two_numbers(symbols="0123", "11", "33") -> "110"

9. Subtract two numbers at least 5 pairs.
Done in Assignment_04Jan2026

10. Multiplication
Done in Assignment_04Jan2026

11. Write code to prepare the tables as array of base * base - 2D list containing your table.
base 7 - 0*0 to 6*6 (49)
    TBS

12. Write code to multiply numbers, you can use the tables and add_two_numbers()
    TBS

13. Write code to fiind log of a number

   ***Start: Python function to calculate log of a number upto 10000.***

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

        print(f"Log10({n}) is {p:.6f}")  


    ***End: Python function to calculate log of a number.***

   ***Function Call to calculate log10 of a number.***
    function call : calbase10log(456) 
    output: Log10(456) is 2.658964

    function call : calbase10log(231) 
    output: Log10(231) is 2.363611
    ***Function Call to calculate log10 of a number.***

14. Write code to find square root of number by guessing logic.

    *** Start: Function to calculate square root of number by guessing the range***

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

   *** End: Function to calculate square root of number by guessing the range***

