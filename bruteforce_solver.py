from itertools import combinations
from utils import is_clique

def bruteforce_solve(adjacency_matrix):
    n = len(adjacency_matrix)
    max_clique = []
    # Generate all possible subsets of vertices
    for r in range(1, n+1):
        for subset in combinations(range(n), r):
            if is_clique(subset, adjacency_matrix):  # imported function
                # update the largest found clique if current is larger
                if len(subset) > len(max_clique):
                    max_clique = subset

    return list(max_clique)  # list of nodes in the max clique


    # adjacency matrix format
    """clique_matrix = [[0]*n for _ in range(n)]
    for i in max_clique:
        for j in max_clique:
            if i != j:
                clique_matrix[i][j] = 1

    return clique_matrix"""
