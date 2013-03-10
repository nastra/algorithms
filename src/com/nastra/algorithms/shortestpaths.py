'''
@author: nastra - Eduard Tudenhoefner
'''
from com.nastra.algorithms.dijkstra import Dijkstra
import copy

class SingleDestinationShortestPath(object):
    '''
    Finds the shortest path to a given destination in a given graph.
    '''

    def __init__(self):
        pass
    
    def findShortestPath(self, graph, destination):
        '''
        Finding shortest paths to a single destination can be reduced to the problem of finding shortest paths when given
        a single source by reversing the direction of each vertex.
        '''
        reversedGraph = self.__reverseGraph(graph)
        print(reversedGraph)
        dijkstra = Dijkstra()
        shortestPathTo, edgeTo = dijkstra.findShortestPaths(reversedGraph, destination)
        print(shortestPathTo)
        print(edgeTo)
        
    def __reverseGraph(self, graph):
        ''' Reverses the given graph and returns it '''
        reversedGraph = {}
        for key in list(graph.keys()):
            reversedGraph[key] = {}
        
        for nodeTuple in graph.items():
            (node, nodeToDist) = nodeTuple
            for k in nodeToDist.items():
                (n, dist) = k
                reversedGraph[n][node] = dist
                
        return reversedGraph
    
def readGraphFromFile(filename):
    with open(filename) as file:
        graph = {}
        for line in file:
            node = int(line.split()[0])
            nodeToDist = {}
            for inner in line.split()[1:]:
                adjacentNodeToDist = inner.split(",")
                adjacentNode = int(adjacentNodeToDist[0])
                distance = int(adjacentNodeToDist[1])
                nodeToDist[adjacentNode] = distance
            graph[node] = nodeToDist
        return graph

if __name__ == '__main__':
    # graph = readGraphFromFile("dijkstraData.txt") 
    graph = {1: {2: 10, 4: 30, 5: 100}, 2: {3: 50}, 3: {5: 10}, 4: {3: 20, 5: 60}, 5: {}}
    calc = SingleDestinationShortestPath()
    calc.findShortestPath(graph, 5)
    
