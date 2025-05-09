from collections import deque

class DFSTraversal:
    def __init__(self, v):
        self.adjacency = [[] for _ in range(v)]
    
    def insert_edge(self, s, d):
        self.adjacency[s].append(d)
        self.adjacency[d].append(s)  # For undirected graph
    
    def dfs_display(self, source):
        visited_nodes = [False] * len(self.adjacency)
        parent_nodes = [-1] * len(self.adjacency)
        stack = deque()
        stack.append(source)
        visited_nodes[source] = True
        
        while stack:
            p = stack.pop()
            print(f"DFS traversal is: {p}")
            
            for i in self.adjacency[p]:
                if not visited_nodes[i]:
                    visited_nodes[i] = True
                    stack.append(i)
                    parent_nodes[i] = p

def main():
    print("Enter the number of Vertices and Edges: ")
    vertices, edges = map(int, input().split())
    dfs = DFSTraversal(vertices)
    
    print("Enter edges: ")
    for _ in range(edges):
        s, d = map(int, input().split())
        dfs.insert_edge(s, d)
    
    print("Enter the source where you want to traverse the graph: ")
    source = int(input())
    dfs.dfs_display(source)

if __name__ == "__main__":
    main()