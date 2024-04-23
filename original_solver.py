import random

def is_clique(clique, graph):
    """Check if all nodes in the set form a clique."""
    for v1 in clique:
        for v2 in clique:
            if v1 != v2 and graph[v1][v2] == 0:
                return False
    return True

def local_search_max_clique(graph, max_iterations=1000):
    n = len(graph)
    current_clique = set([random.randint(0, n-1)])  # Start with a random vertex
    best_clique = current_clique.copy()

    for _ in range(max_iterations):
        if random.random() < 0.5:  # Probability to add a new vertex to the clique
            potential_additions = set(range(n)) - current_clique
            for vertex in potential_additions:
                new_clique = current_clique.copy()
                new_clique.add(vertex)
                if is_clique(new_clique, graph):
                    current_clique = new_clique
                    if len(current_clique) > len(best_clique):
                        best_clique = current_clique.copy()
        else:  # Probability to remove a vertex from the clique
            if len(current_clique) > 1:
                current_clique.remove(random.choice(list(current_clique)))

        # Randomly restart to avoid local maxima
        if random.random() < 0.05:
            current_clique = set([random.randint(0, n-1)])
            if is_clique(current_clique, graph):
                if len(current_clique) > len(best_clique):
                    best_clique = current_clique.copy()

    return list(best_clique)

def original_solve(adjacency_matrix):
    return local_search_max_clique(adjacency_matrix)
