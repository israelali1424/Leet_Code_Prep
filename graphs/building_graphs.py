
from collections import defaultdict
def build_bidirectional_graph_aj_list(edges):
    # preseves the order of items added 
    graph =  defaultdict(list)
    for [a,b ] in edges:
        if a not in graph:
            graph[a]= []
        if b not in graph:
            graph[b]= []
        graph[a].append(b)
        graph[b].append(a)
    
    return graph
def build_directed_graph(edges): 
    # in a directed_graph nodes will only point one way 
    graph =  defaultdict()
    for [a,b ] in edges:
        if a not in graph:
            graph[a]= []
        if b not in graph:
            graph[b]= []
        # because the graph is directed you need connect a to b 
        if a and b:
            graph[a].append(b)
    return graph
    
    
    '''
    by direction graphs means each point leads the connected point 
    you have to loop throygh the list
    for each sub tuple 
    and in this set the value to blank for each item 
    then push the value of the value of edge[a]. append b
    edge[b] . append a 
    return the graph 
    '''

# build an bidrectional graph with these grades 
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

#print(build_bidirectional_graph_aj_list(edges))
print(build_directed_graph(edges))

# Test with a simple example
try:
    # Test case 1: Basic directed graph
    edges1 = [['A', 'B'], ['B', 'C'], ['A', 'C']]
    graph1 = build_directed_graph(edges1)
    print("Test case 1 (Basic graph):")
    print(graph1)
    
    # Test case 2: Graph with cycles
    edges2 = [['1', '2'], ['2', '3'], ['3', '1']]
    graph2 = build_directed_graph(edges2)
    print("\nTest case 2 (Graph with cycles):")
    print(graph2)
    
    # Test case 3: Graph with isolated nodes
    edges3 = [['X', 'Y'], ['Z', 'Z']]
    graph3 = build_directed_graph(edges3)
    print("\nTest case 3 (Graph with isolated nodes):")
    print(graph3)
    
    # Test case 4: Empty edge list
    edges4 = []
    graph4 = build_directed_graph(edges4)
    print("\nTest case 4 (Empty edge list):")
    print(graph4)
    
    # Test case 5: Edges with None values
    edges5 = [[None, 'A'], ['A', None]]
    graph5 = build_directed_graph(edges5)
    print("\nTest case 5 (Edges with None values):")
    print(graph5)
    
    print("\nAll tests passed successfully!")
    
except Exception as e:
    print(f"Test failed with error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()