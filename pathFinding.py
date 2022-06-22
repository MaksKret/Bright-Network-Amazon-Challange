from dijkstraAlgo import *
from generateGraph import *
import random

print("#############")
print("## Phase 1 ##")
print("#############")

blocks = [[8,7],[7,7],[7,8],[7,9]]
graph = genGraph(blocks)
sol = Dijkstra(graph.getGraph())
sol.getPath()

print("#############")
print("## Phase 2 ##")
print("#############")

## choosing blocks excluding [8,7],[7,7],[7,8],[7,9]
randomnums = random.sample([x for x in range(1,99) if x != 87 and x != 77 and x != 78 and x!= 79], 20)
randomblocks = []
for i in randomnums:
    if len(str(i)) == 1:
        randomblocks.append([0,i])
    else:
        randomblocks.append([int(str(i)[0]), int(str(i)[1])])
    
print("-")
print("Randomly generated blocks are: ")
print(randomblocks)

for i in blocks:
    randomblocks.append(i)

graph = genGraph(randomblocks)
sol = Dijkstra(graph.getGraph())
sol.getPath()