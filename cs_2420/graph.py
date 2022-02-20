class Graph:
    
    def __init__(self, num_vertices): # 5 verts
        self.m_neighbors = []
        for num in range(num_vertices):
            self.m_neighbors.append([])
        
    
    def find_path(self, v0, v1): # return a list of steps or None if can't
        Q = Queue()
        From = [-1] * len(self.m_neighbors) # all -1 but first is 0
        Q.enqueue(v0)
        From[v0] = v0
        while Q.is_empty() is False:
            c = Q.dequeue()
            if c == v1:
                # build the whole path and return it
                path = [c]
                while From[c] != c:
                    c = From[c]
                    path.append(c)
                # it'll be backwards, so path.reverse()
                path.reverse()
                return path
            else:
                # for all neighbors n of c that havent been visited
                for n in self.m_neighbors[c]:
                    if From[n] == -1:
                        Q.enqueue(n)
                        From[n] = c # n came From c
        return None
    
    def add_edge(self, v0, v1): # return None
        self.m_neighbors[v0].append(v1)
        return None
    
    def is_edge(self, v0, v1): # return true of false
        if v1 in self.m_neighbors[v0]:
            return True
        return False
    
    def get_neighbors(self, v0): #return list
        return self.m_neighbors[v0]
        
    
class Queue():
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        return self.queue.pop(0)
        
    def is_empty(self):
        if self.queue == []:
            return True
        return False
        

def main():
	f = open("Graph.txt", "r")
	num_vertices = int(f.readline())
	G = Graph(num_vertices)
	num_edges = int(f.readline())
	for i in range(num_edges):
		line = f.readline() # "0 1"
		words = line.split() # ["0", "1"]
		G.add_edge(int(words[0]), int(words[1])) # first item and 2nd, not 0 and 1
	num_tests = int(f.readline())
	for i in range(num_tests):
		line = f.readline() # "0 1"
		words = line.split() # ["0", "1"]
		print(G.find_path(int(words[0]), int(words[1])))
		
main()