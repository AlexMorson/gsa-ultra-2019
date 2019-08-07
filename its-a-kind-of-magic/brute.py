def solution(S, X, Q):
    ans = []
    for L, R in Q:
        total = 0
        for t in range(L, R+1):
            T = str(t)
            magic = 0
            for s, x in zip(S, X):
                sn = len(s)
                for i in range(len(T)-sn+1):
                    if T[i:i+sn] == s:
                        magic += x
            total += magic
        ans.append(total)

    res = 0
    for i in range(len(Q)):
        res += 2**(i+1) * ans[i]
    return res % (10**9 + 7)

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        S = f.readline().strip().split()
        X = [*map(int, f.readline().strip().split())]
        Q = [*map(int, f.readline().strip().split())]
        Q = [*zip(Q, Q[1:])][::2]

    print(solution(S, X, Q))
    # 15980

    def test(S, X, Q, s):
        t = solution(S, X, Q)
        if t != s:
            print("Got solution({}, {}, {}) == {} != {}".format(S, X, Q, t, s))

    S = ["01", "12", "11", "1"]
    X = [10, 100, 1000, 10000]

    test(S, X, [(10, 13)], 2*51100)
