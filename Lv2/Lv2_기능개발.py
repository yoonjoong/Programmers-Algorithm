import math
def solution(progresses, speeds):
    answer = []
    completed = [] 
    for i in range(len(progresses)):
        time = math.ceil((100 - progresses[i])/speeds[i])
        completed.append(time)
    idx=0
    for i in range(len(completed)):
        if completed[i] > completed[idx]:
            answer.append(i-idx)
            idx=i       
    answer.append(len(completed)-idx)
    return answer