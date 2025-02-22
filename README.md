# GraphRAG Project

## Overview
GraphRAG is a **Retrieval-Augmented Generation (RAG)** system that enhances document retrieval by leveraging graph-based relationships and **community detection**. The project stores and manages relationships in **Neo4j**, enabling efficient information retrieval.

## Features
- **Graph-based Retrieval**: Documents and their relationships are stored as a graph.
- **Community Detection**: Uses **Louvain algorithm** to detect related document clusters.
- **Neo4j Integration**: Stores and queries graph data in a Neo4j database.
- **Flexible Data Ingestion**: Loads structured document data from a JSON file.

## Project Structure
```
GraphRAG_Project/
│── graphrag.py          # Core GraphRAG implementation
│── community_detection.py  # Community detection logic
│── neo4j_handler.py     # Handles Neo4j interactions
│── data_loader.py       # Loads document data
│── main.py              # Entry point for running the project
│── data.json            # Sample dataset
│── requirements.txt     # Required dependencies
```

## Installation
### Prerequisites
- **Python 3.8+**
- **Neo4j Database** (Ensure Neo4j is installed and running on `bolt://localhost:7687`)

### Setup
1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd GraphRAG_Project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Step 1: Start Neo4j
Ensure your Neo4j instance is running on `bolt://localhost:7687`.

### Step 2: Load Data and Run the System
Execute the `main.py` file:
```bash
python main.py
```
This will:
1. Load data from `data.json`
2. Build a graph of documents and relationships
3. Detect communities
4. Store the graph in **Neo4j**

## Configuration
- Update `neo4j_uri`, `neo4j_user`, and `neo4j_password` in `main.py` if needed.
- Modify `data.json` to use custom documents.

## Querying Neo4j
After running the project, you can query stored documents and their relationships using **Cypher** queries in Neo4j:
```cypher
MATCH (d:Document) RETURN d LIMIT 10;
```

## Dependencies
- `neo4j`
- `networkx`
- `python-louvain`

## Future Improvements
- Implement **semantic search** for document retrieval.
- Add **graph-based ranking algorithms** for better relevance scoring.
