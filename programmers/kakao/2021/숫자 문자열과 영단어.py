def word_to_num(word):
    num_dict = {"zero": "0", "one": "1", "two": "2", 
                "three": "3", "four": "4", "five": "5", 
                "six": "6", "seven": "7", "eight": "8", 
                "nine": "9"}    
    if word in num_dict:
        return num_dict[word]
    
    else:
        return -1

def solution(s):
    s = list(s)
    answer = ""
    
    word = ""
    while True:
        if len(s) == 0:
            break
        
        if 48 <= ord(s[0]) <= 57:
            answer += s.pop(0)
            continue
                
        word += s.pop(0)
        
        if len(word) >= 3:
            num = word_to_num(word)
            if num == -1:
                continue
            answer += num
            word = ""
    
    answer = int(answer)
    return answer