import re
# https://programmers.co.kr/learn/courses/30/lessons/72410
# 신규 아이디 추천.py

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[^0-9a-z-_.]','',new_id)
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    if new_id[0] == '.':
        new_id = new_id[1:]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id