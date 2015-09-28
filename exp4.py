'''
Experiments with breadth first search and Prim's Minimum Spanning Tree on graphs.

Note that this program needs an external text file to run. This code has been uploaded for viewing purposes only.

The way I implemented my BFS and PrimMST require that the vertices be strings, as opposed to integers (although
I do work with integers to create the actual graphs!)
I think this makes more sense in the context of the assignment, anyway.
'''

from collections import defaultdict
from collections import deque
import random
from heapq import *



########################################################
# Testing the algorithms on the graph given on the assignment
print "INITIAL TESTING OF GRAPH GIVEN ON ASSIGNMENT\n"

def breadthFirstSearch(graph, start):
        queue = []
        visited = []
        totalWeight = 0
        visited.append(start)
        queue.append(start)

        while len(queue) > 0:
            v = queue[0]
            del queue[0]
            for i in graph[v]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                    totalWeight += graph[v][i]
        print "The BFS Tree is:", visited, "with total weight", totalWeight;
        return totalWeight
                
def primMST(vertices, edges):
    connected = defaultdict(list)
    for v1, v2, c in edges:
        connected[v1].append((c,v1,v2))
        connected[v2].append((c,v2,v1))

    MST = []
    totalWeight = 0
    visited = set(vertices[0])
    unvisited = connected[vertices[0]][:]
    heapify(unvisited)

    while unvisited:
        weight, v1, v2 = heappop(unvisited)
        if v2 not in visited:
            visited.add(v2)
            MST.append((v1, v2, weight))
            totalWeight += weight

            for edge in connected[v2]:
                if edge[2] not in visited:
                    heappush(unvisited, edge)
    print "The Prim Tree is", MST, "with total weight", totalWeight;
    return totalWeight
    

# To be used with Prim
vertices = list("ABCDEF")
edge1 = [("A","B",15), ("F", "C", 7), ("A","D",7), ("A","E",10),
         ("B","C",9),("B","D",11),("B","F",9),
         ("C", "B", 9),("C","E",12), ("C","F",7),
         ("D","A",7), ("B", "A", 15),("D","E",8),("D","F",14),
         ("E", "A", 10), ("E","C",12),("E","D",8),("E","F",8),("D", "B", 11),
         ("F","B",9),  ("F","E",8)]
# To be used with BFS
graph = {'A':{'B':15, 'D':7, 'E':10},
         'B':{'A':15,'C':9, 'D':11, 'F':9},
         'C':{'B':9, 'E':12, 'F':7},
         'D':{'A':7, 'B':11, 'E':8, 'F':14},
         'E':{'A':10, 'C':12, 'D':8, 'F':8},
         'F':{'B':9, 'C':7,'D':14,'E':8}
        }

primMST(vertices, edge1)
breadthFirstSearch(graph, 'A')
print "\n"
class vertex(object):
    def __init__(self, value):
        self.id = value
        self.neighbours = []
        
    def newNeighbour(self, friend):
        self.neighbours.append(friend)

class graph(object):
    def __init__(self):
        self.numVertices = 0
        self.vertices = []
        
    def newVertex(self):
        self.vertices.append(vertex(self.numVertices))
        self.numVertices += 1
        
    def newEdge(self, x, y):
        self.vertices[x].newNeighbour(y)
        self.vertices[y].newNeighbour(x)

    def addWeight(self, x, y):
        weight = random.randint(10,100)
        return weight

    def isEdge(self, x, y):
        return y in self.vertices[x].neighbours
    
    def getWeight(self, x, y):
        weight = addWeight(self, x, y)
        return weight
    
    def neighbours(self):
        for i in range(self.numVertices):
            print i, self.vertices[i].neighbours

    def breadthFirstSearch(self, graph, start):
        #standard algorithm given in Professor Dawes' notes
        queue = []
        visited = []
        totalWeight = 0
        visited.append(start)
        queue.append(start)

        while len(queue) > 0:
            v = queue[0]
            del queue[0]
            for i in graph[v]: # goes through the list of v's neighbours
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                    totalWeight += graph[v][i]
        return totalWeight
                
    def primMST(self, vertices, edges):
        connected = defaultdict(list) # creates a dictionary to contain vertices
        for v1, v2, c in edges:
            connected[v1].append((c,v1,v2))
            connected[v2].append((c,v2,v1))

        MST = []
        totalWeight = 0
        visited = set(vertices[0]) #selects the first vertex
        unvisited = connected[vertices[0]][:]
        heapify(unvisited) #creates a heap out of the vertices yet to be visited

        while unvisited:
            weight, v1, v2 = heappop(unvisited) #gets the next unvisited vertex
            if v2 not in visited:
                visited.add(v2)
                MST.append((v1, v2, weight))
                totalWeight += weight

                for edge in connected[v2]:
                    if edge[2] not in visited:
                        heappush(unvisited, edge) # adds the next potential edge to the heap
        return totalWeight
    
#EXPERIMENT, n = 100
print "EXPERIMENT"
n = 100
lis = []
f = open('top_secret_agent_aliases_2015.txt', 'r')
aliases = f.readlines()
for line in range(n):
    lis.append(aliases[line].rstrip('\n'))

lis = sorted(lis) # agents are now sorted alphabetically
for trials in range(n):
    G = graph()
    G.newVertex()
    temp = []
    edges = []
    adjList = {}
    nbrList = {}
    tempDict = {}
    bfsPrimRatio = 0
    averages = 0
    ratio = 0
    for i in range(1, n): #works with the index of an agent opposed to their alias
        agentIndex = i
        G.newVertex()
        neighbour = random.randint(0, agentIndex-1)
        G.newEdge(agentIndex, neighbour)
        weight = G.addWeight(agentIndex, neighbour)
        temp.append([lis[agentIndex], lis[neighbour], weight]) # ['agent1', 'agent2', weight]

    # converts the graph so that I can call primMST on it
    # This needs to happen because primMST needs the graph to be a list of tuples
    # Each tuple contains an agent, its neighbour, and the weight between them
    for i in temp:
        tupleSet = tuple(i)
        edges.append(tupleSet)
        
    # converts the graph again so that I can call BFS on it
    for agent in lis:
        tempDict.clear()
        adjList.update({agent:{}})
        for i in temp: # for each agent in the graph
            '''
            The format BFS requires looks like this: {agent1: {nbr1:weight1, nbr2:weight2}, agent2: {nbr1:weight1,...}}
            So I need a dictionary (adjList) of all the agents and their neighbours and weights, and a
            dictionary for each list of neighbours. This is accomplished by looping through the graph,
            adding each neighbour of a particular agent to a temporary dictionary, and then copying
            the temporary dictionary to the agent's nbrList. Then I clear the tempDict when I move on to the next agent.
            '''
            if i[0] == agent:
                tempDict[i[1]] = i[2]
            elif i[1] == agent:
                tempDict[i[0]] = i[2]
            nbrList = tempDict.copy()
            adjList.update({agent:nbrList})
    #Since the list of agents is sorted, primMST will always start at Agent Beetles.
    #BFS needs to start at Agent Beetles too
    bfs = G.breadthFirstSearch(adjList, 'beetles')
    prim = G.primMST(lis, edges)
    bfsPrimRatio = float(prim)/bfs
    averages += bfsPrimRatio
ratio = averages/n
print "The average ratio for n =", n, "is", ratio;


########################################################
# N = 200
n = 200
lis = []
f = open('top_secret_agent_aliases_2015.txt', 'r')
aliases = f.readlines()
for line in range(n):
    lis.append(aliases[line].rstrip('\n'))
lis = sorted(lis)
for trials in range(n):
    G = graph()
    G.newVertex()
    temp = []
    edges = []
    adjList = {}
    nbrList = {}
    tempDict = {}
    bfsPrimRatio = 0
    averages = 0
    ratio = 0
    for i in range(1, n):
        agentIndex = i
        G.newVertex()
        neighbour = random.randint(0, agentIndex-1)
        G.newEdge(agentIndex, neighbour)
        weight = G.addWeight(agentIndex, neighbour)
        temp.append([lis[agentIndex], lis[neighbour], weight])

    for i in temp:
        tupleSet = tuple(i)
        edges.append(tupleSet)

    for agent in lis:
        tempDict.clear()
        adjList.update({agent:{}})
        for i in temp:
            if i[0] == agent:
                tempDict[i[1]] = i[2]
            elif i[1] == agent:
                tempDict[i[0]] = i[2]
            nbrList = tempDict.copy()
            adjList.update({agent:nbrList})
            
    randomVertex = random.sample(adjList, 1)
    bfs = G.breadthFirstSearch(adjList, 'beetles')
    prim = G.primMST(lis, edges)
    bfsPrimRatio = float(prim)/bfs
    averages += bfsPrimRatio
ratio = averages/n
print "The average ratio for n =", n, "is", ratio;

#####################################################
# N = 300
n = 300
lis = []
f = open('top_secret_agent_aliases_2015.txt', 'r')
aliases = f.readlines()
for line in range(n):
    lis.append(aliases[line].rstrip('\n'))

lis = sorted(lis)
for trials in range(n):
    G = graph()
    G.newVertex()
    temp = []
    edges = []
    adjList = {}
    nbrList = {}
    tempDict = {}
    bfsPrimRatio = 0
    averages = 0
    ratio = 0
    for i in range(1, n):
        agentIndex = i
        G.newVertex()
        neighbour = random.randint(0, agentIndex-1)
        G.newEdge(agentIndex, neighbour)
        weight = G.addWeight(agentIndex, neighbour)
        temp.append([lis[agentIndex], lis[neighbour], weight])

    for i in temp:
        tupleSet = tuple(i)
        edges.append(tupleSet)

    for agent in lis:
        tempDict.clear()
        adjList.update({agent:{}})
        for i in temp:
            if i[0] == agent:
                tempDict[i[1]] = i[2]
            elif i[1] == agent:
                tempDict[i[0]] = i[2]
            nbrList = tempDict.copy()
            adjList.update({agent:nbrList})
            
    randomVertex = random.sample(adjList, 1)
    bfs = G.breadthFirstSearch(adjList, 'beetles')
    prim = G.primMST(lis, edges)
    bfsPrimRatio = float(prim)/bfs
    averages += bfsPrimRatio
ratio = averages/n
print "The average ratio for n =", n, "is", ratio;


########################################################
# N = 400
n = 400
lis = []
f = open('top_secret_agent_aliases_2015.txt', 'r')
aliases = f.readlines()
for line in range(n):
    lis.append(aliases[line].rstrip('\n'))
lis = sorted(lis)

for trials in range(n):
    G = graph()
    G.newVertex()
    temp = []
    edges = []
    adjList = {}
    nbrList = {}
    tempDict = {}
    bfsPrimRatio = 0
    averages = 0
    ratio = 0
    for i in range(1, n):
        agentIndex = i
        G.newVertex()
        neighbour = random.randint(0, agentIndex-1)
        G.newEdge(agentIndex, neighbour)
        weight = G.addWeight(agentIndex, neighbour)
        temp.append([lis[agentIndex], lis[neighbour], weight])

    for i in temp:
        tupleSet = tuple(i)
        edges.append(tupleSet)

    for agent in lis:
        tempDict.clear()
        adjList.update({agent:{}})
        for i in temp:
            if i[0] == agent:
                tempDict[i[1]] = i[2]
            elif i[1] == agent:
                tempDict[i[0]] = i[2]
            nbrList = tempDict.copy()
            adjList.update({agent:nbrList})
            
    randomVertex = random.sample(adjList, 1)
    bfs = G.breadthFirstSearch(adjList, 'beetles')
    prim = G.primMST(lis, edges)
    bfsPrimRatio = float(prim)/bfs
    averages += bfsPrimRatio
ratio = averages/n
print "The average ratio for n =", n, "is", ratio;


############################################################
# N = 500
n = 500
lis = []
f = open('top_secret_agent_aliases_2015.txt', 'r')
aliases = f.readlines()
for line in range(n):
    lis.append(aliases[line].rstrip('\n'))
lis = sorted(lis)
    
for trials in range(n):
    G = graph()
    G.newVertex()
    temp = []
    edges = []
    adjList = {}
    nbrList = {}
    tempDict = {}
    bfsPrimRatio = 0
    averages = 0
    ratio = 0
    for i in range(1, n):
        agentIndex = i
        G.newVertex()
        neighbour = random.randint(0, agentIndex-1)
        G.newEdge(agentIndex, neighbour)
        weight = G.addWeight(agentIndex, neighbour)
        temp.append([lis[agentIndex], lis[neighbour], weight])

    for i in temp:
        tupleSet = tuple(i)
        edges.append(tupleSet)

    for agent in lis:
        tempDict.clear()
        adjList.update({agent:{}})
        for i in temp:
            if i[0] == agent:
                tempDict[i[1]] = i[2]
            elif i[1] == agent:
                tempDict[i[0]] = i[2]
            nbrList = tempDict.copy()
            adjList.update({agent:nbrList})
            
    randomVertex = random.sample(adjList, 1)
    bfs = G.breadthFirstSearch(adjList, 'beetles')
    prim = G.primMST(lis, edges)
    bfsPrimRatio = float(prim)/bfs
    averages += bfsPrimRatio
ratio = averages/n
print "The average ratio for n =", n, "is", ratio;
