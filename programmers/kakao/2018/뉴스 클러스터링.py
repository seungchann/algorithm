def make_group(str):
    ret = []

    for idx, ch in enumerate(str):
        if idx == len(str)-1:
            continue

        if 97 <= ord(ch) <= 122 and 97 <= ord(str[idx+1]) <= 122:
            ret.append(ch+str[idx+1])
            continue        

    return ret

def solution(str1, str2):
    answer = 0

    # 대,소문자 차이 무시
    str1 = str1.lower()
    str2 = str2.lower()

    str1_group = make_group(str1)
    str2_group = make_group(str2)

    if len(str1_group) == 0 and len(str2_group) == 0:
        return 1 * 65536

    intersection = []
    union = len(str2_group)

    for ch1 in str1_group:
        for i, ch2 in enumerate(str2_group):
            if ch1 == ch2:
                str2_group[i] = ""
                intersection.append(ch1)
                break

    intersection = len(intersection)
    union = union + len(str1_group) - intersection

    answer = int((intersection/union) * 65536)

    return answer