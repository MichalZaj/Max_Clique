def read_adjacency_matrix(filename):
    with open(filename, 'r') as file:
        adjacency_matrix = []
        # First, read all rows as they are into the matrix
        for line in file:
            # Ignore the node index, convert the rest to integers
            parts = line.strip().split()
            row = list(map(int, parts[1:]))  # Convert parts to integers
            adjacency_matrix.append(row)
    
    # Determine the total number of nodes, which should be equal to the number of rows
    n = len(adjacency_matrix)

    # Extend each row to full length by appending zeros where necessary
    for i in range(n):
        adjacency_matrix[i].extend([0] * (n - len(adjacency_matrix[i])))

    # Mirror the lower triangular part to the upper part
    for i in range(n):
        for j in range(i + 1, n):
            adjacency_matrix[i][j] = adjacency_matrix[j][i]

    return adjacency_matrix



