def solution(A):
    pass

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        A = [*map(int, f.readline().strip().split())]

    print(solution(A))
