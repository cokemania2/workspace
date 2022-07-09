from collections import defaultdict

def calc_fee(default_fee, default_time, unit_time, unit_fee, t):
    if t <= default_time:
        return default_fee
    t -= default_time
    return ((t // unit_time) + (0 if t % unit_time == 0 else 1))* unit_fee + default_fee

def time_to_minute(t):
    t = t.split(':')
    return int(t[0]) * 60 + int(t[1])

def time_calc(start, end):
    return time_to_minute(end) - time_to_minute(start)

def solution(fees, records):
    answer = []
    book = defaultdict(int)
    parking = defaultdict(int)

    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    
    for record in records:
        record = record.split()
        if record[2] == 'IN':
            parking[record[1]] = record[0]
        else:
            record_time = time_calc(parking[record[1]], record[0])
            book[record[1]] += record_time
            parking.pop(record[1])
    for key, value in parking.items():
        record_time = time_calc(value, "23:59")
        book[key] += record_time
    
    for _, value in sorted(book.items()):
        answer.append(calc_fee(default_fee, default_time, unit_time, unit_fee, value))
    return answer