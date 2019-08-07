def occurrences(s, L, R):
    def _occurrences(s, L, R):
        if s == "":
            return 0, False, False

        s_int = int(s) # Be aware that s may contain leading 0s

        p = 10**len(s)

        if p // 10 > R:
            return 0, False, False

        R_beg = R // p
        R_end = R % p

        # No leading 0s in string representation of j
        upped = False
        if L < p // 10:
            upped = True
            L = p // 10

        L_beg = L // p
        L_end = L % p

        count = R_beg - L_beg

        if L_end > s_int:
            count -= 1
        if R_end >= s_int:
            count += 1

        next_count, start_s, end_s = _occurrences(s, L // 10, R // 10)
        next_count *= 10
        if start_s:
            next_count -= L_end % 10
        if end_s:
            next_count -= 9 - R_end % 10

        return count + next_count, (L_end == s_int and not upped) or start_s, R_end == s_int or end_s

    return _occurrences(s, L, R)[0]

def solution(S, X, Q):
    ans = []
    for L, R in Q:
        total = 0
        for s, x in zip(S, X):
            total += x * occurrences(s, L, R)
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

    assert occurrences("5", 2, 4) == 0
    assert occurrences("5", 2, 5) == 1
    assert occurrences("5", 5, 5) == 1
    assert occurrences("5", 5, 6) == 1
    assert occurrences("5", 4, 6) == 1
    assert occurrences("5", 6, 7) == 0
    assert occurrences("5", 6, 14) == 0
    assert occurrences("5", 5, 15) == 2
    assert occurrences("5", 6, 15) == 1
    assert occurrences("5", 1, 49) == 5

    assert occurrences("05", 1, 200) == 1

    assert occurrences("5", 49, 50) == 1
    assert occurrences("5", 59, 60) == 1
    assert occurrences("5", 52, 57) == 7
    assert occurrences("5", 42, 57) == 10
    assert occurrences("5", 42, 67) == 13

    assert occurrences("5", 492, 512) == 15
    assert occurrences("5", 499, 512) == 14

    assert occurrences("5", 4999, 5021) == 24

    assert occurrences("25", 25, 26) == 1
    assert occurrences("25", 221, 261) == 11
    assert occurrences("25", 221, 257) == 9

    assert occurrences("22", 221, 229) == 10

    assert occurrences("1", 2, 92) == 19
    assert occurrences("1", 2, 100) == 20

    import random
    x = solution([str(random.randint(1, 10000000000000000)) for i in range(3000)], [i for i in range(3000)], [(i, i+10000000000000) for i in range(3000)])
