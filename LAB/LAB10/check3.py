"""
how many comparisons first function made?
===
6+5+4+3+2+1=21
==========================================
If the length of the list is N, what is (roughly) the
number of comparisons as a function of N?
===
(N-1)+(N-2)+...+0=((N-1)*N)/2
==========================================
Assuming (correctly), that sorting makes O(N log N) comparisons, how many additional
comparisons does the code you wrote for the second version make? 
====
if N=7, 7log(7)=5.92
total=5.92+7=12.92<21
the second way is better
"""
import random
import time
def closest1(L1):
    if len(L1)<2:
        return (None,None)
    cloest_1=9999
    difference_1=9999
    return_x=None
    return_y=None

    for i in range(len(L1)):
        for j in range(i+1,len(L1)):

            if L1[i]>L1[j]:
                difference_1=L1[i]-L1[j]
            elif L1[i]<L1[j]:
                difference_1=L1[j]-L1[i]
            if difference_1<cloest_1:
                cloest_1=difference_1
                return_x=L1[i]
                return_y=L1[j]

    return return_x,return_y
            
def closest2(L2):
    cloest_1=9999
    difference_1=9999
    return_x=None
    return_y=None
  
    for i in range(1,len(L2)):

        difference_1=L2[i]-L2[i-1]
        if difference_1<cloest_1:
            cloest_1=difference_1
            return_x=L2[i]
            return_y=L2[i-1]

    return return_x,return_y  
    
if __name__ == "__main__":
    time1_sum=0
    time2_sum=0    

    L1=[]
    for i in range(100):
        L1.append(random.uniform(0.0, 100.0))

    L2 = sorted(L1)
    time_1=time.time()
    
    (x1,y1) = closest1(L1)
    time_2=time.time()

    (x2,y2) = closest2(L2)
    time_3=time.time()
    
    time1=time_2-time_1
    time2=time_3-time_2

    print("method 1 takes",time1,"seconds to find solution in average when the length of list is 100.")
    print("method 2 takes",time2,"seconds to find solution in average when the length of list is 100.")

    
    
    time1_sum=0
    time2_sum=0    
    L1=[]
    for i in range(1000):
        L1.append(random.uniform(0.0, 1000.0))
    L2 = sorted(L1)
    time_1=time.time()
    
    (x1,y1) = closest1(L1)
    time_2=time.time()

    (x2,y2) = closest2(L2)
    time_3=time.time()
    
    time1=time_2-time_1
    time2=time_3-time_2

    print("method 1 takes",time1,"seconds to find solution in average when the length of list is 1000.")
    print("method 2 takes",time2,"seconds to find solution in average when the length of list is 1000.")    
      
    L1=[]
    for i in range(10000):
        L1.append(random.uniform(0.0, 10000.0))

    L2 = sorted(L1)
    time_1=time.time()
    
    (x1,y1) = closest1(L1)
    time_2=time.time()

    (x2,y2) = closest2(L2)
    time_3=time.time()
    
    time1=time_2-time_1
    time2=time_3-time_2

    print("method 1 takes",time1,"seconds to find solution in average when the length of list is 10000.")
    print("method 2 takes",time2,"seconds to find solution in average when the length of list is 10000.")    
