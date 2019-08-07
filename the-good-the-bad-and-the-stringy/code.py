def solution(N, k_1, k_2, X, Y):
    pass

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        N = int(f.readline().strip())
        k_1, k_2 = map(int, f.readline().strip().split())
        X, Y = f.readline().strip().split()

    print(solution(N, k_1, k_2, X, Y))
