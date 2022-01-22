# https://programmers.co.kr/learn/courses/30/lessons/92334
# 신고 결과 받기.py

def solution(id_list, report, k):
    answer = []
    mail_dict = {}
    dic = {}
    for i in report:
        i = i.split()
        if i[1] in dic:
            dic[i[1]].append(i[0])
        else:
            dic[i[1]] = [i[0]]
    for key, val in dic.items():
        val = list(set(val))
        if len(val) >= k:
            for user in val:
                if user in mail_dict:
                    mail_dict[user].append(key)
                else:
                    mail_dict[user] = [key]
    for i in id_list:
        answer.append(len(mail_dict[i]) if i in mail_dict else 0)
    return answer