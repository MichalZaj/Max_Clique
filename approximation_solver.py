def vertex_cover_greedy(graph):
    n = len(graph)
    E_prime = []

    # Iterate over each node in the graph
    for i in range(n):
        for j in range(i + 1, n):
            # if there is an edge between nodes i and j, add it to the list
            if graph[i][j] == 1:
                E_prime.append((i, j))

    vertex_cover = set()

    while E_prime:
        u, v = E_prime.pop(0)  # take an edge
        vertex_cover.update([u, v])  # add both u and v to the vertex cover

        remaining_edges = []

        # loop through each edge
        for e in E_prime:
            # check if either vertex of the edge matches u or v
            if e[0] != u and e[0] != v and e[1] != u and e[1] != v:
                remaining_edges.append(e)  # Keep the edge if it's not incident to u or v

        # Update E_prime with the list of remaining edges
        E_prime = remaining_edges

    return vertex_cover

def complement_graph(graph):
    n = len(graph)  # size of graph
    complement = []  

    # Iterate over each row in the graph
    for i in range(n):
        complement_row = []
        for j in range(n):
            # check if there is no edge between node i and node j and i is not equal to j
            if i != j and graph[i][j] == 0:
                complement_row.append(1)  # add an edge in the complement
            else:
                complement_row.append(0)  # Either there is an edge, or it's the same node
        complement.append(complement_row)  # Add to the complement graph

    return complement

def approximation_solve(adjacency_matrix):
    # Step 1: Find the vertex cover of the complement graph
    g_prime = complement_graph(adjacency_matrix)
    vertex_cover = vertex_cover_greedy(g_prime)
    
    # Step 2: Compute all vertices of the graph
    all_vertices = set(range(len(adjacency_matrix)))
    
    # Step 3: Determine the max clique by finding the complement of the vertex cover
    # V - VC = MC
    max_clique = list(all_vertices - vertex_cover)
    
    return max_clique



