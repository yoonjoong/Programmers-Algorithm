import collections
def solution(clothes):
    answer=1
    a=list(collections.Counter(c[1] for c in clothes).values())
    for i in range(len(a)):
        answer*=a[i]+1
    return answer -1