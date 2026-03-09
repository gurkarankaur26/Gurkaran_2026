def matmult(A,B):
    r_mat=[]
    
    row_a = len(A)
    row_b = len(B)
    col_a = len(A[0])
    col_b = len(B[0])       
    #r_mat(0,0)  = A[0][0]*B[0][0]+A[0][1]*B[1][0]+A[0][2]*B[2][0]
    if col_a != row_b:
        raise ValueError("Cannot multiply: A cols != B rows")
    for i in range(row_a):
        row =[] 
        for j in range(col_b):
            row.append(0)
            #print(row)
        r_mat.append(row)
    #print(r_mat)
    for i in range (row_a):
        for j in range(col_b):
         for k in range (row_b):
             r_mat[i][j]= r_mat[i][j]+A[i][k]*B[k][j]
    return r_mat