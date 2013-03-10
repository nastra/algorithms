'''
Finds the shortest path to a given destination in a given graph by reversing the entire graph and applying Dijkstra's algorithm.

@author: nastra - Eduard Tudenhoefner
'''
from com.nastra.algorithms.dijkstra import Dijkstra

class SingleDestinationShortestPath(object):
    def findShortestPath(self, graph, destination):
        '''
        Finding shortest paths to a single destination can be reduced to the problem of finding shortest paths when given
        a single source by reversing the direction of each vertex.
        '''
        reversedGraph = self.__reverseGraph(graph)
        dijkstra = Dijkstra()
        shortestPathToDestination, edgeTo = dijkstra.findShortestPaths(reversedGraph, destination)
        return (shortestPathToDestination, edgeTo)
    
    def __reverseGraph(self, graph):
        ''' 
        Reverses the given graph and returns it 
        '''
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
    shortest = SingleDestinationShortestPath()
    shortestPathToDestination, edges = shortest.findShortestPath(graph, 5)
    print(shortestPathToDestination)
    print(edges)
    
