def solution(record):
    answer = []
    name_dict = {}

    for val in record:
        val = val.split()
        command, uid, nickname = val[0], val[1], ""

        if len(val) == 3:
            nickname = val[2]

        if command == "Enter":
            answer.append(uid + "  " + "님이 들어왔습니다.")
            name_dict[uid] = nickname
            continue

        elif command == "Leave":
            answer.append(uid + "  " + "님이 나갔습니다.")
            continue

        elif command == "Change":
            name_dict[uid] = nickname
            continue

    for idx, message in enumerate(answer):
        uid, msg = message.split("  ")
        answer[idx] = name_dict[uid] + msg

    return answer