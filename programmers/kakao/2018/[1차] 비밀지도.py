def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        wall = arr1[i] | arr2[i]
        
        row = ""
        for j in range(n):
            row = ("#" if (wall % 2 == 1) else " ") + row
            wall = wall >> 1
        answer.append(row)
    
    return answer