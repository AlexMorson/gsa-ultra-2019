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
    with open("downloadable_input.txt", "r") as f:
        N, M = map(int, f.readline().strip().split())
        A = [[*map(int, line.strip().split())] for line in f.readlines()]

    print(solution(N, M, A))
    # 2401
