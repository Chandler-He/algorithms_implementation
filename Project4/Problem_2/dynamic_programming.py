import pandas as pd
infinite = 9 ** 100

def travel_sales_person1(array):  
    # assume the start node is node 0
    dp = [[infinite] * (2 ** (n-1)) for i in range(n)]  
    # dp matrix, n x 2^(n-1), use binary to represent all subsets
    for i in range(n):  
        # fill in the first column dp[][0]
        if i == 0:  
            # doesn't store matrix[i][i]
            dp[0][0] = infinite
        else:
            dp[i][0] = array[int((i * (i-1)) / 2)]  
            # start node, without passing any other nodes

    for j in range(1, 2 ** (n-1)):  
        # fill in the other columns except dp[][0] in dp
        for i in range(n):  
            # for every row
            if i != 0 and ((j >> (i-1)) & 1) == 1:  
                # if already reached node.Eg: dp[1][{1,3}], no w[3][1]+dp[1][{1}]
                continue

            for k in range(1, n):  
                # try every other nodes, see whether can go to node k first
                if ((j >> (k - 1)) & 1) == 0:  
                    # can't reach node k first
                    continue
                if i == k:
                    distance = infinite
                elif i < k:
                    distance = array[int((k * (k - 1))/2 + i)]
                else: distance = array[int((i * (i - 1))/2 + k)]
                # dp[0][{1, 2, 3}] = min{C01 + dp[1][{2, 3}] ，C02 + dp[2][{1, 3}] ，C03 + dp[3][{1, 2}]}
                if dp[i][j] > distance + dp[k][j ^ (1 << (k-1))]:
                    dp[i][j] = distance + dp[k][j ^ (1 << (k-1))]
        

def travel_sales_person2(matrix):  
    # assume the start node is node 0
    n = len(matrix)
    dp = [[infinite] * (2 ** (n-1)) for i in range(n)]  
    # dp matrix, n x 2^(n-1), use binary to represent all subsets
     
    for i in range(n):  
        # fill in the first column dp[][0]
        dp[i][0] = matrix[i][0]  
        # from node i to start node directly, without passing any other node

    for j in range(1, 2**(n-1)):  
        # fill in the other columns except dp[][0] in dp
        for i in range(n):  
            # for every row
            if i != 0 and ((j >> (i-1)) & 1) == 1:  
                # if already reached node.Eg: dp[1][{1,3}], no w[3][1]+dp[1][{1}]
                continue
            for k in range(1, n):  
                # try every other nodes, see whether can go to node k first
                if ((j >> (k-1)) & 1) == 0:  
                    # can't reach node k first
                    continue
                # dp[0][{1, 2, 3}] = min{C01 + dp[1][{2, 3}] ，C02 + dp[2][{1, 3}] ，C03 + dp[3][{1, 2}]}
                if dp[i][j] > matrix[i][k] + dp[k][j ^ (1 << (k-1))]:
                    dp[i][j] = matrix[i][k] + dp[k][j ^ (1 << (k-1))]
        print(2 ** (n - 1) - j)
    return dp[0][2 ** (n - 1) - 1]





if __name__ == '__main__':
    file = pd.read_csv('Project 4_Problem 2_InputData.csv', usecols=[0, 1, 2])
    f = file
    node1 = f['NodeID'].values
    node2 = f['ConnectedNodeID'].values
    distance = f['Distance'].values
    n = f['NodeID'].values[-1] + 1

    adjac1 = [infinite] * (int((n * (n-1))/2))
    adjac2 = [[infinite] * n for x in range(n)]
    for r in range(len(f)):
        adjac2[node1[r]][node2[r]] = distance[r]
        if node1[r] > node2[r]:
            adjac1[int((node1[r] * (node1[r] - 1))/2 + node2[r])] = distance[r]
    print()

    #print('The minimum distance is:', travel_sales_person1(adjac1))
    print('The minimum distance is:', travel_sales_person2(adjac2))
    print()