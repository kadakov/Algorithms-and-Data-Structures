with open('input.in', 'r') as file:
    N, M = map(int, file.readline().split())
    roads = [list(map(int, file.readline().split())) for _ in range(M)]
    matrix = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        matrix[i][i] = 0
    for i in range(M):
        u, v, p = roads[i][0], roads[i][1], roads[i][2]
        matrix[u - 1][v - 1] = p
        matrix[v - 1][u - 1] = p
    for k in range(N):
        d = matrix
        for i in range(N):
            for j in range(N):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    min_row = sum(matrix[0])
    min_index = 0
    for i in range(1, N):
        if min_row > sum(matrix[i]):
            min_index = i
            min_row = sum(matrix[i])
    min_index += 1


with open('output.out', 'w') as file:
    file.write(f"{min_index} {min_row}\n")