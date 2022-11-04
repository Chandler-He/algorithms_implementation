import numpy as np
import os
import pandas as pd
import psutil

arr = 2**16

def edge(x):
    edgeLists = []
    #def an array to store the edges
    n = np.shape(x)[0]
    for i in range(n):
        for j in range(n):
            if i < j:
                edgeLists.append((x[i][j], i, j))
    edgeLists.sort()
    return edgeLists


def kruskal(x):
    n = np.shape(x)[0]
    m = list(range(n))

    edgeLists = edge(x)
    #recall the function
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
    print('Node\t', 'Node\t', 'Distance\t')
    while len(result) < n-1:
        (long, vertice_small, vertice_big) = edgeLists[j]
        q = find(vertice_small)
        p = find(vertice_big)

        if q != p:
            merge(p, q)
            result.append(edgeLists[j])
            print(vertice_small,'\t', vertice_big,'\t',long)
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
    #read file1
    file_2 = pd.read_csv('Project3_G2_Data.csv')
    coordinate2 = file_2['Coordinates'].values
    distance2 = file_2['Distance'].values
    name2 = file_2['Intersection_Name'].values
    #read file2

    for i in range(len(file_1)):
        if coordinate1[i] not in coordinates:
            coordinates.append(coordinate1[i])
            name.append(name1[i])

    for j in range(len(file_2)):
        if coordinate2[j] not in coordinates:
            coordinates.append(coordinate2[j])
            name.append(name2[j])

    n = len(coordinates)
    # using a two-dimensional array
    adjacency = [[arr] * n for x in range(n)]

    for i in range(len(file_1)):
        adjacency[file_1['NodeID'].values[i]][file_1['ConnectedNodeID'].values[i]] = distance1[i]

    for j in range(len(file_2)):
        tmp = np.where(file_2['NodeID'].values == file_2['ConnectedNodeID'].values[j])
        adjacency[coordinates.index(coordinate2[j])][coordinates.index(coordinate2[tmp[0][0]])] = distance2[j]
    
    print('\nTotal distance with adjacency matrix:', kruskal(adjacency))
    pid = os.getpid()
    py = psutil.Process(pid)
    memUsage = py.memory_info()[0] / 2. ** 20
    print()
    print('Memory use:', '%.2f' % memUsage, 'MB')
    print()