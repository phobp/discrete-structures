#!/usr/bin/python
# This is a comment line in Python

#
# The following lines must appear at the beginning for graph drawing to work
# Do not touch them
import matplotlib
matplotlib.use('Agg')

# The following line imports networkx so that your program can use it
import networkx as nx

# The following line imports Matplotlib so that you can draw a graph
import pylab as plt

# The following is needed to take arguments from command line
import sys

#
# The following defines a function
#
def operateGraph (inG, inPngFilename1, inPngFilename2, inPngFilename3, inPngFilename4, inGraphFilename):
    # The following line adds a node a to the graph
    inG.add_node ('a')

    # This will add an edge (a, b) with weight 0.1
    # It automatically adds node b too
    inG.add_edge('a', 'b', weight=0.1)

    # This will add an edge (b, c) with weight 1.5
    inG.add_edge('b', 'c', weight=1.5)

    # This will add an edge (a, c) with weight 1.0
    inG.add_edge('a', 'c', weight=1.0)

    # This will add an edge (c, d) with weight 2.2
    inG.add_edge('c', 'd', weight=2.2)

    # This will add an edge (e, f) with weight 10
    # It automatically adds nodes e & f too
    inG.add_edge('e', 'f', weight=10)

    # The following line prints all existing nodes in graph inG
    print ("List of nodes: " + str(inG.nodes()))
    # The following line prints all edges nodes in graph inG
    print ("List of edges: " + str(inG.edges()))

    # The following line prints every node and its degree
    for node in inG.nodes(): 
        print ("Node " + node + ": degree = " + str(inG.degree(node)))

    # The following line draws graph g
    nx.draw_networkx(inG)
    plt.show()
    # The following line saves graph as picture to inPngFilename1
    plt.savefig(inPngFilename1)
    # The following line clears the old graph
    plt.clf()

    # The following line removes edge (e, f) from graph inG
    inG.remove_edge ('e', 'f')

    # The following line draws graph g
    pos = nx.spring_layout(inG)
    nx.draw_networkx(inG, pos)
    labels = nx.get_edge_attributes(inG, 'weight')
    nx.draw_networkx_edge_labels(inG, pos, edge_labels=labels)
    # The following line saves graph as picture to inPngFilename2
    plt.savefig(inPngFilename2)
    plt.clf()

    inG.remove_node ('e')
    inG.remove_node ('f')
    # The following line draws graph inG
    nx.draw_networkx(inG)
    # The following line saves graph as picture to inPngFilename3
    plt.savefig(inPngFilename3)
    plt.clf()

    # The following line prints all existing nodes in graph inG
    print ("Nodes after removing: " + str(inG.nodes()))

    # The following line prints all existing nodes in graph inG
    print ("Edges after removing: " + str(inG.nodes()))

    # The networkx library implements a lot of graph algorithms
    # such as finding the shortest path between two nodes
    #
    print ("Shortest path between b and d = " + str(nx.shortest_path(inG, 'b', 'd')))

    print ("Shortest path between b and d in terms of weight = " + str(nx.shortest_path(inG, 'b', 'd', weight='weight')))

    # The following lines show how to save a graph to a file and read a graph from a file
    #
    nx.write_graphml(inG, inGraphFilename)

    localG = nx.read_graphml (inGraphFilename)
    # The following line prints all existing nodes in graph localG
    print ("Nodes of the graph from a saved file: " + str(localG.nodes()))

    # The following line prints all existing nodes in graph localG
    print ("Edges of the graph from a saved file: " + str(localG.nodes()))

    pos2 = nx.spring_layout(localG)
    nx.draw_networkx(localG, pos2)
    labels2 = nx.get_edge_attributes(localG,'weight')
    nx.draw_networkx_edge_labels(localG, pos2, edge_labels=labels2)
    # The following line saves graph as picture to inPngFilename4
    plt.savefig(inPngFilename4)
    plt.clf()

def main():
    numOfArgs = len(sys.argv)
    if numOfArgs == 1:
        print ("Use python nxexample01.py NAME_OF_FILE_TO_BE_WRITTEN")
        print ("\t For example, python nxexample01.py new-file.graphml")
        return
    
    # The following line creates a new undirected, empty graph
    g1 = nx.Graph()
    operateGraph (g1, 'wangxx-cs327graph01.png', 'wangxx-cs327graph02.png', 'wangxx-cs327graph03.png', 'wangxx-cs327graph04.png', sys.argv[1])

    # The following line creates a new directed, empty graph
    g2 = nx.DiGraph()
    operateGraph (g2, 'wangxx-cs327directedgraph01.png', 'wangxx-cs327directedgraph02.png', 'wangxx-cs327directedgraph03.png', 'wangxx-cs327directedgraph04.png', sys.argv[1])

    #
    # The following line converts a directed graph to an undirected one
    #
    g3 = g2.to_undirected ()

if __name__ == "__main__":
    main()
