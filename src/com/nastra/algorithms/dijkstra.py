'''
This class implements Dijkstra's shortest path algorithm in a fast way where an own implementation of a min priority
queue is used. Due to the usage of a min priority queue (which is based on a min binary heap), the running
time of this algorithm is O((V+E) log V), where V represents the number of vertices and E represents the number of edges
in the graph.

@author: nastra - Eduard Tudenhoefner
'''
from com.nastra.data.queue import MinPriorityQueue

class Dijkstra(object):
    def __init__(self):
        self.infinity = 1000000
        self.shortestPathTo = {}
        self.edgeTo = {}
        self.minQueue = MinPriorityQueue()
    
    def __initSingleSource(self, graph, startNode):
        self.shortestPathTo = dict.fromkeys(graph, self.infinity)
        self.edgeTo = dict.fromkeys(graph, None)
        self.shortestPathTo[startNode] = 0
        
    def findShortestPaths(self, graph, startNode):
        self.__initSingleSource(graph, startNode)
        self.minQueue.insert((self.shortestPathTo[startNode], startNode))
        
        while not self.minQueue.empty():
            dist, node = self.minQueue.extractMin()
            self.__relaxation(graph, node)
        return self.shortestPathTo, self.edgeTo
            
    def __relaxation(self, graph, node):
        for adjacentNode in graph[node]:
            edgeDistance = graph[node][adjacentNode]
            overallDistance = self.shortestPathTo[node] + edgeDistance
            if self.shortestPathTo[adjacentNode] > overallDistance:
                self.shortestPathTo[adjacentNode] = overallDistance
                self.edgeTo[adjacentNode] = node
                
                if self.minQueue.contains(adjacentNode):
                    self.minQueue.decreaseKey(self.shortestPathTo[adjacentNode], adjacentNode)
                else:
                    self.minQueue.insert((self.shortestPathTo[adjacentNode], adjacentNode))
        

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
    dijkstra = Dijkstra()
    shortestPathTo, edgeTo = dijkstra.findShortestPaths(graph, 1)
    
    print(shortestPathTo)
    print(edgeTo)
