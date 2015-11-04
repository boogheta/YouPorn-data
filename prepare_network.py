#!/usr/bin/env python

import sys
import networkx as nx

def add_node(node, graph, stats, nline):
    if graph.has_node(node):
        graph.node[node]['occurences'] += 1
        stats[tag].add(nline)
    else:
        graph.add_node(node, occurences=1)
        stats[tag] = set([nline])

def add_edge(node1, node2, graph):
    if not graph.has_edge(node1, node2):
        graph.add_edge(node1, node2)

def add_edge_weight(node1, node2, graph):
    if graph.has_edge(node1, node2):
        graph[node1][node2]['weight'] += 1
    else:
        graph.add_edge(node1, node2)
        graph[node1][node2]['weight'] = 1

graph = nx.Graph()
stats = {}
nline = 0
with open(sys.argv[1]) as f:
    for line in f.readlines():
        line = line.strip()
        prevtags = []
        for tag in line.split(","):
            add_node(tag, graph, stats, nline)
            for old in prevtags:
                #add_edge_weight(tag, old, graph)
                add_edge(tag, old, graph)
            prevtags.append(tag)
        nline += 1

tags = graph.nodes()
for tag1 in graph.nodes():
    tags.remove(tag1)
    for tag2 in tags:
        if graph.has_edge(tag1, tag2):
            graph[tag1][tag2]["weight"] = float(len(stats[tag1] & stats[tag2])) / len(stats[tag1] | stats[tag2])

nx.write_gexf(graph, sys.argv[1].replace(".csv", ".gexf"))
