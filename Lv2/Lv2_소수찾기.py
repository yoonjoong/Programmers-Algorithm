from itertools import chain, permutations
import math
def is_prime(num):
    if num<2:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i ==0 :
                return False
    return True
def solution(numbers):
    answer = 0  
    num_list = list(map(int,numbers))
    
    array=list(chain.from_iterable(permutations(num_list, r) for r in range(1, len(num_list) + 1)))
    
    
    tmp=[]
    for i in array:
        tmp.append(int("".join(list(map(str,i)))))
    tmp=list(set(tmp))
    
    for i in tmp:
        if is_prime(i) == True:
            answer+=1
    return answer