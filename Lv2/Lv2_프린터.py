def solution(priorities, location):
    answer = 0
    queue =  [(i,p) for i,p in enumerate(priorities)]
    
    while True :
        first = queue.pop(0)
        if any(first[1] < q[1] for q in queue):
            queue.append(first)
        else:
            answer +=1
            if first[0]==location:
                return answer