def solution(Z, T, D, N):
    T = T[0] / T[1]
    D = D[0] / D[1]
    def wins(n):
        m = Z
        for i in range(N):
            if i % 2 == 0:
                turned = min(n, int(m * T))
                m += turned
                n -= turned
            else:
                killed = min(m, int(n * D))
                m -= killed

            if m == 0:
                return True
            elif n == 0:
                return False
        return False
    
    n = 1
    while not wins(n):
        n *= 2

    if n == 1:
        return 1

    l = n // 2  # Always lose with n=l
    r = n       # Always win  with n=r
    while l < r-1:
        m = (l + r) // 2
        if wins(m):
            r = m
        else:
            l = m

    return r

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        Z = int(f.readline().strip())
        T = tuple(map(int, f.readline().strip().split()))
        D = tuple(map(int, f.readline().strip().split()))
        N = int(f.readline().strip())

    print(solution(Z, T, D, N))
    # 742443
