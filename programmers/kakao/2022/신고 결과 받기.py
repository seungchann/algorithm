def solution(id_list, report, k):
    
    id_dict = dict()
    report_dict = dict()
    report_check = []
    
    for id in id_list:
        id_dict[id] = []
        report_dict[id] = 0
    
    for val in report:
        ids = val.split(" ")
        report_check.append((ids[0], ids[1]))
        
    report_check = list(set(report_check))
    
    for id in report_check:
        id_dict[id[0]].append(id[1])
        report_dict[id[1]] += 1
    
    report_dict = dict(filter(lambda x: x[1]>=k, report_dict.items())).keys()
    
    answer = [0] * len(id_dict)
    
    for report_id in report_dict:
        for idx, ids in enumerate(id_dict.values()):
            if report_id in ids:
                answer[idx] += 1
    
    return answer