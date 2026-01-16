def print_ndigit_no_in_base(symbols="0123456789AB",n=3):
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