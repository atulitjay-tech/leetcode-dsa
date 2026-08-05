# LeetCode: 3310
# Problem: Remove Methods From Project

# Primary Topic:
# - Graph

# Secondary Topics:
# - BFS
# - Graph Theory

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

# Author: Atulit



from collections import deque
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        graph = {i: [] for i in range(n)}
        for u, v in invocations:
            graph[u].append(v)
            
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
                
        return [i for i in range(n) if i not in suspicious]
