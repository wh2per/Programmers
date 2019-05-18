def solution(land):
    rows = 100001
    cols = 4
    d = []
    for row in range(rows) :
        d += [[0]*cols]

    for i in range(4):
        d[0][i] = land[0][i]

    for i in range(1,len(land)):
        for j in range(4):    # 현재 줄 선택
            for k in range(4):   # 다음 줄 선택
                if k != j:
                    d[i][j] = max(d[i][j], land[i][j] + d[i-1][k])
    return max(d[len(land)-1])