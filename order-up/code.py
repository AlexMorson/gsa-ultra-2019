def solution(C, D):
    C = sorted(C)
    D = sorted(D)
    return sum(min(c, d) for c, d in zip(C, D))

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        C = [*map(int, f.readline().strip().split())]
        D = [*map(int, f.readline().strip().split())]

    print(solution(C, D))
    # 1524471

    def test(C, D, s):
        t = solution(C, D)
        if t != s:
            print("Got solution({}, {}) == {} != {}".format(C, D, t, s))

    import itertools
    def brute_force(C, D):
        best = 0
        for perm in itertools.permutations(D):
            eaten = 0
            for c, d in zip(C, perm):
                eaten += min(c, d)
            if eaten > best:
                best = eaten
        return best

    import random
    size = 8
    for _ in range(100):
        C = random.sample(range(100), size)
        D = random.sample(range(100), size)

        sol = brute_force(C, D)
        test(C, D, sol)
    print("Tests passed")
