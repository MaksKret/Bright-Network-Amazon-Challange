import math

## Only works with square graphs

class genGraph():
    
    def __init__(self, blocks):
        ## n = number of nodes
        self.n = 100
        self.sqrtn = 10
        ## getting the graph ready
        self.graph = [[None]*self.n for i in range(self.n)]
        for i in range(self.n):
            self.graph[i][i] = 0

        ## cases for the first inner square, not counting horizontal bottom rim and vertical most right rim
        for i in range(self.n):
            if (i+1)%self.sqrtn != 0 and i < (self.n - self.sqrtn):
                self.graph[i][i+1] = 1
                self.graph[i+1][i] = 1
                self.graph[i][i+self.sqrtn] = 1
                self.graph[i+self.sqrtn][i] = 1
                self.graph[i][i+self.sqrtn+1] = math.sqrt(2)
                self.graph[i+self.sqrtn+1][i] = math.sqrt(2)

        ## vertical most right (-1 because don't need last one)
        for i in range(self.sqrtn-1):
            self.graph[self.sqrtn - 1 + i*self.sqrtn][self.sqrtn - 1 + (i+1)*self.sqrtn] = 1
            self.graph[self.sqrtn - 1 + (i+1)*self.sqrtn][self.sqrtn - 1 + i*self.sqrtn] = 1

        ## horizontal bottom
        for i in range(self.n - self.sqrtn, self.n-1):
            self.graph[i][i+1] = 1
            self.graph[i+1][i] = 1

        ## horizontal diagonal
        for i in range(1, self.sqrtn):
            for j in range(i,i*self.sqrtn,self.sqrtn-1):
                self.graph[j][j+self.sqrtn-1]
                self.graph[j+self.sqrtn-1][j]
                
        ## vertical diagonal
        cnt = 1
        for i in range(self.n-1, 2*self.sqrtn-1, -self.sqrtn+1):
            cnt =+ 1
            for j in range(i,self.n-cnt,self.sqrtn-1):
                self.graph[j][j+self.sqrtn-1]
                self.graph[j+self.sqrtn-1][j]

        ## now adding blocks
        for i in blocks:
            block = int(str(i[0])+str(i[1]))
            for j in range(self.n):
                if block != j:
                    self.graph[block][j] = None
                    self.graph[j][block] = None
        
    def getGraph(self):
        return self.graph

        



