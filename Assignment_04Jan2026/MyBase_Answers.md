1. Selected Base 4 for base related tasks. Below is the Base4 upto three digits

   Base10   Base4
      0      0
      1      1
      2      2
      3      3
      4      10
      5      11
      6      12
      7      13
      8      20
      9      21
      10     22
      11     23
      12     30
      13     31
      14     32
      15     33
      16     100
      17     101
      18     102
      19     103
      20     110
      21     111
      22     112
      23     113
      24     120
      25     121
      26     122
      27     123
      28     130
      29     131
      30     132
      31     133
      32     200
      33     201
      34     202
      35     203
      36     210
      37     211
      38     212
      39     213
      40     220
      41     221
      42     222
      43     223
      44     230
      45     231
      46     232
      47     233
      48     300  
      49     301
      50     302
      51     303
      52     310
      53     311
      54     312
      55     313
      56     320
      57     321
      58     322
      59     323
      60     330
      61     331
      62     332
      63     333
      64     1000
     
 2. a. Single Digit Addition in Base4
       
         1 2  3
       1 2 3  10
       2 3 10 11

       2+3 = 11
       3+1 = 10
       

    b. Single Digit Subtraction in Base4

       3-1  = 2
       3-2  = 1

3.  a. Multi Digit Addition in Base4

       22 + 11 = 33
       31 + 33 = 130 (3 +1 is 10 so 1 carry over -> 1 + 3 + 3 = 10 + 3 = 13)
    
    b. Multi Digit Subtraction in Base 4       

       22 - 10 =  12
       23 - 12 =  11
       33 - 11 =  22

4. Single Digit Multiplication

       Tables in  base 4

       1  2   3
       2  10  12
       3  12  21       

       2*3 = 12 
       2*2 = 20  

5. Double Digit Multiplication  
       
       12 
      *31
      ----
       12
     102
     -----
     1032
     ------

     33
    *13
    -----
     231
     33
    -----
    1221
    -----

6. Convert from your base to decimal
    yourbase(Base4) -> base10
    1   -> 1
    10  -> 4 
    100 -> 16 (1*4^2 + 0.4^1 + 0.4^0 = 16+0+0)
    11  -> 5  (1*4^1 + 1*4^0 = 4 +1)
    111 -> 21 (1*4^2 + 1*4^1 + 1*4^0 = 16+4+1)
    20  -> 8  (2*4^1 + 0*4^0 = 8 +0)
    121 -> 25 (1*4^2 + 2*4^1 + 1*4^0 = 16+8+1)

    ***Start: Python Function to convert a number from a specified base to decimal***
    def convert_num_todecimal(base,num):
    ln= len(str(num))
    res=0
    str_num=str(num)
    for i in str_num:
        if(ln<0):
         break
        res=res+ int(i)*(base**(ln-1))
        ln=ln-1
    print(res)
     ***End: Python Function to convert a number from a specified base to decimal***

7. What is the smallest base possible?
   A. 1   B. 2
   Base === # of symbols
   Base2 is the smallest base possible as we at least two symbols are required to create a number

8.  In base 7, how many numbers can we represent with 1 digit?
    7

9.  In base 7, how many numbers can we represent with 2 digits?
      #First Digit  can be  1,2,3,4,5,6 (exclude 0 as 01 will be 1 02 will be 2...i.e. a single digit number)
      First Digit  can be  0,1,2,3,4,5,6 
      Second Digit can be  0,1,2,3,4,5,6
      Total Numbers for first digit  = 7
      Total Numbers for second digit = 7
      Total Number of combinations for two digits: 7*7 =42 

      For Base4
      First Digit  can be  0,1,2,3
      Second Digit can be 0,1,2,3
      Total Numbers for first digit = 4
      Total Numbers for second digit =4
      Total Number of combinations for two digit: 4*4 =16 (base10)

10.  In base7, how many numbers can we represent with d digits?
      Total Numbers for first digit  = 7
      Total Numbers for second digit = 7
      Total Numbers for three digit  = 7
      Total Numbers for fourth digit = 7
      ..
      ..
      ..
      Total Numbers for d digit = 7
      7^(d)

11. In baseb, how many numbers can we represent with 3 digits?
      b^3

12. In baseb, how many numbers can we represent with d digits?
     ***Start: Python function to find to total numbers for specified base and digit***
     def total_nos_for_base_digit(b,d):
      res = b**3
      return res
     ***End: Python function to find to total numbers for specified base and digit***
      
13. In base10, to represent 1000 numbers how many digits do we need?
      3 = log(1000)

14. In base10, to represent N numbers how many digits do we need?
      d = log10(N)

      10 ^ d = N (number)
     => d = log10(N)

# So log is nothing but the count of zeros

15. In base 2, to represent N numbers how many digits do we need?
    2^d = N
    d = log2(N)

16. Compute log10 of 456 and few more numbers. You can use power(i.e. 10**x) in python but Do not 
    use math.log10. Accurate to say 3 decimal digits.
    Try computing Manually.
    Write full strategy.
    Step / Code it in your own way.
   
    log(1000) = 3       
    10**3 = 1000
    10**(1.5)=  31.622776601683793 -> Try power < 3 as 456 < 1000 and that is 10^3 -> Very Low 
    10**(2.5)=  316.22776601683796 -> Try power 2.5 < power 3
    10**(2.7)=  501.18723362727246 -> Find in the range 2.5- 2.7
    10**(2.6)=  398.1071705534973  -> Find in the range 2.6 -2.7
    10**(2.68)= 478.6300923226385
    10**(2.66)= 457.0881896148752
    10**(2.65)= 446.683592150963   -> Find in the range 2.65 -2.66
    10**(2.658)= 454.9880601500485 
    10**(2.659)= 456.03691595129595
    
    log10(456) = 2.659
  
   ***Start: Python function to calculate log of a number upto 10000.***
    def calbase10log(n):
    if n <10000:
     #print(n)
     pow=4
     while(pow>0):
        #print('power',pow)
        res=int(10**pow)
        #print(res)
        if res==n:
         break
        else:
         pow = pow -.00001
        
     print(f"Log10({n}) is {pow}")    
    else:
     print('No. should not be greater than 10000')  

    ***End: Python function to calculate log of a number upto 10000.***

    ***Function Call to calculate log of a number upto 10000.***
    function call : calbase10log(456) 
    output: Log10(456) is 2.659909999991221

    function call : calbase10log(231) 
    output: Log10(231) is 2.365479999989292
    ***Function Call to calculate log of a number upto 10000.***

17. Write your strategy to compute SQRT! Work out manually first using python as calculator and 
    then keep automating.

    *** Start: Python function to calculate square root of a number ***
    def calsquareroot(n):
    sqrt= n**(1/2)
    print(f"Square root of {n} is {sqrt}")
    *** End: Python function to calculate square root of a number ***
    
    *** Calling Python function to calculate square root of a number ***
    Function Call:  calsquareroot(64)
    Output: Square root of 64 is 8.0

    Function Call:  calsquareroot(6)
    Output: Square root of 6 is 2.449489742783178

    Function Call:  calsquareroot(64)
    Output: Square root of 64 is 2.8284271247461903    
   *** Calling Python function to calculate square root of a number ***  
               


