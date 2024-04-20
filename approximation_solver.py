def vertex_cover_greedy(graph):
    covered = set()
    cover = set()
    edges = [(i, j) for i in range(len(graph)) for j in range(i+1, len(graph)) if graph[i][j] == 1]
    
    while edges:
        edge = edges.pop(0)  # Take an edge
        if edge[0] not in covered and edge[1] not in covered:
            # If neither vertex is covered, add both to the cover
            cover.update(edge)
            covered.update(edge)
    
    return cover

def complement_graph(graph):
    n = len(graph)
    complement = [[1 if i != j and graph[i][j] == 0 else 0 for j in range(n)] for i in range(n)]
    return complement

def approximation_solve(adjacency_matrix):
    # Step 1: Find the vertex cover of the complement graph
    g_prime = complement_graph(adjacency_matrix)
    vertex_cover = vertex_cover_greedy(g_prime)
    
    # Step 2: Compute the independent set in G as the complement of the vertex cover of G'
    maximal_clique = list(set(range(len(adjacency_matrix))) - vertex_cover)
    
    return maximal_clique

