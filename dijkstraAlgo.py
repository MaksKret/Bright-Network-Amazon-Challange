from minH import minHeap
import math 

## Dijkstra on a graph with starting node 0, and using a matrix graph

class Dijkstra:

    def __init__(self, G):
        ## number of nodes
        self.num = 100
        self.graph = G
        self.queue = minHeap([])
        self.initializeSource()
        self.queue.insertItem([0,0])
        self.d[0] = 0
        while not self.queue.isEmpty():
            curr = self.queue.extractMin()
            for i in range(self.num):
                if self.graph[curr[1]][i] != None and curr[1] != i:
                    self.relax([curr[1], i])

    def initializeSource(self):
        self.d = [math.inf for i in range(self.num)]
        self.pi = [None for i in range(self.num)]

    def relax(self, tuple):
        if self.d[tuple[1]] == math.inf:
            self.d[tuple[1]] = self.d[tuple[0]] + self.graph[tuple[0]][tuple[1]]
            self.pi[tuple[1]] = tuple[0]
            self.queue.insertItem([self.d[tuple[1]], tuple[1]])
        elif self.d[tuple[1]] > self.d[tuple[0]] + self.graph[tuple[0]][tuple[1]]:
            self.d[tuple[1]] = self.d[tuple[0]] + self.graph[tuple[0]][tuple[1]]
            self.pi[tuple[1]] = tuple[0]
            self.queue.reduceKey(self.d[tuple[1]], tuple[1])

    def getPath(self):
        if self.d[self.num - 1] != math.inf:
            x = self.pi[self.num-1]
            path = [self.num - 1]
            while x != 0:
                path.append(x)
                x = self.pi[x]
            path.append(0)
            path.reverse()     ## path is in backwards chronological order so need to reverse it
            coorpath = []
            for i in path:
                if len(str(i)) == 1:
                    coorpath.append((0,i))
                else:
                    coorpath.append((int(str(i)[0]), int(str(i)[1])))
            print("-")
            print("Optimal path is " + str(coorpath))
            print("-")
            print("Number of steps is " + str(len(coorpath)))
            print("-")
            print("The optimal path is length " + str(self.d[self.num-1]))
            print("-")
        else:
            print("-------------------------------------")
            print("There is no path from (0,0) and (9,9)")
            print("-------------------------------------")



