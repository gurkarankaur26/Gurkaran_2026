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
        res=res+ val*(base**(ln-1))
        ln=ln-1
    return(res)