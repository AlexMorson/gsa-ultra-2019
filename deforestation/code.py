from fractions import Fraction

def solution(T, Q):
    T_n = len(T) + 1

    # Convert into sane indices (sizes will be used as adjacency list)
    sizes = [{} for _ in range(T_n)]
    for u, v in T:
        sizes[u-1][v-1] = None
        sizes[v-1][u-1] = None

    # Compute the size of each section of the tree
    todo = [(True, None, 0)]
    while todo:
        explore, parent, node = todo.pop()

        if explore:
            todo.append((False, parent, node))
            for child in sizes[node]:
                if child != parent:
                    todo.append((True, node, child))
        elif parent is not None:
            node_size = 1
            for child, child_size in sizes[node].items():
                if child != parent:
                    node_size += child_size
            assert sizes[parent][node] is None
            assert sizes[node][parent] is None
            sizes[parent][node] = node_size
            sizes[node][parent] = T_n - node_size

    #print(sizes)

    ways_to_get_size = [0 for _ in range(T_n+1)]
    for node in range(T_n):
        ways_to_get_size[T_n] += 1
        for size in sizes[node].values():
            ways_to_get_size[T_n - size] += size

    assert sum(ways_to_get_size) == T_n*T_n

    def modular_inverse(a):
        m0 = m = 10**9 + 7
        y = 0
        x = 1
        while a > 1:
            q = a // m
            t = m
            m = a % m
            a = t
            t = y
            y = x - q * y
            x = t
        if x < 0:
            x = x + m0
        return x

    def ans(q):
        ways = ways_to_get_size[q]
        prob = Fraction(ways, T_n*T_n)
        A = prob.numerator
        B = prob.denominator
        #A = ways
        #B = T_n*T_n

        print(q)
        print(A, B)

        return (A * modular_inverse(B)) % (10**9 + 7)

    total = 0
    for i, q in enumerate(Q, start=1):
        total += i * ans(q)
    return total % (10**9 + 7)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        T = [*map(int, f.readline().strip().split())]
        T = [*zip(T, T[1:])][::2]

        Q = [*map(int, f.readline().strip().split())]

    #T = [(1,2), (2,3), (3,4), (4,5), (3,6), (6,7)]
    #Q = [*range(8)]

    print(solution(T, Q))
