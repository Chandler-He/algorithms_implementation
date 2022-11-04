import pandas as pan
#import pandas lib for read csv file, it is the easiest way to catch files

arr = 2**32  
# size of the array

class Solution():
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.next = None

def prim(linklist):
    ver_near = 0
    #def distance arrays
    total = 0
    #total vertices
    n = len(linklist)
    #def n as the val of graph
    nearest_path = [0] * n
    #def nearest path
    dist = [-1] * n
    #def distance
    edge = n-1
    #def the graph's bound

    for i in range(1, n):
        nearest_path[i] = 0
        #from the first val to iterate
        dist[i] = dists(0, i, linklist)
        #if the last added val equals to the first val of graph

    print()
    print('Node\t', 'Node\t', 'Distance\t')
    print("*"*50)
    while edge > 0:
        #check the boundary
        mins = arr
        for i in range(1, n):
            #loop for nearest nodes
            if 0 < dist[i] < mins:
                mins = dist[i]
                ver_near = i
                #update mins and nearest vertice
        
        print("%s\t"%nearest_path[ver_near], "%s\t"%ver_near, "%s"%dist[ver_near])
        total += dist[ver_near]
        #def the calculation rules
        for j in range(1, n):
            #loop for nodes
            if dists(j, ver_near, linklist) < dist[j]:
                #check the boundary
                dist[j] = dists(j, ver_near, linklist)
                nearest_path[j] = ver_near
        dist[ver_near] = -1
        edge -= 1
    return total

def dists(i, j, linklist):
    #store the 2d matrix in a linked list
    head = linklist[i]
    p_head = head.next
    #def a linked list and pointers to the nodes
    while p_head:
        if p_head.vertices == j:
            return p_head.edges
        else:
            p_head = p_head.next
    return arr

def main():
    global n
    
    file = pan.read_csv('Quiz6_Input_File.csv', usecols=[0, 1, 2])
    f = file

    node1 = f['node_id'].values
    node2 = f['connected_node_id'].values
    dist = f['distance'].values
    n = f['node_id'].values[-1] + 1
    linked_list = []
    #def a linkedlist array
    pre_lastVal = -1
    #def the last end value
    for r in range(len(f)):
        N = node1[r]
        if N != pre_lastVal:
            head = Solution(N, 0) 
            #init to 0
            linked_list.append(head)
            linklist = Solution(node2[r], dist[r])
            head.next = linklist
            end = linklist
        elif N == pre_lastVal:
            curr = Solution(node2[r], dist[r])
            end.next = curr
            end = curr
        pre_lastVal = N
    
    print('The total distance is:', prim(linked_list))
    print()
main()
