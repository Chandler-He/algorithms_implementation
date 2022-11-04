import time
import os
import psutil
import pandas as pan

arr = 2**32
#def arr boundary size


class Solution:
    #def a class for storing the vertices and edges
    def __init__(self, vertices, edge):
        self.vertices = vertices
        self.edge = edge
        self.next = None

def Floyd_linklist(linklist):
    length = len(linklist)
    min_len = [[arr] * length for i in range(length)]
    #def minimum length got the matrix
    for i in range(length):
        for j in range(length):
            min_len[i][j] = distance(i, j, linklist)
            #calculate min_len and update it 
    
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if (min_len[i][k] + min_len[k][j]) < min_len[i][j]:
                    min_len[i][j] = min_len[i][k] + min_len[k][j]
                    prev[i][j] = prev[k][j]
    return min_len

def Path(start, end, parent_path):
    path = []
    #def paths as an empty sets
    path.append(str(end))

    while parent_path[start][end] != start:
        #gudge if the parent path end not the start, append the new array
        path.append(str(parent_path[start][end]))
        end = parent_path[start][end]
    path.append(str(start))
    path.reverse()
    print("Shortest Path")
    print("Test Cases 1 - 3 respectively:\n")
    print('Start '+str(start)+' End '+str(end) + ':', '---->'.join(path))
    print()


def distance(m, n, linklist):
    global arr
    head = linklist[m]
     #def a linklist and assign the node head
    p = head.next
    while p:
        if p.vertices == n:
            return p.edge
        else:
            p = p.next
    return arr



if __name__ == '__main__':
    start = time.process_time()

    file = pan.read_csv('Project2_Input_Files/Project2_Input_File10.csv', usecols=[0, 1, 2])
    f = file
    node1 = f['NodeID'].values
    node2 = f['ConnectedNodeID'].values
    dist = f['Distance'].values
    n = f['NodeID'].values[-1] + 1
    
    vertices_linklist = []
    last = -1
    prev = [[i] * n for i in range(n)]

    for i in range(len(f)):
        N = node1[i]
    
        if N != last:
            head = Solution(N, 0)  
            #vertices are to 0
            vertices_linklist.append(head)

            floyd_linklist = Solution(node2[i],dist[i])
            head.next = floyd_linklist
            end = floyd_linklist
            #update the nodes
        elif N == last:
            curr = Solution(node2[i], dist[i])
            end.next = curr
            end = curr
        last = N
        #update last val as N

    Floyd_linklist(vertices_linklist)
    Path(197, 27, prev)
    Path(65, 280, prev)
    Path(187,68, prev)

    end = time.process_time()
    total = end - start
    print('time usage:', '%.2f' % total, 'S')
    pid = os.getpid()
    mem = psutil.Process(pid)
    memory_usage = mem.memory_info()[0] / 2. ** 20
    print('RAM usage:', '%.2f' % memory_usage, 'MB')