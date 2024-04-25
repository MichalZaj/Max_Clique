import random
from tqdm import tqdm
from utils import is_clique

def expand_clique(current_clique, graph):
    n = len(graph)  
    potential_additions = set(range(n)) - current_clique  # Find vertices not yet in the clique
    best_clique = current_clique.copy()  
    for vertex in potential_additions:
        new_clique = current_clique.copy()  # Create a copy of the current clique
        new_clique.add(vertex)  # Attempt to add a new vertex
        if is_clique(list(new_clique), graph):  # Check if the new set is still a clique
            if len(new_clique) > len(best_clique):  # Check if the new clique is larger
                best_clique = new_clique.copy()  # Update
    return best_clique 

def local_search(graph, density, max_iterations=1000):
    n = len(graph)
    current_clique = set([random.randint(0, n-1)])
    best_clique = current_clique.copy()
    
    add_prob = 0.7 if density > 0.5 else 0.3  # More aggressive expansion in dense graphs
    remove_prob = 0.2 if density > 0.5 else 0.7  # More pruning in sparse graphs
    restart_prob = 0.01 if density > 0.5 else 0.1  # Less frequent restarts in dense graphs, more in sparse

    iterations_without_improvement = 0
    max_iterations_without_improvement = 50  # Threshold can be adjusted

    # Use tqdm for the loop to show a progress bar
    for iteration in tqdm(range(max_iterations), desc="Searching for Max Clique"):
        improved = False
        # Check if adding a vertex based on add probability
        if random.random() < add_prob: 
            current_clique = expand_clique(current_clique, graph)
            if len(current_clique) > len(best_clique):
                best_clique = current_clique.copy()
                improved = True
        # Check if removing a vertex based on remove probability
        elif random.random() < remove_prob:
            if len(current_clique) > 1:
                current_clique.remove(random.choice(list(current_clique))) # Randomly remove a vertex
         # Check if restarting the search based on restart probability
        if random.random() < restart_prob:
            new_start = set([random.randint(0, n-1)])
            if is_clique(list(new_start), graph):
                current_clique = new_start
                if len(current_clique) > len(best_clique):
                    best_clique = current_clique.copy()
                    improved = True

        if not improved:
            iterations_without_improvement += 1
        else:
            iterations_without_improvement = 0

        # Adjustments based on the lack of improvements
        if iterations_without_improvement >= max_iterations_without_improvement:
            restart_prob += 0.05  # Incrementally increase the restart probability
            iterations_without_improvement = 0  # Reset the counter after adjustment
            if restart_prob > 0.5:  # Keep the restart probability within reasonable limits
                restart_prob = 0.5

    return list(best_clique)

def original_solve(adjacency_matrix, density):
    return local_search(adjacency_matrix, density)
