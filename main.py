import json
import networkx as nx
from graphrag import GraphRAG
from community_detection import detect_communities
from neo4j_handler import Neo4jHandler

neo4j_uri = "bolt://localhost:7687"
neo4j_user = "neo4j"
neo4j_password = "password"

graphrag = GraphRAG(neo4j_uri, neo4j_user, neo4j_password)

with open("data.json", "r") as f:
    data = json.load(f)

graphrag.load_data(data)
detect_communities(graphrag.graph)
graphrag.store_in_neo4j()
graphrag.close()
