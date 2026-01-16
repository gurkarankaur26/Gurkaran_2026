import  multiply
def tables(symbols):
    matrix =[]
    base = len(symbols)
    row=[]
    for j in range(base):
        row.append(symbols[j])
    matrix.append(row)
    for i in range(base):
        row=[]
        if i>0:
            row.append(symbols[i])
            for j in range(base-1):
                row.append(symbols[i])
            matrix.append(row)     
    for k in range(base):    
        if k+1>=base:break    
        for j in range(base):
            if k+1>=base:break
            if j==0:continue
            num1 = matrix[j][0]
            num2= matrix[0][k+1]
            # print(j,k)    
            matrix[j][k+1]=multiply.multiply_two_numbers(symbols,str(num1),str(num2))
    print('*'*60) 
    print(f'{" ":20}Base '+str(base)+' Tables from 2 to '+symbols[base-1])  
    print('*'*60) 
    for row in matrix[1:]:        
        for value in row[2:]:
            print(f"{value:5}", end=" ")
        if matrix.index(row)==1:
            print() 
            print('*'*60) 
        print()

 
 
