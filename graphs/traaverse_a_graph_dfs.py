# print a graph using dfs 
# this grpah is an Adjacency List
def depthFirstPrint(graph,source):
    stack = [source]
    
    while stack: 
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)
       
        
def depthFirstPrintRecursion(graph,source):
    print(source)
    for neighbor in graph[source]:
        depthFirstPrintRecursion(graph,neighbor)
        
    
     
graph = {
    'a':['b','c'],
    'b': ['d'],
    'c':['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depthFirstPrintRecursion(graph,'a') #acbedf 

