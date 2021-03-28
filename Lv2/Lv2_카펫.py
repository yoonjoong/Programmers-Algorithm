def solution(brown, yellow):
    answer = []
    size = brown + yellow
    
    for i in range(1,size//2 ):
        if size %i ==0:
            if (size/i)*2 + i*2 -4 == brown:
                return([size//i,i])