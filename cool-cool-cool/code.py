def solution(A):
    # Find strictly increasing
    A_inc = []
    last_a = 0
    for a in A:
        new_a = max(last_a+1, a)
        A_inc.append(new_a)
        last_a = new_a

    # Find strictly decreasing
    A_dec = []
    last_a = 0
    for a in A[::-1]:
        new_a = max(last_a+1, a)
        A_dec.append(new_a)
        last_a = new_a

    # Return min
    bitonic = []
    for a, a_inc, a_dec in zip(A, A_inc, A_dec[::-1]):
        bitonic.append(min(a_inc, a_dec))
    
    # Check!
    inc = True
    for i in range(len(bitonic)-1):
        if bitonic[i] == bitonic[i+1]:
            bitonic[i+1] += 1
        if inc:
            if bitonic[i] > bitonic[i+1]:
                inc = False
        else:
            if bitonic[i] < bitonic[i+1]:
                raise Exception("UP AGAIN")

    total = 0
    for a, new_a in zip(A, bitonic):
        total += new_a - a

    return total

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        A = [*map(int, f.readline().strip().split())]

    print(solution(A))
    # 273412501

    def test(A, s):
        t = solution(A)
        if t != s:
            print("Got solution({}) == {} != {}".format(A, t, s))

    test([1, 1], 1)
    test([1, 1, 1], 1)
    test([2, 1, 2], 2)
    test([2, 1, 1], 2)
    test([1, 1, 1, 1], 3)
    test([3, 1, 1, 1], 4)
    test([4, 1, 1, 1], 3)
    test([5, 1, 1, 1], 3)
    test([1, 10, 10, 1], 1)
