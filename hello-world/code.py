def solution(a, b):
    return a + b

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        a = int(f.readline().strip())
        b = int(f.readline().strip())

    print(solution(a, b))
