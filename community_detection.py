import networkx as nx
from community import community_louvain

def detect_communities(graph):
    partition = community_louvain.best_partition(graph)
    for node, community in partition.items():
        graph.nodes[node]["community"] = community
    return partition
