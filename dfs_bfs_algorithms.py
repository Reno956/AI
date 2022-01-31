# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:29:22 2020

@author: myriam.hernandez
"""
def printPath(path):
    #Asume que el camino es una lista de nodos
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path)-1:
            result = result + '-->'
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start]
    if toPrint:
        print('Camino DFS actual:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Ya visitado', node)
    return shortest

def BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def shortestPath(graph, start, end, toPrint = False):
    #return DFS(graph, start, end, [], None, toPrint)
    return BFS(graph, start, end, toPrint)

class Node(object):
    def __init__(self, name):
        """Asume que name es un string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Asume que src y dest son nodos"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class Digraph(object):
    """edges está en un diccionario con una lista conectada a sus 
    hijos"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Nodo duplicado')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Nodo no está en el grafo')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omita la nueva línea al final
        
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
                
    
    
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Arad', 'Sibiu', 'Zerind', 'Oradea', 'Rimnicu', 'Timisoara', 'Lugoj', 'Mehadia', 'Dobreta', 'Craiova','Pitesti', 'Fagaras', 'Bucarest'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Arad'), g.getNode('Zerind')))
    g.addEdge(Edge(g.getNode('Arad'), g.getNode('Timisoara')))
    g.addEdge(Edge(g.getNode('Arad'), g.getNode('Sibiu')))
    g.addEdge(Edge(g.getNode('Zerind'), g.getNode('Oradea')))
    g.addEdge(Edge(g.getNode('Timisoara'), g.getNode('Lugoj')))
    g.addEdge(Edge(g.getNode('Lugoj'), g.getNode('Mehadia')))
    g.addEdge(Edge(g.getNode('Mehadia'), g.getNode('Dobreta')))
    g.addEdge(Edge(g.getNode('Dobreta'), g.getNode('Craiova')))
    g.addEdge(Edge(g.getNode('Craiova'), g.getNode('Pitesti')))
    g.addEdge(Edge(g.getNode('Pitesti'), g.getNode('Bucarest')))
    g.addEdge(Edge(g.getNode('Sibiu'), g.getNode('Rimnicu')))
    g.addEdge(Edge(g.getNode('Sibiu'), g.getNode('Fagaras')))
    g.addEdge(Edge(g.getNode('Rimnicu'), g.getNode('Pitesti')))
    g.addEdge(Edge(g.getNode('Fagaras'), g.getNode('Bucarest')))
    return g

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True)
                      
    if sp != None:
        print('Camino más corto desde ', source, 'a',
              destination, 'es', printPath(sp))
    else:
        print('No hay camino desde', source, 'a', destination)
        
testSP('Arad', 'Bucarest')


