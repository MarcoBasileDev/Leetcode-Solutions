class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(root, visited):
            if root == destination:
                return True

            visited.add(root)
            for neighbor in adj[root]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            
            return False

        visited = set()
        return dfs(source, visited)

        # Time Complexity O(V+E)
        # Space Complexity O(V+E)