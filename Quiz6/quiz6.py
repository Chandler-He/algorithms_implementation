import pandas as pan
#import pandas lib for read csv file, it is the easiest way to catch files

arr = 2**32  # size of the array

def prim(graph):

    global arr

    #def distance arrays
    ver_near = 0
    #def nearset vertice
    total = 0
    #total vertices
    n = len(graph)
    #def n as the val of graph
    nearest_path = [0] * n
    #def nearest path
    dist = [-1] * n
    #def distance
    edge = n - 1
    #def the graph's bound
    
    for i in range(1, n):

        nearest_path[i] = 0
        #from the first val to iterate
        dist[i] = graph[i][0]
        #if the last added val equals to the first val of graph
    
    while edge > 0:
        #set boundary
        mins = arr
        for i in range(1, n):
            #loop for nearest nodes
            if 0 < dist[i] < mins:
                #update mins and nearest vertice
                mins = dist[i]
                ver_near = i
        print("%s\t\t"%nearest_path[ver_near], "%s\t"%ver_near, "%s"%dist[ver_near])
            
        total = total + dist[ver_near]
        #def the calculation rules
        for j in range(1, n):
            #loop for nodes
            if graph[j][ver_near] < dist[j]:
                #set boundary, in case out of range
                dist[j] = graph[j][ver_near]
                nearest_path[j] = ver_near
        dist[ver_near] = -1
        edge = edge - 1
        #update edge
    print("*"*50)
    print()
    return total


def main():
    global arr

    print()
    print('Node\t', 'Node\t', 'Distance\t')
    print("*"*50)

    file = pan.read_csv('Quiz6_Input_File.csv', usecols=[0, 1, 2])
    #catch csv file and set the output columns display.
    f = file
    node1 = f['node_id'].values
    node2 = f['connected_node_id'].values
    dis = f['distance'].values
    n = f['node_id'].values[-1] + 1
    #read and set rules for csv file

    adjacent = [[arr] * n for i in range(n)]
    #iterate the arr in the range of NodeID

    for k in range(len(f)):
        adjacent[node1[k]][node2[k]] = dis[k]
    #update adjacent array
    
    print('The total distance is:', prim(adjacent))
    print()

main()