def solution(n, lost, reserve):
    cloth = [1 for _ in range(n)]
    
    for stu_id in lost:
        cloth[stu_id-1] -= 1
    
    for stu_id in reserve:
        cloth[stu_id-1] += 1
    
    for i, c in enumerate(cloth):
        if c == 0:
            if i > 0 and cloth[i-1] > 1:
                cloth[i] += 1
                cloth[i-1] -= 1
            
            elif  i < n-1 and cloth[i+1] > 1:
                cloth[i] += 1
                cloth[i+1] -= 1
                    
    return n-cloth.count(0)