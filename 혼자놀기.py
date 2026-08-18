#https://school.programmers.co.kr/learn/courses/30/lessons/131130

#num에서 사용하는 번호는 실제 리스트번호 +1 해야함. 1,2,3  . .


def iteration(cards, num, temp, storage):
    #안되는경우
    if temp[num-1] == 1:
        next_start = None
        for i in range(len(temp)):
            if temp[i] == 0:
                next_start = i + 1
                break
        return next_start
    else:
        temp[num-1] = 1
        storage.append(cards[num-1])
        return iteration(cards, cards[num-1], temp, storage)


def solution(cards):
    temp = []
    for i in range(len(cards)):
        temp.append(0)

    storage2 = []

    start = 1
    while start is not None:
        storage = []
        start = iteration(cards, start, temp, storage)
        storage2.append(len(storage))

    storage2.sort(reverse=True)
    if len(storage2) == 1:
        answer = 0
    else:
        answer = storage2[0] * storage2[1]

    return answer
