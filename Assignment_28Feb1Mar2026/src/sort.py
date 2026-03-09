def sort_list(num):
    len_n = len(num)
    for i in range(len_n):
        for  j in range(len_n-1):
            if num[j] > num[j+1]:
                temp = num[j+1]
                num[j+1] = num[j]
                num[j] =temp
    return num
                
    
                
#sort_list([5,45,6,8,3,67,2])