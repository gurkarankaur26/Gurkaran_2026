1. Choose you base between 3 to 13
   Done in Assignment_04Jan2026

2. Choose your symbols
   Done in Assignment_04Jan2026

3. Write upto 3 digits in your base
   Done in Assignment_04Jan2026

4. Add/subtract single digit in your base
   Done in Assignment_04Jan2026

5. Base64:0-9, A-Z, a-z, =, +

6. a. Write strategy to print next number in a number system. A system is a sequence of symbols
        next_number(symbols="0123456789AB", "1") -> 2
        next_number(symbols="0123456789AB", "B") -> 10
        next_number(symbols="0123456789AB", "111") -> 112
        next_number(symbols="0123456789AB", "BB") -> 100
        next_number(symbols="0123456789AB", "ABAB") -> ABB0

        def next_number(symbols, n):
            base =len(symbols)
            str_n = str(n)
            rev_n = str_n[::-1] #Reverse the number
            total_len = len(str_n)    
            next_num=''
            all_last_char=True 
            for char in rev_n:  
                if char != symbols[base-1]:
                    all_last_char=False  
                    
                index_char = symbols.find(char) 
                # if digit/char in the number is not the last symbol of the base then 
                # find the index of the char in symbols and increment it by one and get 
                # the next number
                if  char != symbols[base-1]:             
                    next_num = symbols[index_char+1]+next_num 
                    break
                else:
                    # if digit/char in the number is  the last symbol of the base then 
                    # next number will be the first symbol of the base concatenated with 
                    # the next number
                    next_num = symbols[0]+next_num
            result=''
            if all_last_char==True:
                # if all the char/digit in the number are last symbol of the base
                # then append the second symbol to the next number i.e. if BBB then 1000
                result = symbols[1]+ next_num
            else:
                # else append to next number value, the remaining char/digit of the number that 
                #  were not incremented.
                result = str_n[0:total_len - len(next_num)]+ next_num
            print(result)
            

        
    b. Print first n digits in symbols="0123456789AB"

      ### Start: Function to print n digit for the given base

      def print_ndigit_no_in_base(symbols,n):
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
       ### End: Function to print n digit for the given base

       ### Output: Print n digit for the given base: Base 12 3 digit numbers

        000 001 002 003 004 005 006 007 008 009 00A 00B
        010 011 012 013 014 015 016 017 018 019 01A 01B
        020 021 022 023 024 025 026 027 028 029 02A 02B
        030 031 032 033 034 035 036 037 038 039 03A 03B
        040 041 042 043 044 045 046 047 048 049 04A 04B
        050 051 052 053 054 055 056 057 058 059 05A 05B
        060 061 062 063 064 065 066 067 068 069 06A 06B
        070 071 072 073 074 075 076 077 078 079 07A 07B
        080 081 082 083 084 085 086 087 088 089 08A 08B
        090 091 092 093 094 095 096 097 098 099 09A 09B
        0A0 0A1 0A2 0A3 0A4 0A5 0A6 0A7 0A8 0A9 0AA 0AB
        0B0 0B1 0B2 0B3 0B4 0B5 0B6 0B7 0B8 0B9 0BA 0BB

        100 101 102 103 104 105 106 107 108 109 10A 10B
        110 111 112 113 114 115 116 117 118 119 11A 11B
        120 121 122 123 124 125 126 127 128 129 12A 12B
        130 131 132 133 134 135 136 137 138 139 13A 13B
        140 141 142 143 144 145 146 147 148 149 14A 14B
        150 151 152 153 154 155 156 157 158 159 15A 15B
        160 161 162 163 164 165 166 167 168 169 16A 16B
        170 171 172 173 174 175 176 177 178 179 17A 17B
        180 181 182 183 184 185 186 187 188 189 18A 18B
        190 191 192 193 194 195 196 197 198 199 19A 19B
        1A0 1A1 1A2 1A3 1A4 1A5 1A6 1A7 1A8 1A9 1AA 1AB
        1B0 1B1 1B2 1B3 1B4 1B5 1B6 1B7 1B8 1B9 1BA 1BB

        200 201 202 203 204 205 206 207 208 209 20A 20B
        210 211 212 213 214 215 216 217 218 219 21A 21B
        220 221 222 223 224 225 226 227 228 229 22A 22B
        230 231 232 233 234 235 236 237 238 239 23A 23B
        240 241 242 243 244 245 246 247 248 249 24A 24B
        250 251 252 253 254 255 256 257 258 259 25A 25B
        260 261 262 263 264 265 266 267 268 269 26A 26B
        270 271 272 273 274 275 276 277 278 279 27A 27B
        280 281 282 283 284 285 286 287 288 289 28A 28B
        290 291 292 293 294 295 296 297 298 299 29A 29B
        2A0 2A1 2A2 2A3 2A4 2A5 2A6 2A7 2A8 2A9 2AA 2AB
        2B0 2B1 2B2 2B3 2B4 2B5 2B6 2B7 2B8 2B9 2BA 2BB

        300 301 302 303 304 305 306 307 308 309 30A 30B
        310 311 312 313 314 315 316 317 318 319 31A 31B
        320 321 322 323 324 325 326 327 328 329 32A 32B
        330 331 332 333 334 335 336 337 338 339 33A 33B
        340 341 342 343 344 345 346 347 348 349 34A 34B
        350 351 352 353 354 355 356 357 358 359 35A 35B
        360 361 362 363 364 365 366 367 368 369 36A 36B
        370 371 372 373 374 375 376 377 378 379 37A 37B
        380 381 382 383 384 385 386 387 388 389 38A 38B
        390 391 392 393 394 395 396 397 398 399 39A 39B
        3A0 3A1 3A2 3A3 3A4 3A5 3A6 3A7 3A8 3A9 3AA 3AB
        3B0 3B1 3B2 3B3 3B4 3B5 3B6 3B7 3B8 3B9 3BA 3BB

        400 401 402 403 404 405 406 407 408 409 40A 40B
        410 411 412 413 414 415 416 417 418 419 41A 41B
        420 421 422 423 424 425 426 427 428 429 42A 42B
        430 431 432 433 434 435 436 437 438 439 43A 43B
        440 441 442 443 444 445 446 447 448 449 44A 44B
        450 451 452 453 454 455 456 457 458 459 45A 45B
        460 461 462 463 464 465 466 467 468 469 46A 46B
        470 471 472 473 474 475 476 477 478 479 47A 47B
        480 481 482 483 484 485 486 487 488 489 48A 48B
        490 491 492 493 494 495 496 497 498 499 49A 49B
        4A0 4A1 4A2 4A3 4A4 4A5 4A6 4A7 4A8 4A9 4AA 4AB
        4B0 4B1 4B2 4B3 4B4 4B5 4B6 4B7 4B8 4B9 4BA 4BB

        500 501 502 503 504 505 506 507 508 509 50A 50B
        510 511 512 513 514 515 516 517 518 519 51A 51B
        520 521 522 523 524 525 526 527 528 529 52A 52B
        530 531 532 533 534 535 536 537 538 539 53A 53B
        540 541 542 543 544 545 546 547 548 549 54A 54B
        550 551 552 553 554 555 556 557 558 559 55A 55B
        560 561 562 563 564 565 566 567 568 569 56A 56B
        570 571 572 573 574 575 576 577 578 579 57A 57B
        580 581 582 583 584 585 586 587 588 589 58A 58B
        590 591 592 593 594 595 596 597 598 599 59A 59B
        5A0 5A1 5A2 5A3 5A4 5A5 5A6 5A7 5A8 5A9 5AA 5AB
        5B0 5B1 5B2 5B3 5B4 5B5 5B6 5B7 5B8 5B9 5BA 5BB

        600 601 602 603 604 605 606 607 608 609 60A 60B
        610 611 612 613 614 615 616 617 618 619 61A 61B
        620 621 622 623 624 625 626 627 628 629 62A 62B
        630 631 632 633 634 635 636 637 638 639 63A 63B
        640 641 642 643 644 645 646 647 648 649 64A 64B
        650 651 652 653 654 655 656 657 658 659 65A 65B
        660 661 662 663 664 665 666 667 668 669 66A 66B
        670 671 672 673 674 675 676 677 678 679 67A 67B
        680 681 682 683 684 685 686 687 688 689 68A 68B
        690 691 692 693 694 695 696 697 698 699 69A 69B
        6A0 6A1 6A2 6A3 6A4 6A5 6A6 6A7 6A8 6A9 6AA 6AB
        6B0 6B1 6B2 6B3 6B4 6B5 6B6 6B7 6B8 6B9 6BA 6BB

        700 701 702 703 704 705 706 707 708 709 70A 70B
        710 711 712 713 714 715 716 717 718 719 71A 71B
        720 721 722 723 724 725 726 727 728 729 72A 72B
        730 731 732 733 734 735 736 737 738 739 73A 73B
        740 741 742 743 744 745 746 747 748 749 74A 74B
        750 751 752 753 754 755 756 757 758 759 75A 75B
        760 761 762 763 764 765 766 767 768 769 76A 76B
        770 771 772 773 774 775 776 777 778 779 77A 77B
        780 781 782 783 784 785 786 787 788 789 78A 78B
        790 791 792 793 794 795 796 797 798 799 79A 79B
        7A0 7A1 7A2 7A3 7A4 7A5 7A6 7A7 7A8 7A9 7AA 7AB
        7B0 7B1 7B2 7B3 7B4 7B5 7B6 7B7 7B8 7B9 7BA 7BB

        800 801 802 803 804 805 806 807 808 809 80A 80B
        810 811 812 813 814 815 816 817 818 819 81A 81B
        820 821 822 823 824 825 826 827 828 829 82A 82B
        830 831 832 833 834 835 836 837 838 839 83A 83B
        840 841 842 843 844 845 846 847 848 849 84A 84B
        850 851 852 853 854 855 856 857 858 859 85A 85B
        860 861 862 863 864 865 866 867 868 869 86A 86B
        870 871 872 873 874 875 876 877 878 879 87A 87B
        880 881 882 883 884 885 886 887 888 889 88A 88B
        890 891 892 893 894 895 896 897 898 899 89A 89B
        8A0 8A1 8A2 8A3 8A4 8A5 8A6 8A7 8A8 8A9 8AA 8AB
        8B0 8B1 8B2 8B3 8B4 8B5 8B6 8B7 8B8 8B9 8BA 8BB

        900 901 902 903 904 905 906 907 908 909 90A 90B
        910 911 912 913 914 915 916 917 918 919 91A 91B
        920 921 922 923 924 925 926 927 928 929 92A 92B
        930 931 932 933 934 935 936 937 938 939 93A 93B
        940 941 942 943 944 945 946 947 948 949 94A 94B
        950 951 952 953 954 955 956 957 958 959 95A 95B
        960 961 962 963 964 965 966 967 968 969 96A 96B
        970 971 972 973 974 975 976 977 978 979 97A 97B
        980 981 982 983 984 985 986 987 988 989 98A 98B
        990 991 992 993 994 995 996 997 998 999 99A 99B
        9A0 9A1 9A2 9A3 9A4 9A5 9A6 9A7 9A8 9A9 9AA 9AB
        9B0 9B1 9B2 9B3 9B4 9B5 9B6 9B7 9B8 9B9 9BA 9BB

        A00 A01 A02 A03 A04 A05 A06 A07 A08 A09 A0A A0B
        A10 A11 A12 A13 A14 A15 A16 A17 A18 A19 A1A A1B
        A20 A21 A22 A23 A24 A25 A26 A27 A28 A29 A2A A2B
        A30 A31 A32 A33 A34 A35 A36 A37 A38 A39 A3A A3B
        A40 A41 A42 A43 A44 A45 A46 A47 A48 A49 A4A A4B
        A50 A51 A52 A53 A54 A55 A56 A57 A58 A59 A5A A5B
        A60 A61 A62 A63 A64 A65 A66 A67 A68 A69 A6A A6B
        A70 A71 A72 A73 A74 A75 A76 A77 A78 A79 A7A A7B
        A80 A81 A82 A83 A84 A85 A86 A87 A88 A89 A8A A8B
        A90 A91 A92 A93 A94 A95 A96 A97 A98 A99 A9A A9B
        A90 A91 A92 A93 A94 A95 A96 A97 A98 A99 A9A A9B
        AA0 AA1 AA2 AA3 AA4 AA5 AA6 AA7 AA8 AA9 AAA AAB
        AB0 AB1 AB2 AB3 AB4 AB5 AB6 AB7 AB8 AB9 ABA ABB

        B00 B01 B02 B03 B04 B05 B06 B07 B08 B09 B0A B0B
        B10 B11 B12 B13 B14 B15 B16 B17 B18 B19 B1A B1B
        B20 B21 B22 B23 B24 B25 B26 B27 B28 B29 B2A B2B
        B30 B31 B32 B33 B34 B35 B36 B37 B38 B39 B3A B3B
        B40 B41 B42 B43 B44 B45 B46 B47 B48 B49 B4A B4B
        B50 B51 B52 B53 B54 B55 B56 B57 B58 B59 B5A B5B
        B60 B61 B62 B63 B64 B65 B66 B67 B68 B69 B6A B6B
        B70 B71 B72 B73 B74 B75 B76 B77 B78 B79 B7A B7B
        B80 B81 B82 B83 B84 B85 B86 B87 B88 B89 B8A B8B
        B90 B91 B92 B93 B94 B95 B96 B97 B98 B99 B9A B9B
        BA0 BA1 BA2 BA3 BA4 BA5 BA6 BA7 BA8 BA9 BAA BAB
        BB0 BB1 BB2 BB3 BB4 BB5 BB6 BB7 BB8 BB9 BBA BBB
       ### Output: Print n digit for the given base: Base 12 3 digit numbers



7. Add two numbers at least 5 pairs.
   Done in Assignment_04Jan2026

8. Write an strategy to add two numbers of multiple digits in your base.
   ### Start: Function to add numbers in a given base
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
    def add_two_numbers(symbols,num1:str,num2:str): 
        result=''
        n2=num1
        ctr = int(convert_num_todecimal(symbols,num2))
        for i in range(ctr):
            result= next_number(symbols,n2)
            n2=result
        return(result)

   ### End Function to add numbers in a given base


9. Subtract two numbers at least 5 pairs.
   Manually done in Assignment_04Jan2026

10. Multiplication
    Manually done in Assignment_04Jan2026

    ### Start: Function to multiply two numbers in the given base
    ## Code available in \src\multiply.py and in Jupyter notebook-answers.ipynb
    
    import  numtodecimal
    def multiply_two_numbers(symbols,num1:str,num2:str):
        res=0
        n1=num1
        ctr = int(numtodecimal.convert_num_todecimal(symbols,num2))
        #print('ctr:',ctr)
        for i in range(ctr-1):
            res= add.add_two_numbers(symbols,num1,n1) # 2+2+2+2+2+2          
            num1=res
            #print('i:'+str(i),'res:',str(res))
        return(res)
      ### End: Function to multiply two numbers in the given base
    

11. Write code to prepare the tables as array of base * base - 2D list containing your table.
    base 7 - 0*0 to 6*6 (49)
    ### Start: Function to print tables of given base starting from 2
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
            matrix[j][k+1]=multiply_two_numbers(symbols,str(num1),str(num2))
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
   
    ### End: Function to print tables of given base starting from 2




    ### Function Call to print tables in Base 12 and Output
    tables("0123456789AB")
    Output is as below:
    ************************************************************
                    Base 12 Tables from 2 to B
    ************************************************************
    2     3     4     5     6     7     8     9     A     B     
    ************************************************************

    4     6     8     A     10    12    14    16    18    1A    
    6     9     10    13    16    19    20    23    26    29    
    8     10    14    18    20    24    28    30    34    38    
    A     13    18    21    26    2B    34    39    42    47    
    10    16    20    26    30    36    40    46    50    56    
    12    19    24    2B    36    41    48    53    5A    65    
    14    20    28    34    40    48    54    60    68    74    
    16    23    30    39    46    53    60    69    76    83    
    18    26    34    42    50    5A    68    76    84    92    
    1A    29    38    47    56    65    74    83    92    A1
    ### Function Call to print tables in Base 12 and Output

12. Write code to multiply numbers, you can use the tables and add_two_numbers()

    ### Start: Function to multiply two numbers in the given base
    ## Code available in \src\multiply.py and in Jupyter notebook-answers.ipynb
    ### Start: Function to multiply two numbers of a given base

    def multiply_two_numbers(symbols,num1:str,num2:str):
     res=0
     n1=num1
     ctr = int(convert_num_todecimal(symbols,num2))
     #print('ctr:',ctr)
     for i in range(ctr-1):
          res= add_two_numbers(symbols,num1,n1)         
          num1=res
          #print('i:'+str(i),'res:',str(res))
     return(res)
     

    ### End: Function to multiply two numbers of a given base

13. Write code to fiind log of a number

   ***Start: Python function to calculate log of given baseof a number upto 10000.***

   def calbaselog(base,n):
        p = 0
        ctn = True
        step = 0.1
        while ctn:
            if base ** (p + step) <= n:
                p = p + step
            else:
                step = step / 10
                if step < 1e-6:
                    ctn = False

        print(f"Log{base}({n}) is {p:.6f}")  

    ***End: Python function to calculate log of given base of a number.***

   ***Function Call to calculate log of given base of a number.***
    function call : calbaselog(12,1000000) 
    output:Log12(1000000) is 5.559770
    ***Function Call to calculate log of given base of a number.***

14. Write code to find square root of number by guessing logic.

    *** Start: Function to calculate square root of number by guessing the range***

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

   *** End: Function to calculate square root of number by guessing the range***

