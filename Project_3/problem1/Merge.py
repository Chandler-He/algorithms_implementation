import pandas as pd
import numpy as np
import os
import psutil

arr = 2 ** 16

class Node(object):
    def __init__(self, vertices, edge):
        self.vertices = vertices
        self.edge = edge
        self.next = None


if __name__ == '__main__':
    coordinates = []  
    # distinct coordinates for every node
    name = []  
    
    file1 = pd.read_csv('Project3_G1_Data.csv')
    coordinate1 = file1['Coordinates'].values
    distance1 = file1['Distance'].values
    name1 = file1['Intersection_Name'].values

    file2 = pd.read_csv('Project3_G2_Data.csv')
    coordinate2 = file2['Coordinates'].values
    distance2 = file2['Distance'].values
    name2 = file2['Intersection_Name'].values

    for i in range(len(file1)):
        if coordinate1[i] not in coordinates:
            coordinates.append(coordinate1[i])
            name.append(name1[i])

    for j in range(len(file2)):
        if coordinate2[j] not in coordinates:
            coordinates.append(coordinate2[j])
            name.append(name2[j])

    n = len(coordinates)
    # using a two-dimensional array
    adjacency = [[arr] * n for i in range(n)]
    for i in range(len(file1)):
        adjacency[file1['NodeID'].values[i]][file1['ConnectedNodeID'].values[i]] = distance1[i]

    for j in range(len(file2)):
        tmp = np.where(file2['NodeID'].values == file2['ConnectedNodeID'].values[j])
        adjacency[coordinates.index(coordinate2[j])][coordinates.index(coordinate2[tmp[0][0]])] = distance2[j]

    # using linked-list
    vertic_linkedlist = []
    pre = -1
    #set start val

    for r in range(len(file1)):
        node = file1['NodeID'].values[r]
        if node != pre:
            head = Node(node, 0)  
            # edge for vertices itslef is set to 0
            vertic_linkedlist.append(head)
            N = Node(file1['ConnectedNodeID'].values[r], distance1[r])
            head.next = N
            tail = N
        elif node == pre:
            curr = Node(file1['ConnectedNodeID'].values[r], distance1[r])
            tail.next = curr
            tail = curr
        pre = node

    n1 = len(vertic_linkedlist)
    for r in range(len(file2)):
        node = coordinates.index(coordinate2[r])
        if node != pre and node >= n1:
            head = Node(node, 0)  
            # edge for vertices itslef is set to 0
            vertic_linkedlist.append(head)
            tmp = np.where(file2['NodeID'].values == file2['ConnectedNodeID'].values[r])
            N = Node(coordinates.index(coordinate2[tmp[0][0]]), distance2[r])
            head.next = N
            tail = N
        elif node == pre:
            tmp = np.where(file2['NodeID'].values == file2['ConnectedNodeID'].values[r])
            curr = Node(coordinates.index(coordinate2[tmp[0][0]]), distance2[r])
            tail.next = curr
            tail = curr
        else:  
            # if the vertices is already in vertic_linkedlist
            for node in vertic_linkedlist:
                if node.vertices == node:
                    tail = node
                    break
            while tail.next:
                tail = tail.next
            tmp = np.where(file2['NodeID'].values == file2['ConnectedNodeID'].values[r])
            curr = Node(coordinates.index(coordinate2[tmp[0][0]]), distance2[r])
            tail.next = curr
            tail = curr
        pre = node

    print(adjacency, vertic_linkedlist)
    pid = os.getpid()
    py = psutil.Process(pid)
    usage = py.memory_info()[0] / 2. ** 20
    print()
    print('Memory use:', '%.2f' % usage, 'MB')