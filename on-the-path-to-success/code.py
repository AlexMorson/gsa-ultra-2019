def solution(P, V):

    # Renumber nodes from 0 to N-1
    N = len(V)
    neighbours = [set()] + [{parent-1} for parent in P]
    for node, parent in enumerate(P, start=1):
        neighbours[parent-1].add(node)

    # Precompute scores
    scores = [sum(map(int, "{:b}".format(x))) for x in range(256)]

    # Do BFS from each node, stopping once value is 0
    f = [0 for _ in range(9)]
    for start in range(N):
        seen = {start}
        todo = {(V[start], start)}
        f[scores[V[start]]] += 2
        while todo:
            value, node = todo.pop()
            for new_node in neighbours[node]:
                if new_node not in seen:
                    new_value = value & V[new_node]
                    if new_value != 0:
                        f[scores[new_value]] += 1
                        seen.add(new_node)
                        todo.add((new_value, new_node))
        f[0] += N - len(seen)

    # We have counted every path twice
    f = [n//2 for n in f]
    total = 0
    for i in range(9):
        total += f[i] * 2**i
    return total % (10**9 + 7)

if __name__ == "__main__":
    with open("downloadable_input.txt", "r") as f:
        P = [*map(int, f.readline().strip().split())]
        V = [*map(int, f.readline().strip().split())]

    print(solution(P, V))
    # 1213321
