from typing import Any

import numpy as np
import networkx as nx

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, mst_set: set[Any], rest_set: set[tuple[Any, Any]], mst_edges: set[Any]) -> set[tuple[Any, Any]]:
    edge_to_add = {
        "edge": (None, None),
        "weight": np.inf,
    }
    node_to_add = None
    for node in mst_set:
        for neigh_node in G.neighbors(node):
            if neigh_node in mst_set:
                continue
            if G[node][neigh_node]["weight"] < edge_to_add["weight"]:
                edge_to_add["edge"] = (node, neigh_node)
                edge_to_add["weight"] = G[node][neigh_node]["weight"]
                node_to_add = neigh_node
    if rest_set:
        return (
            prim_mst(
            G,
            mst_set | {node_to_add},
            rest_set.difference(mst_set | {node_to_add}),
            mst_edges | {edge_to_add["edge"]}
            )
        )
    else:
        return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("./graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)

    start_node = "0"

    edges = prim_mst(G, set(start_node), set(G.nodes()).difference({start_node}), set())

    plot_graph(G, highlighted_edges=list(edges))
