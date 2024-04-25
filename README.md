# Algorithms for Solving Max Clique Problem

## Introduction
The **Max Clique Problem** involves finding the largest clique (a subset of vertices such that every two vertices are adjacent) within a given graph. This problem is NP-Hard, meaning there is no known polynomial-time solution.

## Solutions Implemented
Three approaches to the Max Clique problem are implemented in this repository:

### 1. Bruteforce
The bruteforce solution examines all possible combinations of vertices to find the largest subset that forms a clique. This method finds the max clique but is computationally expensive.

### 2. Reduction/Approximation
This approach uses a reduction strategy combined with a greedy vertex-cover approximation algorithm. It doesn't guarantee the largest clique and ouputs terrible cliques.

### 3. Local Search + Dynamic Heuristics
The local search algorithm starts with a random vertex and adjusts its strategy based on the graph's density. It iteratively attempts to expand or shrink the current solution through a dynamic set of heuristics, which include probabilities for vertex addition, removal, and periodic restarts. Results still vary greatly with each run. Adjustments to probabilities are made based on the progress of the search.

## Prerequisites
Before you can run the algorithms provided in this repository, you must have Python installed on your computer.

### Installing Python

If you do not have Python installed, you can download it from the official Python website:

[Download Python](https://www.python.org/downloads/)

## Installation / Build
Clone or dowlnoad the repository to your local machine:
 ```
 git clone https://github.com/MichalZaj/Max_Clique.git
 cd Max_Clique
 ```
 Ensure you have Python installed, then install the required dependencies:
 ```
pip install -r requirements.txt
```
## Input Specifics
The input graph must be provided in a specific adjacency matrix format where each line represents a node and its edges to other nodes. The format is as follows:
```
0
1 0
2 1 0
3 1 1 1
```
- The first character on each line is the node index.
- The subsequent numbers on the line represent the adjacency of this node with earlier nodes, where `1` indicates an edge is present, and `0` indicates no edge.


## Usage
To run the solution, use the following command in the terminal:
```
python max_clique_main.py [solver_type] [filename]
```
Where `solver_type` can be `bruteforce`, `approximation`, or `original`, and `filename` is the path to the graph data file.
## Repository Layout
- **Graphs/**: Folder containing sample graph data files in adjacency matrix format.
- **approximation_solver.py**: Implements the reduction/approximation algorithm.
- **bruteforce_solver.py**: Contains the brute-force solution to find the max clique.
- **max_clique_main.py**: Runs the specified algorithm on provided graph data.
- **original_solver.py**: Contains the Local Search + Dynamic Heuristics algorithm.
- **requirements.txt**: Lists all Python libraries required to run the scripts.
- **utils.py**: Utility functions 

### Utils.py Functions
- **read_adjacency_matrix(filename)**: Reads a graph from a file and converts it into an adjacency matrix format.
- **is_clique(nodes, graph)**: Checks if a given set of nodes forms a clique in the graph.
- **calculate_density(graph)**: Calculates the density of the graph by determining the ratio of actual edges to the total possible edges.

