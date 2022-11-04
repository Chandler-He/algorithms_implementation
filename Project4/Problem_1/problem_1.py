import pandas as pd

infinite = 9 ** 10

def Floyd(matrix):
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    parents[i][j] = parents[k][j]


def CalBetweeness(ParentPath, matrix):
    btw_ctral = [0] * len(matrix)

    for start in range(len(matrix)):
        for end in range(len(matrix)):
            if start != end and matrix[start][end] < infinite:
                btw_ctral[start] += 1
                btw_ctral[end] += 1
                tmp = end
                while ParentPath[start][tmp] != start:
                    k = ParentPath[start][tmp]
                    btw_ctral[tmp] += 1
    return btw_ctral


if __name__ == '__main__':
    file = pd.read_csv('Project 4_Problem 1_InputData.csv', usecols=[0, 1, 2])
    f = file
    node1 = f['NodeID'].values
    node2 = f['ConnectedNodeID'].values
    distance = f['Distance'].values
    n = f['NodeID'].values[-1] + 1

    adjacency = [[infinite] * n for x in range(n)]
    parents = [[i] * n for i in range(n)]

    for r in range(len(f)):
        adjacency[node1[r]][node2[r]] = distance[r]
    
    Floyd(adjacency)
    btwness = CalBetweeness(parents, adjacency)
    
    print('The top 20 btwness centrality vertices in the road network are:')
    for i in range(20):
        max_node = btwness.index(max(btwness))
        print(max_node, end=',')
        btwness[max_node] = -1