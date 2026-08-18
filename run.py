    def solution(players, callings):
        rank = {name: idx for idx, name in enumerate(players)} #딕셔너리형태로

        for player in range(len(callings)):
            i = rank[callings[player]]

            if players[i] == callings[player]:
                players[i], players[i-1] = players[i-1], players[i]
                rank[players[i]] = i
                rank[players[i-1]] = i-1

        answer = players
        return answer

    #선형탐색 -> 해시탐색
    #python은 temp없어도 swap가능