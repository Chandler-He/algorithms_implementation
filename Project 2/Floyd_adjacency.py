import time
import os
import psutil
import pandas as pan

arr = 2**32
#def arr boundary size

def Floyd_adjacent(mrtx):
    L = len(mrtx)
    #length of the matrix
    for k in range(L):
        for i in range(L):
            for j in range(L):
                #3 for loop for the textbook
                if (mrtx[i][k] + mrtx[k][j]) < mrtx[i][j]:
                    mrtx[i][j] = mrtx[i][k] + mrtx[k][j]
                    parents[i][j] = parents[k][j]


def Path(start, end, parent_path):
    path = []
    path.append(str(end))

    while parent_path[start][end] != start:
        #gudge if the parent path end not the start, append the new array
        path.append(str(parent_path[start][end]))
        end = parent_path[start][end]
        #update the array

    path.append(str(start))
    path.reverse()
    #reverse the new stored path
    print("Shortest Path")
    print("Test Cases 1 - 3 respectively:\n")
    print('Start '+str(start)+' End '+str(end) + ':', '---->'.join(path))
    print()

if __name__ == "__main__":
    start = time.process_time()
    file = pan.read_csv('Project2_Input_Files/Project2_Input_File3.csv', usecols=[0, 1, 2]) 
    f = file
    
    node1 = f['NodeID'].values
    node2 = f['ConnectedNodeID'].values
    dist = f['Distance'].values
    n = f['NodeID'].values[-1] + 1
    
    adjacent_martix = [[arr] * n for i in range(n)]
    parents = [[j] * n for j in range(n)]
    #traverse the parent paths

    for k in range(len(f)):
        adjacent_martix[node1[k]][node2[k]] = dist[k]
        #update
    Floyd_adjacent(adjacent_martix)
    #recall the function
    Path(197, 27, parents)
    Path(65, 280, parents)
    Path(187,68, parents)
    end = time.process_time()
    total = end - start
    print('time usage:', '%.2f' % total, 'S')

    pid = os.getpid()
    mem = psutil.Process(pid)
    memory_usage = mem.memory_info()[0] / 2. ** 20
    print('RAM use:', '%.2f' % memory_usage, 'MB')
