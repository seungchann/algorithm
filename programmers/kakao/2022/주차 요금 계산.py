from math import ceil

def calculate_time(ih, im, oh, om):
    return (oh - ih) * 60 + (om - im)
    

def solution(fees, records):
    answer = []
    
    # 차량별 주차 요금, 현재 주차장에 주차되어 있는 차량
    car_dict = {}
    parking_dict = {}
    
    # 요금 b -> basic, a -> additional
    b_min, b_fee, a_min, a_fee = map(int, fees)
    
    for record in records:
        t, car_num, io = record.split(' ')
        h, m = map(int, t.split(":"))
        
        if io == 'IN':
            parking_dict[car_num] = (h, m)
            continue
        else:
            fee = 0
            in_h, in_m = parking_dict.pop(car_num)
            time = calculate_time(in_h, in_m, h, m)
            
            if car_num in car_dict:
                car_dict[car_num] += time
            else:
                car_dict[car_num] = time
    
    for car_num, (in_h, in_m) in parking_dict.items():
        time = calculate_time(in_h, in_m, 23, 59)

        if car_num in car_dict:
            car_dict[car_num] += time
        else:
            car_dict[car_num] = time
    
    answer = list(map(lambda x: (x[0], b_fee + ((ceil((x[1] - b_min) / a_min) * a_fee) if x[1] >= b_min else 0)), car_dict.items()))
    
    answer = list(map(lambda x: x[1], sorted(answer, key= lambda x: x[0])))
    
    return answer