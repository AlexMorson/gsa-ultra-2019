def solution(N):
    return int(N*(N-1)/2)

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        N = int(f.readline().strip())

    print(solution(N))
    # 1400301
