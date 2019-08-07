
def solution(A):
    best_start = -1
    best_count = 0
    cur_start = -1
    cur_count = 0

    last = 0
    for i, a in enumerate(A, start=1):
        if a == 1:
            if last == 0:
                cur_start = i
                cur_count = 0
            cur_count += 1

            if cur_count > best_count:
                best_count = cur_count
                best_start = cur_start

        last = a

    return best_start

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        A = [*map(int, f.readline().split())]

    print(solution(A))
