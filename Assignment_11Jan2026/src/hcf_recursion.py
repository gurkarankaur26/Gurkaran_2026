def compute_hcf(a, b):
     if(str(a).isdigit()==False or  str(b).isdigit()==False):
        print('Provide postive numeric values to find HCF')
        return      
     if a <0 or b < 0:
        print('Provide postive numeric values to find HCF')
        return    
     if b==0:
        return a
     remainder = a%b
     a=b
     b=remainder
     return compute_hcf(a,b)