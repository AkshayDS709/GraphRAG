from neo4j import GraphDatabase
import networkx as nx
from community import community_louvain
import json

class GraphRAG:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.graph = nx.Graph()

    def close(self):
        self.driver.close()

    def load_data(self, json_data):
        for doc in json_data["documents"]:
            self.graph.add_node(doc["id"], content=doc["content"], type="document")
        for link in json_data.get("links", []):
            self.graph.add_edge(link["source"], link["target"], weight=link.get("weight", 1))

    def detect_communities(self):
        partition = community_louvain.best_partition(self.graph)
        for node, community in partition.items():
            self.graph.nodes[node]["community"] = community
        return partition

    def store_in_neo4j(self):
        with self.driver.session() as session:
            session.write_transaction(self._create_graph)

    def _create_graph(self, tx):
        for node, attributes in self.graph.nodes(data=True):
            tx.run("CREATE (n:Document {id: $id, content: $content, community: $community})",
                   id=node, content=attributes["content"], community=attributes.get("community", -1))
        for source, target, attributes in self.graph.edges(data=True):
            tx.run("MATCH (a:Document {id: $source}), (b:Document {id: $target}) "
                   "CREATE (a)-[:LINKS_TO {weight: $weight}]->(b)",
                   source=source, target=target, weight=attributes.get("weight", 1))
