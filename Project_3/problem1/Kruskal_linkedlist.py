import pandas as pd
import os
import numpy as np
import psutil

arr = 2**16

class Solution(object):
    def __init__(self, vertice, edge):
        self.vertice = vertice
        self.edge = edge
        self.next = None

def edge(linklist):
    edgeList = []
    for node in linklist:
        N = node.next
        while N:
            if node.vertice < N.vertice:
                edgeList.append((N.edge, node.vertice, N.vertice))
            N = N.next
    edgeList.sort()
    return edgeList


def kruskal(linklist):
    n = len(linklist)
    m = list(range(n))
    edgeList = edge(linklist)
    result = []
    sum = 0  
    # total distance

    def find(i):
        while m[i] != i:
            i = m[i]
        return i

    def merge(p, q):
        if p < q:
            m[q] = p
        else:
            m[p] = q

    j = 0
    print('Node', 'Node', 'Distance')
    while len(result) < n-1:
        (long, vertice_small, vertice_big) = edgeList[j]
        q = find(vertice_small)
        p = find(vertice_big)
        if q != p:
            merge(p, q)
            result.append(edgeList[j])
            print(vertice_small,'\t', vertice_big,'\t', long)
            sum = sum+long
        j = j + 1
    return sum


if __name__ == '__main__':
    coordinates = []  
    # distinct coordinates for every node
    name = []  
    # intersection_names
    
    file_1 = pd.read_csv('Project3_G1_Data.csv')
    coordinate1 = file_1['Coordinates'].values
    distance1 = file_1['Distance'].values
    name1 = file_1['Intersection_Name'].values
    #processing file_1
    file_2 = pd.read_csv('Project3_G2_Data.csv')
    coordinate2 = file_2['Coordinates'].values
    distance2 = file_2['Distance'].values
    name2 = file_2['Intersection_Name'].values
    #processing file_2

    for i in range(len(file_1)):
        if coordinate1[i] not in coordinates:
            coordinates.append(coordinate1[i])
            name.append(name1[i])

    for j in range(len(file_2)):
        if coordinate2[j] not in coordinates:
            coordinates.append(coordinate2[j])
            name.append(name2[j])
    
    n = len(coordinates)
    # using linked-list
    vertex_llist = []
    pre = -1
    for r in range(len(file_1)):
        v = file_1['NodeID'].values[r]
        if v != pre:
            head = Solution(v, 0)  # edge for vertice itslef is set to 0
            vertex_llist.append(head)
            ajv = Solution(file_1['ConnectedNodeID'].values[r], distance1[r])
            head.next = ajv
            tail = ajv
        elif v == pre:
            curr = Solution(file_1['ConnectedNodeID'].values[r], distance1[r])
            tail.next = curr
            tail = curr
        pre = v

    n1 = len(vertex_llist)

    for r in range(len(file_2)):
        v = coordinates.index(coordinate2[r])
        if v != pre and v >= n1:
            head = Solution(v, 0)  
            # edge for vertice itslef is set to 0
            vertex_llist.append(head)
            tmp = np.where(file_2['NodeID'].values == file_2['ConnectedNodeID'].values[r])
            ajv = Solution(coordinates.index(coordinate2[tmp[0][0]]), distance2[r])
            head.next = ajv
            tail = ajv
        elif v == pre:
            tmp = np.where(file_2['NodeID'].values == file_2['ConnectedNodeID'].values[r])
            curr = Solution(coordinates.index(coordinate2[tmp[0][0]]), distance2[r])
            tail.next = curr
            tail = curr
        else:  
        # if the vertice is already in vertex_llist
            for node in vertex_llist:
                if node.vertice == v:
                    tail = node
                    break
            while tail.next:
                tail = tail.next
            tmp = np.where(file_2['NodeID'].values == file_2['ConnectedNodeID'].values[r])
            curr = Solution(coordinates.index(coordinate2[tmp[0][0]]), distance2[r])
            tail.next = curr
            tail = curr
        pre = v
        
    print('\nThe total distance for linked list is:', kruskal(vertex_llist))
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2. ** 20
    print()
    print('Memory use:', '%.2f' % memoryUse, 'MB')
    print()