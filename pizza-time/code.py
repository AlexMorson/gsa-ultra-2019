import sys
sys.setrecursionlimit(1000000)

def solution(N, M, A):
    order = []
    seen = [[False for _ in range(M)] for _ in range(N)]
    lengths = [[1 for _ in range(M)] for _ in range(N)]
    def topological_sort():
        def explore(x, y):
            seen[y][x] = True
            cA = A[y][x]
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= ny < N and 0 <= nx < M:
                    if not seen[ny][nx] and A[ny][nx] < cA:
                        explore(nx, ny)
            order.append((x, y))


        for y in range(N):
            for x in range(M):
                if not seen[y][x]:
                    explore(x, y)
    topological_sort()

    for x, y in order[::-1]:
        cA = A[y][x]
        l = lengths[y][x]
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= ny < N and 0 <= nx < M:
                if A[ny][nx] < cA and lengths[ny][nx] < l + 1:
                    lengths[ny][nx] = l + 1

    return max(max(row) for row in lengths)


if __name__ == "__main__":
    import random

    with open("input.txt", "r") as f:
        N, M = map(int, f.readline().strip().split())
        A = [[*map(int, line.strip().split())] for line in f.readlines()]

    N = M = 1000
    A = [[500*i+500*j+random.randint(1, 1000) for i in range(M)] for j in range(N)]

    A = [[1000*j+i for i in range(M)] for j in range(N)]
    for y in range(0, N, 2):
        A[y] = A[y][::-1]
    #A = [
    #    [ 1,  3,  4,  6,  5,  7,  7,  9, 10, 11],
    #    [ 2,  5,  6,  7,  7,  8,  8, 11, 11, 13],
    #    [ 3,  5,  7,  6,  9, 10, 10, 12, 11, 14],
    #    [ 5,  7,  8,  8, 10, 11, 11, 12, 14, 13],
    #    [ 5,  8,  9,  8,  9, 12, 13, 12, 15, 16],
    #    [ 6,  8,  9, 11, 12, 13, 12, 14, 14, 16],
    #    [ 8,  9, 10, 10, 13, 12, 14, 16, 17, 16],
    #    [ 9,  9, 10, 13, 12, 14, 15, 17, 18, 17],
    #    [11, 10, 13, 14, 14, 14, 17, 16, 19, 20],
    #    [10, 12, 14, 13, 14, 17, 18, 17, 20, 19]]

    #N = 2
    #M = 5
    #A = [[9, 7, 5, 3, 2],
    #     [8, 7, 6, 3, 1]]

    print(solution(N, M, A))
