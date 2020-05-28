# Test.it("But what if you actually needed to move?")
# Test.assert_equals(cheapest_path([[1,9,1],[2,9,1],[2,1,1]], (0,0), (0,2)), ["down", "down", "right", "right", "up", "up"])

# Steps:
# 1. Convert start & end tuples to index in array
# 2. Convert matrix to adjacency matrix so that all possible connections are mapped out 
#     (Djikstra s algorithm is typically written for adjacency matrices)
#     a. Get list of all possible connections for all elements 
#     b. create adjacency matrix, all 0 except 1s for the elements that have a weight
#     c. multiply all rows of elements with the same 'leaving weight': a row will contain either a 0 or this leaving weight
# 3. Pass this matrix to Djikstra s algorithm while keeping track of the parent nodes for shortest path
# 4. Finish the matrix


import numpy as np
import sys
from collections import defaultdict 

matrix = np.array([[1,9,1],[2,9,1],[2,1,1]])
start = (0,0)
finish = (0,2)


def convert_position(el:tuple, matrix):
    """Get array index of tuple start and tuple finish
    Returns:
        [int] -- index of tuple in array of elements
    """
    return el[0]*ncol + el[1]
    # for start: 0 
    # for finish: 2


def return_list_connections(matrix):
    """Return list of possible connections for all elements. 
    Eg: element and index (0,0) in example has a convert_position of 0.
    0 can match with 2 and 4 only (right and down). the return will start with [[2,4], ...]
    Returns:
        [list of list] -- [containing potential connections]
    """
    # [[1,2,3]
    # [4,5,6]
    # [7,8,9]]
    # if n % ncol == 0,   then el is on the right side, and CANNOT GO RIGHT aka cannot do +1
    # if (n - 1)%ncol == 0, then el is on the left side and CANNOT GO LEFT aka cannot do -1
    # if el+move < 1, means we are at first row, then       CANNOT GO UP, think 3-3 = 0 -> 3 
    # if el+move> number of elements, means that we are at last row, and CANNOT GO DOWN aka cannot do +ncol

    num_el = ncol * matrix.shape[0]
    # Potential connections for each array element:
    possible_iter = [-1, +1, -ncol, +ncol]


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
    # [[2, 4], [1, 3, 5], [2, 6], [5, 1, 7], [4, 6, 2, 8], [5, 3, 9], [8, 4], [7, 9, 5], [8, 6]]
    # means 1 can connect with 2 and 4, 2 can connect with 1, 3 and 5


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
    # now that have matrix of 1 and 0, need to times the actual weight so that connection row_value -> col_value

    # iterate over all values and times this value times the corresponding row:
    diago = []
    for (x,y), value in np.ndenumerate(matrix):
        diago.append(value)

    c = np.diag(diago)
    adjacency_matrix = np.dot(c,adjacency_matrix)

    return adjacency_matrix
    # [[0 1 0 1 0 0 0 0 0]
    # [9 0 9 0 9 0 0 0 0]
    # [0 1 0 0 0 1 0 0 0]
    # [2 0 0 0 2 0 2 0 0]
    # [0 9 0 9 0 9 0 9 0]
    # [0 0 1 0 1 0 0 0 1]
    # [0 0 0 2 0 0 0 2 0]
    # [0 0 0 0 1 0 1 0 1]
    # [0 0 0 0 0 1 0 1 0]]





# Python program for Dijkstra's  
# single source shortest 
# path algorithm. The program 
# is for adjacency matrix 
# representation of the graph
  
  
class Graph: 
  
    # A utility function to find the  
    # vertex with minimum dist value, from 
    # the set of vertices still in queue 
    def minDistance(self,dist,queue): 
        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
          
        # from the dist array,pick one which 
        # has min value and is in queue 
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
    

    def printDirection(self, arr):
    # compute difference between array elements of the path found by Djikstra's algorithm.
    # if +ncol then down, -ncol then up, +1 then right, -1 then left
        diff = np.diff(arr)
        diff = np.where(diff == ncol, "down", 
            (np.where(diff==-ncol, "up", 
            (np.where(diff==-1, "left",
            "right")))))
        return list(diff)
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
    def printSolution(self, parent, finish): 
        print(self.printPath(parent,finish))
  
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

  
            # remove min element -> checked all the paths going from this node     
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
                    # eg:
                    # if dist[0] + graph[0][1] < dist[1], then found a shortest path to a specific node and have to add it
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
  
  
        # print the constructed distance array 
        self.printSolution(parent, finish) 


def cheapest_path(matrix, start, finish):
    matrix = np.array(matrix)
    global arr 
    arr = []
    global ncol
    ncol = matrix.shape[1]
    start = convert_position(start, matrix)
    finish = convert_position(finish, matrix)
    graph = return_adjacency_matrix(matrix)

    g = Graph() 
    # Print the solution 
    g.dijkstra(graph,start, finish)

cheapest_path(matrix, start, finish)
# cheapest_path([[1]], (0,0), (0,0))
# cheapest_path([[1,4,1],[1,9,1],[1,1,1]], (0,0), (0,2))
