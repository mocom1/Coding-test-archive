def solution(bandage, health, attacks):
    current_health = health
    stack = 0
    n = 0
    time = 0
    end_time = attacks[-1][0]
    answer = 0

    while time <= end_time: #턴돌리기
        if time == attacks[n][0]: #피깎기
            current_health -= attacks[n][1]
            n = n+1
            time += 1
            stack = 0

        elif current_health <= 0: #체력 0미만 시 예외처리
            answer = -1
            stack = 0
            return -1

        else: #회복
            if stack == bandage[0]: #추가회복량
                stack = 0
                time += 1
                current_health += bandage[2]

            else: #체력일반회복
                stack += 1
                time += 1
                current_health += bandage[1]

            if current_health >= health: #체력상한선 정상화
                current_health = health
        answer = current_health
    
    return answer















