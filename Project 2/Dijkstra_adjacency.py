import time
import os
import psutil
import pandas as pan

arr = 2**32
#def arr boundary size

def Dijxstra(matrix, start = 0, end = -1):
    #starting node from the first value and end node from the the last value
    global arr
    min_dist = []
    temp = []
    
    min_dist.extend(matrix[start])
    temp.extend(matrix[start])
    temp[start] = arr
    #def the size of temp array
    passed_node = [start]
    #def the node which were traversed
    parent_node = [start] * len(matrix)
    
    while len(passed_node) < len(matrix):
        #def boundary
        i = temp.index(min(temp))
        temp[i] = arr
        
        if end != -1 and i == end:  
        # choose the start and end node
            Paths(start, end, parent_node)
            
        passed_node.append(i)
        for j in range(len(matrix)):
            if j not in passed_node:
                if (min_dist[i] + matrix[i][j]) < min_dist[j]:
                    #judge the boundary of minimum distance
                    min_dist[j] = temp[j] = min_dist[i] + matrix[i][j]
                    parent_node[j] = i
                    #update
    return min_dist   
    


def Paths(start, end, parent_node):
    path = []
    path.append(str(end))
    x = end

    while parent_node[x] != start:
        #judge if the parent node is not from the start, then
        path.append(str(parent_node[x]))
        x = parent_node[x]
        
    path.append(str(start))
    path.reverse()
    #reverse the new stored path
    print("Shortest Path")
    print("Test Cases 1 - 3 respectively:\n")
    print('Start '+str(start)+' End '+str(end) + ':', '---->'.join(path))
    print()


def main():
    global arr
    
    file = pan.read_csv('Project2_Input_Files/Project2_Input_File1.csv', usecols=[0, 1, 2]) 
    f = file
    
    node1 = f['NodeID'].values
    node2 = f['ConnectedNodeID'].values
    dist = f['Distance'].values
    n = f['NodeID'].values[-1] + 1
    
    #time calculaion
    start = time.process_time()
    adjacent_martix = [[arr] * n for x in range(n)]
    #def a two-dimension array
    for k in range(len(f)):
        adjacent_martix[node1[k]][node2[k]] = dist[k]
    #Dijxstra(adjacent_martix, 197, 27)
    #Dijxstra(adjacent_martix, 65, 280)
    #Dijxstra(adjacent_martix, 187, 68)
    for node in range(n):
        Dijxstra(adjacent_martix, node)
    end = time.process_time()
    total = end - start
    print('time consumption:', '%.2f' % total, 's')
    
    #memory calculation
    pid = os.getpid()
    mem = psutil.Process(pid)
    M = mem.memory_info()[0] / 2. ** 20
    print('RAM useage:', '%.2f' % M, 'MB')
main()




