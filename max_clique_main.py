import sys
from bruteforce_solver import bruteforce_solve
from approximation_solver import approximation_solve
from original_solver import original_solve
from utils import read_adjacency_matrix, is_clique

def main():
    if len(sys.argv) < 3:
        print("Usage: python max_clique_main.py [solver_type] [filename]")
        return
    
    solver_type = sys.argv[1]
    filename = sys.argv[2]
    adjacency_matrix = read_adjacency_matrix(filename)

    if solver_type == "bruteforce":
        max_clique_nodes = bruteforce_solve(adjacency_matrix)
    elif solver_type == "approximation":
        max_clique_nodes = approximation_solve(adjacency_matrix)
    elif solver_type == "original":
        max_clique_nodes = original_solve(adjacency_matrix)
    else:
        print("Invalid solver type specified.")
        return

    print("Nodes in the Max Clique:", max_clique_nodes)
    print("Number of Nodes in the Max Clique:", len(max_clique_nodes))

    # Verify that the returned nodes indeed form a clique
    if is_clique(max_clique_nodes, adjacency_matrix):
        print("The nodes form a valid clique.")
    else:
        print("The nodes do not form a valid clique.")

if __name__ == "__main__":
    main()


