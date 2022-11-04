import time
import os
import psutil
import pandas as pan

arr = 2**32
#def arr boundary size

class Solution:
    #init link list
    def __init__(self, vertice, edge):
        self.vertice = vertice
        self.edge = edge
        self.next = None


def Dijkstra(linklist, start = 0, end = -1):
    global arr
    #starting node from the first value and end node from the the last value
    leng = len(linklist)
    temp = []
    #def a temp array to store the nodes
    min_len = []
    #def a minimum array length to do comparasion
    
    for i in range(leng):
        min_len.append(distance(start, i, linklist))
        temp.append(distance(start, i, linklist))
    
    temp[start] = arr
    traversed = [start]
    parent_path = [start] * leng

    while len(traversed) < leng:
        i = temp.index(min(temp))
        temp[i] = arr

        if end != -1 and i == end:  
            path(start, end, parent_path)
        #print the shorest path between start and end node.
        traversed.append(i)
        for j in range(leng):
            if j not in traversed:
                if (min_len[i] + distance(i, j, linklist)) < min_len[j]:
                    min_len[j] = temp[j] = min_len[i] + distance(i, j, linklist)
                    parent_path[j] = i
    return min_len   
    # min_dis stores the leng of shortest 
    # path from start node to each other nodes



def distance(m, n, linklist):
    global arr
    head = linklist[m]
    #def a linklist and assign the node head
    p = head.next
    while p:
        if p.vertice == n:
            return p.edge
        else:
            p = p.next
    return arr


def path(start, end, parent_path):
    path = []
    path.append(str(end))
    #calculate the shorest path and print
    while parent_path[end] != start:
        path.append(str(parent_path[end]))
        end = parent_path[end]
    path.append(str(start))
    path.reverse()
    print("Shortest Path")
    print("Test Cases 1 - 3 respectively:\n")
    print('Start '+str(start)+' End '+str(end) + ':', '---->'.join(path))
    print()
    


def main():
    start = time.process_time()
    file = pan.read_csv('Project2_Input_Files/Project2_Input_File3.csv', usecols=[0, 1, 2])
    f = file
    node1 = f['NodeID'].values
    node2 = f['ConnectedNodeID'].values
    dis = f['Distance'].values
    n = f['NodeID'].values[-1] + 1
    linkedlist = []
    #def a empty linkedlist
    prev = -1
    #from the end node
    for i in range(len(f)):
        N = node1[i]
        if N != prev:
            head = Solution(N, 0)  
            #set the vertice for 0
            linkedlist.append(head)
            li = Solution(node2[i],dis[i])
            #def li and recall from the Solution class
            head.next = li
            end = li
        elif N == prev:
            curr = Solution(node2[i], dis[i])
            end.next = curr
            end = curr
        prev = N

    Dijkstra(linkedlist, 197, 27)
    Dijkstra(linkedlist, 65, 280)
    Dijkstra(linkedlist, 187, 68)

    for k in range(n):
        Dijkstra(linkedlist, k)

    end = time.process_time()
    total = end - start

    print('time usage:', '%.2f' % total, 'S')
    pid = os.getpid()
    me = psutil.Process(pid)
    memory_usage = me.memory_info()[0] / 2. ** 20
    print('RAM consumption:', '%.2f' % memory_usage, 'MB')
    
main()