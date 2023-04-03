from typing import Any

import numpy as np
import networkx as nx

from src.plotting import plot_graph

def dijkstra_sp(G: nx.Graph, destination_node: str, source_node="0") -> dict[Any, list[Any]]:
    unvisited = set(G.nodes())
    visited = set()
    shortest_paths = {}
    dist = {n: np.inf for n in G}
    dist[source_node] = 0
    shortest_paths[source_node] = [source_node]
    while len(unvisited) > 1:
        node = None
        min_dist = np.inf
        for n, d in dist.items():
            if (n in unvisited) and (d < min_dist):
                min_dist = d
                node = n
        if (node == destination_node):
            return shortest_paths
        unvisited.remove(node)
        visited.add(node)
        for neigh_node in G.neighbors(node):
            if neigh_node in visited:
                continue
            new_dist = min_dist + G.edges[node, neigh_node]["weight"]
            if new_dist < dist[neigh_node]:
                dist[neigh_node] = new_dist
                shortest_paths[neigh_node] = shortest_paths[node] + [neigh_node]
    return shortest_paths


if __name__ == "__main__":
    destination_node = "4"
    G = nx.read_edgelist("./graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, destination_node, source_node="0")
    shortest_path_edges = [
        (shortest_paths[destination_node][i], shortest_paths[destination_node][i + 1])
        for i in range(len(shortest_paths[destination_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
