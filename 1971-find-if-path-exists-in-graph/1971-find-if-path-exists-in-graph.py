class Solution(object):
    def validPath(self, n, edges, source, destination):
        if n == 1:
            return True  
        visited = [False] * n
        visited[source] = True
        flag = True
        while flag:
            flag = False
            for edge in edges:
                if visited[edge[0]] != visited[edge[1]]:
                    visited[edge[0]] = True
                    visited[edge[1]] = True
                    flag = True
                if visited[destination]:
                    return True
        return False