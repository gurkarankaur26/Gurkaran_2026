# What is the order of complexity of 
    - Multiplcation of matrics n x n with n x n?
      Answer: matmul.py => Time =O(n^3) Space = n^2 + n^2 =2(n^2)= O(n^2)

    - Multiplcation of matrics a x b with b x c?
      Answer: matmul.py => Time =O(a*b*c) Space = a*b + a*b =2(a*b)= O(a*b)      

    - Solving n variable equation?

    - Find a number in a unsorted list? 
       Answer: Linear search => Time =O(n) Space = O(1)

    - a binary search tree?
       Answer:As per binary_search_tree.py
         Insert : Balanced-> Time = O(logn) Space= O(1)  Worst -> Time = O(n)
         SearchBst: Balanced-> Time = O(logn) Space= O(1)  Worst -> Time= O(n)
         PrintBst:  Time =O(n) => All nodes are to be visited Space= O(logn)=>At any moment, the stack only contains one path of the tree. so it is equal to the height of the Tree=log n

    - Your own sorting algorithms?
       Answer:  sort.py=> Time= O(n^2) Space = O(1)

    - You have a list containing 0s and 1s. [0, 1, 0, 0, 1, 0, 1] Propose various methods to sort 
      them and report the time and space complexity for each.
      Answer:  
         1. sort.py=> Time= O(n^2): No of loops is two and each loop runs n times. Space = O(1)
         2. mergesort.py=> Time = O(nlogn) Merge runs for all elements so work per call is n and 
            recursive call levels is logn so total time complexity is O(nLogn) Space=O(n)

    - check method of our decision tree?
      Answer:
         job_decision_tree.py =>  Time = O(logn) Space = O(n)