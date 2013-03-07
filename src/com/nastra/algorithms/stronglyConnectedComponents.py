'''
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph. 

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0".

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.

@author: nastra - Eduard Tudenhoefner
'''

import collections
class KosarajuSharirSCC(object):
    def __init__(self):
        self.visited = {}
        self.leaderOf = {}
        self.leaderNode = None
        self.leaders = []
        self.finishingTime = 0
        self.graph = {}
        self.reversedGraph = {}
        self.finishingTimeOf = {}
        self.componentSizes = {}
        self.nodes = 0
        
    def __init(self):
        for i in range(1, self.nodes + 1):
            self.visited[i] = False 
            self.leaderOf[i] = -1
            self.finishingTimeOf[i] = 0
        
    def __reset(self):
        for i in range(1, self.nodes + 1):
            self.visited[i] = False 
        self.leaders = []  # reset the leaders from the first run
        self.componentSizes = {}
        
        
    def findStronglyConnectedComponents(self, graph):
        self.__init()
        self.__findSCCs(self.reversedGraph)  # perform the 1st run on the reversed graph
        self.__reset()
        finishingTimesGraph = self.__createGraphFromFinishingTimes(graph)
        # perform the 2nd run on the original graph where the nodes are named according 
        # to their finishing times from the 1st run
        self.__findSCCs(finishingTimesGraph)  
        return self.leaders, self.componentSizes  # each strongly connected component has a single leader
        
    def __findSCCs(self, graph):
        self.finishingTime = 0
        self.leaderNode = None
        
        for i in range(self.nodes, 0, -1):
            if not self.visited[i]:
                self.leaderNode = i
                self.leaders.append(i)
                self.__depthFirstSearch(graph, i)
                self.componentSizes[self.leaderNode] = 1
            else:
                self.componentSizes[self.leaderOf[i]] += 1
            
        
    def __depthFirstSearch(self, graph, node):
        self.visited[node] = True
        self.leaderOf[node] = self.leaderNode
        for adjacentNode in graph[node]:
            if not self.visited[adjacentNode]:
                self.__depthFirstSearch(graph, adjacentNode)
        self.finishingTime += 1
        self.finishingTimeOf[node] = self.finishingTime
        
    def __reverseGraph(self, graph):
        ''' Reverses the given graph and returns it '''
        reversedGraph = {}
        for key in list(graph.keys()):
            reversedGraph[key] = []
        for key in list(graph.keys()):
            for edge in graph[key]:
                reversedGraph[edge].append(key)
        return reversedGraph

    def __createGraphFromFinishingTimes(self, graph):
        result = collections.defaultdict(list)
        for key in range(1, self.nodes + 1):
            for edge in graph[key]:
                result[self.finishingTimeOf[key]].append(self.finishingTimeOf[edge])
        return result
    
    def getFiveMostLargestSCCs(self):
        return sorted(self.leaders, reverse=True)[0:5]
    
    def getFiveMostLargestSCCCounts(self):
        elements = []
        for element in list(self.componentSizes.keys()):
            elements.append(self.componentSizes[element])
        return sorted(elements, reverse=True)[0:5]
            
    def readGraphFromFile(self, filename):
        with open(filename) as file:
            global graph
            graph = collections.defaultdict(list)
            reversedGraph = collections.defaultdict(list)
            lastVertex = 0
            for line in file:
                node = int(line.split()[0])
                edge = int(line.split()[1])
                graph[node].append(edge)
                reversedGraph[edge].append(node)
                lastVertex = node
            self.nodes = lastVertex
            print(str(self.nodes) + " vertices in dictionary.")
            print("--"*50)
            return graph, reversedGraph
    
    
if __name__ == '__main__':
    import sys
    import time
    sys.setrecursionlimit(547483647)
    sccFinder = KosarajuSharirSCC()
    start = time.time()
    graph, revGraph = sccFinder.readGraphFromFile("SCC.txt")
    end = time.time()
    print("Reading graph from file took: " + str(end - start))
    print("--"*50)
    sccFinder.reversedGraph = revGraph
    start = time.time()
    leaders, sccSizes = sccFinder.findStronglyConnectedComponents(graph)
    end = time.time()
    print("Total time required: " + str(end - start))
    fiveLargestLeaders = sccFinder.getFiveMostLargestSCCs()
    fiveLargestComponents = sccFinder.getFiveMostLargestSCCCounts()
    print("All leaders of the SCCs:")
    print(leaders)
    print(sccSizes)
    print(fiveLargestComponents)
    print("--"*50)
    print("The five largest leaders are: ")
    print(fiveLargestLeaders)
    print("--"*50)
    pass
        
        
