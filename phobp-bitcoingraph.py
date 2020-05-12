# Name: Brendan Pho
# Honor code: This work adheres to the JMU honor code

# *NOTE* This program is very inefficient, and so it is very slow.
# It takes over a minute for it to complete, but it will work!

import matplotlib
matplotlib.use('Agg')

import networkx as nx

import pylab as plt

import pygeoip

import os

import sys

def lookUpCountry(inIP):

    dirpath = os.getcwd()
    GEOIP = pygeoip.GeoIP(dirpath + "/GeoIP.dat", pygeoip.MEMORY_CACHE)
    country = GEOIP.country_name_by_addr(inIP)
    return country

def readGraph(inGraphFilename):

    localg = nx.read_graphml(inGraphFilename)
    localg = localg.to_undirected()

    degrees = [val for (node, val) in localg.degree()]
    degrees.sort(reverse=True)
    nodes = sorted(localg.degree, key=lambda x: x[1], reverse=True)
    country_list = []
    node_freq_list = []
    node_freq = {}

    print ("1. Bitcoin nodes in Bitcoin network: " + str(len(localg)))
    print ("\n2. Edges in the Bitcoin network: " + str(localg.number_of_edges()))

    print ("\n3. Largest node degree: " + str(degrees[0]))
    print ("Nodes that have the largest degree: ")
    for (node, val) in nodes:
        if val == degrees[0]: 
            print (node)

    print ("\n4. Smallest node degree: " + str(degrees[len(degrees) - 1]))
    print ("Nodes that have the smallest degree: ")
    for (node, val) in nodes:
        if val == degrees[len(degrees) - 1]:
            print (node)
    
    print ("\n5. 10 nodes with highest degree (IP address, degree): ")
    for i in range(10):
        pair = tuple(nodes[i])
        print (nodes[i]) 
        print("Country: " + lookUpCountry(pair[0]))
        print ("\n")

    print ("6. 5 countries with highest number of Bitcoin nodes (country, number of nodes): ")
    for node in localg:
        country_list.append(lookUpCountry(node)) 
  
    for country in country_list:
        node_freq[country] = 0

    for country in country_list:
        if country in node_freq:
            node_freq[country] += 1

    for key in node_freq:
        node_freq_list.append((key, node_freq[key]))
    node_freq_list.sort(key=lambda x: x[1], reverse = True)


    for i in range(5):
        print(node_freq_list[i]) 

    nx.draw_networkx(localg)
    plt.show()
    plt.savefig("graph-visual.png")
        
def main():

    numOfArgs = len(sys.argv)
    if numOfArgs == 1:
        print ("Use python phobp-bitcoingraph.py NAME_OF_FILE_TO_BE_READ")
        print ("\t For example, python phobp-bitcoingraph.py file-to-read.graphml")
        return
    readGraph(sys.argv[1])

if __name__ == "__main__":
    main()


        
