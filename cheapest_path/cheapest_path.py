# Test.it("But what if you actually needed to move?")
# Test.assert_equals(cheapest_path([[1,9,1],[2,9,1],[2,1,1]], (0,0), (0,2)), ["down", "down", "right", "right", "up", "up"])
import numpy as np
import sys
from collections import defaultdict 

matrix = np.array([[1,9,1],[2,9,1],[2,1,1]])
start = (0,0)
finish = (0,2)

# get position in array of starting and finishing element:
def convert_position(el:tuple, matrix):
    ncol = matrix.shape[1]
    return el[0]*ncol + el[1]
start = convert_position(start, matrix)
finish = convert_position(finish, matrix)

ncol = matrix.shape[1]
# print(len(matrix))


def return_list_connections(matrix):
    ncol = matrix.shape[1]
    num_el = ncol * matrix.shape[0]

    possible_iter = [-1, +1, -ncol, +ncol]

    # list of lists of possible connections for each node
    connections = []
    for el in range(1,num_el+1):
        new_el = []
        possible_iter_el = possible_iter
        if el % ncol == 0:
            possible_iter_el = possible_iter_el[:1] + possible_iter_el[2:]
        elif (el-1) % ncol == 0:
            possible_iter_el = possible_iter_el[1:]

        for move in possible_iter_el:
            new_connection = el + move
            if new_connection<1 or new_connection>num_el:
                pass
            else:
                new_el.append(el+move)
        connections.append(new_el)

    return connections

# at the locations listed above put a 1, else it is 0
# multiply by row value
def return_adjacency_matrix(matrix):
    list_connections = return_list_connections(matrix)
    num_el = matrix.shape[0]*matrix.shape[1]
    adjacency_matrix = np.zeros([num_el,num_el], dtype = int)

    n = len(list_connections)

    for i in range(0,n):
        for el in list_connections[i]:
            adjacency_matrix[i,el-1] = 1
    
    # now that have matrix of 1 and 0, need to x it so that connection row_value -> col_value

    # iterate over all values and times this value times the corresponding row:
    diago = []
    for (x,y), value in np.ndenumerate(matrix):
        diago.append(value)

    c = np.diag(diago)
    adjacency_matrix = np.dot(c,adjacency_matrix)

    return adjacency_matrix

# print(return_adjacency_matrix(matrix))




# Python program for Dijkstra's  
# single source shortest 
# path algorithm. The program 
# is for adjacency matrix 
# representation of the graph 
  
  
#Class to represent a graph 
class Graph: 
  
    # A utility function to find the  
    # vertex with minimum dist value, from 
    # the set of vertices still in queue 
    def minDistance(self,dist,queue): 
        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
          
        # from the dist array,pick one which 
        # has min value and is till in queue 
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
  
    def printDirection(self, arr):
    # compute difference between arr elements. if +ncol then down, -ncol then up, +1 then right, -1 then left
        diff = np.diff(arr)
        diff = np.where(diff == ncol, "down", 
            (np.where(diff==-ncol, "up", 
            (np.where(diff==-1, "left",
            "right")))))
        return diff
    # Function to print shortest path 
    # from source to j 
    # using parent array 

    def printPath(self, parent, j): 
          
        #Base Case : If j is source 
        if parent[j] == -1 :  
            arr.append(j) 
            return
        self.printPath(parent , parent[j]) 
        arr.append(j) 
        return self.printDirection(arr)

          
  
    # A utility function to print 
    # the constructed distance 
    # array 
    def printSolution(self, dist, parent, start, finish): 
        print(self.printPath(parent,finish))
        # print("\n%d --> %d \t\t%d \t\t\t\t\t" % (start, finish, dist[finish])), self.printPath(parent,finish) 
  
  
    '''Function that implements Dijkstra's single source shortest path 
    algorithm for a graph represented using adjacency matrix 
    representation'''
    def dijkstra(self, graph, src, finish): 
  
        row = len(graph) 
        col = len(graph[0])
  
        # The output array. dist[i] will hold 
        # the shortest distance from src to i 
        # Initialize all distances as INFINITE  
        dist = [float("Inf")] * row 
  
        #Parent array to store  
        # shortest path tree 
        parent = [-1] * row 
  
        # Distance of source vertex  
        # from itself is always 0 
        dist[src] = 0
      
        # Add all vertices in queue 
        queue = [] 
        for i in range(row): 
            queue.append(i) 
              
        #Find shortest path for all vertices 
        while queue: 
  
            # Pick the minimum dist vertex  
            # from the set of vertices 
            # still in queue 
            u = self.minDistance(dist,queue)  
  
            # remove min element      
            queue.remove(u) 
  
            # Update dist value and parent  
            # index of the adjacent vertices of 
            # the picked vertex. Consider only  
            # those vertices which are still in 
            # queue 
            for i in range(col): 
                '''Update dist[i] only if it is in queue, there is 
                an edge from u to i, and total weight of path from 
                src to i through u is smaller than current value of 
                dist[i]'''
                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
  
  
        # print the constructed distance array 
        self.printSolution(dist,parent, start, finish) 
  
g = Graph() 
arr = []
graph = return_adjacency_matrix(matrix)

# Print the solution 
g.dijkstra(graph,start, finish)