def solution(new_id):
    answer = ''
    
    # 1단계
    answer = new_id.lower()
    
    # 2단계
    answer = list(filter(lambda x: 97 <= ord(x) <= 122 or 48 <= ord(x) <= 57 or ord(x) in [45, 46, 95] , answer))
    
    # 3단계
    updated = []
    
    idx = 0
    while True:
        if answer[idx] == '.':
            while True:
                if idx == len(answer)-1:
                    if answer[idx] != '.':
                        idx -= 1
                    break
                
                if answer[idx] != '.':
                    idx -= 1
                    break
                
                idx += 1

            updated.append('.')
        
        else:
            updated.append(answer[idx])
        
        if idx == len(answer)-1:
            break
        
        idx += 1
    
    answer = updated
        
            
    # 4단계
    while True:
        if len(answer) == 0:
            break
        if answer[0] != '.' and answer[-1] != '.':
            break
        
        if answer[0] == '.':
            answer.pop(0)
        if answer and answer[-1] == '.':
            answer.pop(-1)
    
    # 5단계
    if len(answer) == 0:
        answer.append('a')

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    
    if answer[-1] == '.':
        answer.pop(-1)
    
    # 7단계
    if len(answer) <= 2:
        answer += list(answer[-1] for _ in range(3-len(answer)))
    
    answer = ''.join(answer)
        
    return answer