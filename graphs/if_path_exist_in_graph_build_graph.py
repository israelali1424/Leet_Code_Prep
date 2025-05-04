class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        def build_graph(edges):
            graph = {}
            for u, v in edges:
                if u not in graph:
                    graph[u] = []
                if v not in graph:
                    graph[v] = []
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def dfs(graph, node, destination, seen):
            if node == destination:
                return True
            
            seen.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in seen:
                    if dfs(graph, neighbor, destination, seen):
                        return True
            return False

        graph = build_graph(edges)
        return dfs(graph, source, destination, set())