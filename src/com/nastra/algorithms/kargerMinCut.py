'''
Implements Karger's Random Contraction Algorithm to calculate minimum cuts in a graph. It is possible that this algorithm has to be 
run multiple times to find the minimum cut in a graph.

@author: nastra - Eduard Tudenhoefner
'''
import random
import copy

cuts = []
graph = {}

def kargerMinCut(graph):
    while len(graph) > 2:
        v = random.choice(list(graph.keys()))
        w = random.choice(graph[v])
        contract(graph, v, w)
        
    # Calculating and recording the mincut    
    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)

def contract(graph, v, w):
    for node in graph[w]:  # merge the nodes from w to v
        if node != v:  # we dont want to add self-loops
            graph[v].append(node)
        graph[node].remove(w)  # delete the edges to the absorbed node 'w' and change them to the source node 'v'
        if node != v:
            graph[node].append(v)

    del graph[w]  # delete the absorbed vertex 'w'
    
def readGraphFromFile(filename):
    file = open(filename)
    global graph
    graph = {}
    count = 0
    for line in file:
        node = int(line.split()[0])
        edges = []
        for edge in line.split()[1:]:
            edges.append(int(edge))
        graph[node] = edges
        count += 1
    print(str(len(graph)) + " vertices in dictionary.")
    return graph

if __name__ == '__main__':
    # graph = readGraphFromFile("graph.txt") # read the graph from a text file
    numberOfRepeatedTrials = 10
    graph[1] = [2, 4]
    graph[2] = [1, 3, 4]
    graph[3] = [2, 4]
    graph[4] = [1, 2, 3]
    for i in range(1, numberOfRepeatedTrials):  # we do repeated trials to find the minimum cut.
        copiedGraph = copy.deepcopy(graph)
        kargerMinCut(copiedGraph)
    print("MinCut is " + str(min(cuts)))
    pass
