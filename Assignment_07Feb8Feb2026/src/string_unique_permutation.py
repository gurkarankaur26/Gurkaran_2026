

'''Write a function to print all the permutations of a string containing uinque letters
example input: pr output: pr rp input pri output: pri pir rpi rip ipr irp '''

def str_per(str, target_str= None,prev_index=None,ctr=None):  
  len_str= len(str)
  if ctr==None:
    ctr = math.factorial(len_str)
  source_str=[]  
  if prev_index == None:
    prev_index = 0
  if target_str==None:
    target_str=[] 
  if prev_index < len_str:        
    for c in str:
      source_str.append(c) #['A','B','C']
    for k, m in enumerate(source_str):
      val = str[k];  #A B
      for n in source_str:
        if n != str[k]:
          val = val+n
      if not val in target_str:
        target_str.append(val) #[ABC , BAC, CAB]
        #print(m,target_str)
        
    if prev_index+ 1<len_str:
        source_str[prev_index], source_str[prev_index+1]= source_str[prev_index+1],source_str[prev_index]
        new_str = "".join(source_str)
        #print(new_str,prev_index+1)
        str_per(new_str,target_str,prev_index+1, ctr-1)
    else:
      if ctr >0:
        prev_index=0
        str_per(str,target_str,prev_index, ctr-1)
  return target_str
