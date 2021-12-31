import itertools


def tsp(cities, distances):
    n = len(cities)
    opt = [[0 for x in range(n)] for y in range(n)]
    for i in range(1, n):
        opt[i][i] = distances[0][i]
        print(opt[i][i])
    for j in range(2, n):
        subsets = itertools.combinations(range(2, n+1), j)
        for s in subsets:
            print(s)


c = ["c1", "c2", "c3", "c4", "c5"]
d = [[0, 10, 12, 7, 4], [6, 0, 8, 11, 5], [4, 4, 0, 11, 12], [1, 10, 6, 0, 13], [8, 7, 6, 5, 0]]

tsp(c, d)
