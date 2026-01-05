 1. I choose Base 4. Below is the Base4 upto three digits

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
     
 2. a. Single Digit Addtion in Base4

       2+3 = (5/4=1  reminder  1 1/4=0 remainder 1) = 11 
       3+6 = (9/4=2  remainder 1 2/4=0 remaider  2) = 21  
       8+9 = (17/4=4 remainder 1 4/4=1 remainder 0  1/4=0 remainder 1) = 101
       5+6 = (11/4=2 remainder 3 2/4=0 remainder 2) = 23

    b. Single Digit Subtraction in Base4

       9-2 = (7/4=1 remainder 3 1/4 = 0 remainder 1) = 13
       7-3 = (4/4=1 remainder 0 1/4=0 remainder 1) = 10
       8-6=  (2/4=0 remainder 2) = 2

3.  a. Multi Digit Addition in Base4

       10+22=  (32/4=8  remainder 0 8/4=2  remainder 0 2/4=0 reaminder 2)= 200      
       31+32 = (63/4=15 remainder 3 15/4=3 remainder 2 3/4=0 remainder 3)= 333      
       40+13 = (53/4=13 remainder 1 13/4=3 remainder 2 3/4=0 remainder 3)= 311
    
    b. Multi Digit Subtraction in Base 4

       22-10 = (12/4=3  remainder 0 3/4=0 remainder 3 ) = 30  
       44-13 = (31/4= 7 remainder 3 7/4=1 remainder 3 1/4=0 remainder 1)= 133
       31-12 = (19/4= 4 remainder 3 4/4=1 remainder 0 1/4=0 remainder 1) = 103

4. Single Digit Multipliction

       2*3 = (5/4=1  remainder 1 1/4=0 remainder 1) = 11  
       3*4 = (12/4=3 remainder 0 3/4=0 remainder 3) = 30  
       4*6 = (24/4=6 remainder 0 6/4 1 remainder 2 1/4=0 reminder 1) = 120

5. Double Digit Multiplication    

        22       
       *31 
      ______
        22
      132
      ______
      2002
      ______

       12
      *21
      ______
       12
      30
      ______
      312
      ______

6. Convert from your base to decimal
    yourbase(Base4) -> base10
    1   -> 1
    10  -> 4 
    100 -> 16 (1*4^2 + 0.4^1 + 0.4^0 = 16+0+0)
    11  -> 5  (1*4^1 + 1*4^0 = 4 +1)
    111 -> 13 (1*4^2 + 1*4^1 + 1*4^0 = 8+4+1)
    20  -> 8  (2*4^1 + 0*4^0 = 8 +0)
    121 -> 25 (1*4^2 + 2*4^1 + 1*4^0 = 16+8+1)

7. What is the smallest base possible?
   A. 1   B. 2
   Base === # of symbols
   Base2 is the smallet base possible as we atleast two symbols are required to create a number

8.  In base 7, how many numbers can we represent with 1 digit?
    7

9.  In base 7, how many numbers can we represent with 2 digits?
      First Digit  can be  1,2,3,4,5,6
      Second Digit can be  0,1,2,3,4,5,6
      Total Numbers for first digit  = 6
      Total Numbers for second digit = 7
      Total Number of combinations for two digits: 6*7 =42 (base10)

      For Base4
      First Digit  can be  1,2,3
      Second Digit can be 0,1,2,3
      Total Numbers for first digit = 3
      Total Numbers for second digit =4
      Total Number of combinations for two digit: 3*4 =12 (base10)

9.  In base7, how many numbers can we represent with d digits?
      Total Numbers for first digit  = 6
      Total Numbers for second digit = 7
      Total Numbers for three digit  = 7
      Total Numbers for fourth digit = 7
      ..
      ..
      ..
      Total Numbers for d digit = 7
      6*7^(d-1)

10. In baseb, how many numbers can we represent with 3 digits?
      (b-1)*b^2

11. In baseb, how many numbers can we represent with d digits?
      (b-1)*b^(d-1)

12. In base10, to represent 1000 numbers how many digits do we need?
      3 = log(1000)

13. In base10, to represent N numbers how many digits do we need?
      d = log10(N)

      10 ^ d = N (number)
     => d = log10(N)

# So log is nothing but the count of zeros

14. In base 2, to represent N numbers how many digits do we need?
2^d = N
d = log2(N)

                
