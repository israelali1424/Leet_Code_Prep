import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create a social network graph
social_network = nx.Graph()

# Add people as nodes
people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]
social_network.add_nodes_from(people)

# Add friendships as edges
friendships = [
    ("Alice", "Bob"), ("Alice", "Charlie"), ("Alice", "David"),
    ("Bob", "Charlie"), ("Bob", "Eve"), 
    ("Charlie", "David"), ("Charlie", "Frank"),
    ("David", "Eve"), ("David", "Frank"),
    ("Eve", "Grace"), 
    ("Frank", "Grace"), ("Frank", "Heidi"),
    ("Grace", "Heidi")
]
social_network.add_edges_from(friendships)

# Find communities using the Louvain method
try:
    from community import community_louvain
    partition = community_louvain.best_partition(social_network)
    # Color nodes based on community
    cmap = plt.cm.get_cmap("viridis", max(partition.values()) + 1)
    node_colors = [cmap(partition[node]) for node in social_network.nodes()]
except ImportError:
    # If community package is not available, use default colors
    node_colors = "skyblue"

# Analysis functions
def analyze_network(graph):
    analysis = {}
    
    # Basic statistics
    analysis["num_nodes"] = graph.number_of_nodes()
    analysis["num_edges"] = graph.number_of_edges()
    analysis["density"] = nx.density(graph)
    
    # Find the most connected person (highest degree centrality)
    degree_centrality = nx.degree_centrality(graph)
    analysis["most_connected"] = max(degree_centrality.items(), key=lambda x: x[1])[0]
    
    # Find the person with highest betweenness centrality (connecting different groups)
    betweenness_centrality = nx.betweenness_centrality(graph)
    analysis["highest_betweenness"] = max(betweenness_centrality.items(), key=lambda x: x[1])[0]
    
    # Clustering coefficient (how interconnected the friends are)
    analysis["avg_clustering"] = nx.average_clustering(graph)
    
    return analysis

# Run analysis
network_analysis = analyze_network(social_network)

# Calculate position layout for graph
pos = nx.spring_layout(social_network, seed=42)

# Visualization with node sizes based on importance
plt.figure(figsize=(10, 8))
degree = dict(social_network.degree())
node_size = [v * 500 for v in degree.values()]

nx.draw_networkx(
    social_network,
    pos=pos,
    with_labels=True,
    node_color=node_colors,
    node_size=node_size,
    edge_color="gray",
    alpha=0.8,
    font_weight="bold"
)

plt.title("Social Network Analysis")
plt.axis("off")

# Print analysis results
print("Network Analysis Results:")
print(f"Number of people: {network_analysis['num_nodes']}")
print(f"Number of friendships: {network_analysis['num_edges']}")
print(f"Network density: {network_analysis['density']:.3f}")
print(f"Most connected person: {network_analysis['most_connected']}")
print(f"Person bridging most communities: {network_analysis['highest_betweenness']}")
print(f"Clustering coefficient: {network_analysis['avg_clustering']:.3f}")

# Find shortest paths between specific people
shortest_path = nx.shortest_path(social_network, source="Alice", target="Heidi")
print(f"\nShortest connection path from Alice to Heidi: {shortest_path}")

# Calculate average path length
avg_path_length = nx.average_shortest_path_length(social_network)
print(f"Average degrees of separation: {avg_path_length:.2f}")