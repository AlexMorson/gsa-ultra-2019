import itertools

def find_smallest_string(S):
    if len(S) > 4 and S[0] == "?":
        S = "1" + S[1:]

    start = S[:-3]
    start = start.replace("?", "0")
    S = start + S[-3:]

    poss = []
    for c in S[-3:]:
        if c == "?":
            poss.append([*map(str, range(10))])
        else:
            poss.append([c])

    if S[0] == "?":
        poss[0] = [*map(str, range(1, 10))]

    ends = []
    for s in itertools.product(*poss[-3:]):
        w = "".join(s)
        if int(w) % 8 == 0:
            return start + w
    return None

def solution(S):
    A = find_smallest_string(S)
    if A is None:
        return 1000000007

    res = 0
    mul = 1
    for i, c in enumerate(A, start=1):
        d = int(c)
        res += mul * (d+1)
        mul *= 11
        mul %= 10**9 + 7
    return res % (10**9 + 7)

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        S = f.readline().strip()

    print(solution(S))
    # 1000000007
