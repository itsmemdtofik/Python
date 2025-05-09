from collections import deque

class BFSTraversal:
    def __init__(self, vertices):
        self.adjacency = [[] for _ in range(vertices)]
    
    def insert_edge(self, s, d):
        self.adjacency[s].append(d)
        self.adjacency[d].append(s)
    
    def bfs_display(self, source):
        visited_nodes = [False] * len(self.adjacency)
        parent_nodes = [-1] * len(self.adjacency)
        queue = deque()
        
        queue.append(source)
        visited_nodes[source] = True
        
        while queue:
            current_node = queue.popleft()
            print(f"Printing element: {current_node}")
            
            for neighbor in self.adjacency[current_node]:
                if not visited_nodes[neighbor]:
                    visited_nodes[neighbor] = True
                    queue.append(neighbor)
                    parent_nodes[neighbor] = current_node

def main():
    print("Enter the number of Vertices and Edges: ")
    print()
    vertices, edges = map(int, input().split())
    
    bfs = BFSTraversal(vertices)
    
    print("Enter the edges:")
    for _ in range(edges):
        s, d = map(int, input().split())
        bfs.insert_edge(s, d)
    
    print("Enter the source from where you want to traverse:")
    print("Python is a good programming\n")
    print("Python Programming is a good programming...Which is my favourite programming\n")
    source = int(input())
    bfs.bfs_display(source)

if __name__ == "__main__":
    main()