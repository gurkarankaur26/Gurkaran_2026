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