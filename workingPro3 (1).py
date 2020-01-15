import math
import timeit
import random

def BFS_connected(graph, s, t):
    #YOU DO
    discovered = [None] * len(graph) 
    toVisitQ = []
    discovered[s] = True
    discovered[t] = False
    
    toVisitQ.append(s)
    
    while toVisitQ:
            i = toVisitQ.pop(0)
            for edge in graph[i]:
                if discovered[t] == False:
                    discovered[t] = True
                    toVisitQ.append(edge)
    return discovered[t]

def DFS_connected(graph, s, t):
    #YOU DO
    discovered = [None] * len(graph)
    toVisitS = []
    discovered[s] = True
    discovered[t] = False
    toVisitS.append(s)
    
    while toVisitS:
        i = toVisitS.pop()
        for edge in graph[i]:
                if discovered[t] == False:
                    discovered[t] = True
                    toVisitS.append(edge)
    return discovered[t]

def adjacency_list(matrix):
    #YOU DO #checks if they are edges
    adList = []
    for i in range(len(matrix)):
        a = 0
        nList = []
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and a != len(matrix):
                nList.append(j)
                j = j + 1
        adList.append(nList)
    return adList


def generate_adjacency_matrix(n):
    """returns a randomly generated graph with n nodes, given as an adjacency list."""
    
    graph = [[-1 for i in range(n)] for i in range(n)]
    for i in range(n):
        graph[i][i] = 0
        for j in range(i+1, n):
            graph[i][j] = random.randint(0,1)
            graph[j][i] = graph[i][j]
    return graph

def test_BFS(graph):
    """runs breadth-first search for every pair of nodes in the graph."""
    
    num_nodes = len(graph)
    for i in range(num_nodes):
        for j in range(num_nodes):
            BFS_connected(graph, i, j)

def test_DFS(graph):
    """runs depth-first seearch for every pair of nodes in the graph."""
    
    num_nodes = len(graph)
    for i in range(num_nodes):
        for j in range(num_nodes):
            DFS_connected(graph, i, j)

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def time_function(func, test_input, iterations = 10):
    """Takes the name of a function and input to time the function on. Optional: can specify how times you want to repeat this call (default 100). Returns the time it takes for the function to run on the given input, repeated the given number of times"""
    
    wrapped = wrapper(func, test_input)
    return timeit.timeit(wrapped, number = iterations)

def time_searches(num_nodes, num_graphs):
    """Takes a number of nodes and a number of graphs, and
    returns the total amount of time to run breadth-first
    and depth-first searches on the given number of randomly
    generated graphs, with the given number of nodes."""
    
    total_BFS = 0
    total_DFS = 0
    
    for i in range(num_graphs):
        graph = adjacency_list(generate_adjacency_matrix(num_nodes))
        total_BFS += time_function(test_BFS,graph)
        total_DFS += time_function(test_DFS,graph)
    return total_BFS, total_DFS
