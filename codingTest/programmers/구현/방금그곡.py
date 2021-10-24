# https://programmers.co.kr/learn/courses/30/lessons/17683
# 방금그곡.py

def replace_word(s):
    return s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

def solution(m, musicinfos):
    answer = "(None)"
    max_time = 0
    m = replace_word(m)
    for info in musicinfos:
        s = ''
        info = info.split(',')
        before_time = list(map(int,info[0].split(':')))
        after_time = list(map(int,info[1].split(':')))
        time = (after_time[0] - before_time[0]) * 60 + after_time[1] - before_time[1]
        new_str = replace_word(info[3])
        for i in range(time // len(new_str)):
            s += new_str
        s += new_str[:time%len(new_str)]
        if m in s and max_time < time:
            max_time = time
            answer = info[2]
    return answer