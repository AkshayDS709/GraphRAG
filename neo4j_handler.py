from neo4j import GraphDatabase

class Neo4jHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_graph(self, graph):
        with self.driver.session() as session:
            session.write_transaction(self._create_graph, graph)

    def _create_graph(self, tx, graph):
        for node, attributes in graph.nodes(data=True):
            tx.run("CREATE (n:Document {id: $id, content: $content, community: $community})",
                   id=node, content=attributes["content"], community=attributes.get("community", -1))
        for source, target, attributes in graph.edges(data=True):
            tx.run("MATCH (a:Document {id: $source}), (b:Document {id: $target}) "
                   "CREATE (a)-[:LINKS_TO {weight: $weight}]->(b)",
                   source=source, target=target, weight=attributes.get("weight", 1))
