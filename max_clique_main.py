import sys
from bruteforce_solver import bruteforce_solve
#from approximation_solver import approximation_solve
#from original_solver import original_solve
from utils import read_adjacency_matrix  # Import the utility function

def main():
    if len(sys.argv) < 3:
        print("Usage: python max_clique_main.py [solver_type] [filename]")
        return
    
    solver_type = sys.argv[1]
    filename = sys.argv[2]
    # Read the adjacency matrix from the file
    adjacency_matrix = read_adjacency_matrix(filename)

    if solver_type == "bruteforce":
        max_clique_nodes = bruteforce_solve(adjacency_matrix)
        print("Nodes in the Max Clique:", max_clique_nodes)
    elif solver_type == "approximation":
        print("approximation")
        #approximation_solve(adjacency_matrix)
    elif solver_type == "original":
        print("original")
        #original_solve(adjacency_matrix)
    else:
        print("Invalid solver type specified.")

if __name__ == "__main__":
    main()

