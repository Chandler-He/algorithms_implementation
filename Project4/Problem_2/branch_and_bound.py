import pandas as pd
infinite  = 9 ** 100

def travel_sales_person1(array):
    def completion(s1, s2):  
        # get the set of s2-s1, return a list
        s = []
        for i in s2:
            if i not in s1:
                s.append(i)
        return s

    def length(path):  
        # return the length of a path
        sum = 0
        for i in range(len(path) - 1):
            sum += distance(path[i], path[i+1])
        return sum

    def distance(m, n):  
        # return the distance between node m and node n
        if m == n:
            return infinite
        elif m < n:
            return array[int((n * (n-1))/2 + m)]
        else:
            return array[int((m * (m - 1))/2 + n)]

    

    def minBound(queue):  
        # find the node with the smallest bound
        min = infinite
        min_index = 0

        for item_index in range(len(queue)):
            if queue[item_index][2] < min:
                min = queue[item_index][2]
                min_index = item_index
        return min_index

    def bound(path):
        b1 = length(path)
        others_point = completion(path, all_nodes)
        b2 = min([distance(path[-1], j) for j in others_point])
        b3 = 0
        for i in others_point:
            s = []
            for j in others_point:
                if i != j:
                    s.append(distance(i, j))
            b3 = b3 + min(min(s), distance(i, 0))
        return b1 + b2 + b3

    all_nodes = list(range(n))
    tmp = [[0, [0], bound([0])]] 
    
    optimal_path = []  
    # the optimal path
    minlen = infinite  
    # the minimum length
    while tmp:
        min_bound_index = minBound(tmp)
        level1, path1, bound1 = tmp[min_bound_index]
        tmp.pop(min_bound_index)  

        # find the node with smallest bound and pop it
        if bound1 < minlen:  
            # if this node is promising
            level2 = level1+1  
            # expand the node, next level
            for i in range(1, n):  
                # generate all its children, except the start node 0
                if i not in path1:
                    path2 = path1+[i]
                    if level2 == n-2:  
                        # already reach the leaf, the final node is determined
                        path2.extend(completion(path2, all_nodes))  
                        # put [the last remaining node] at the end
                        path2.append(0)  
                        # then put start node at the end
                        if length(path2) < minlen:
                            minlen = length(path2)
                            optimal_path = path2
                    else:
                        if bound(path2) < minlen:  
                            # if has not reached the leaf and the node is promising, in queue
                            tmp.append([level2, path2, bound(path2)])
    return optimal_path, minlen


def travel_sales_person2(matrix):
    def completion(s1, s2):  
        # return a list of set between s1 and s2
        s = []
        for i in s2:
            if i not in s1:
                s.append(i)
        return s

    def length(path): 
         # return the length of a path
        sum = 0
        for i in range(len(path)-1):
            sum = sum+matrix[path[i]][path[i+1]]
        return sum

    def minBound(queue):  
        # find the node with the smallest bound
        min = infinite
        min_index = 0
        for item_index in range(len(queue)):
            if queue[item_index][2] < min:
                min = queue[item_index][2]
                min_index = item_index
        return min_index

    def bound(path):
        b1 = length(path)
        others_point = completion(path, all_nodes)
        b2 = min([matrix[path[-1]][j] for j in others_point])
        b3 = 0
        for i in others_point:
            s = []
            for j in others_point:
                if i != j:
                    s.append(matrix[i][j])
            b3 = b3 + min(min(s), matrix[i][0])
        return b1 + b2 + b3

    all_nodes = list(range(n))
    tmp = [[0, [0], bound([0])]]  
    # a queue[level, path, bound]
    optimal_path = []  
    # the optimal path
    minlen = infinite  
    # the minimum length
    while tmp:
        min_bound_index = minBound(tmp)
        level1, path1, bound1 = tmp[min_bound_index]
        tmp.pop(min_bound_index)  
        # find the node with smallest bound and pop it
        if bound1 < minlen:  
            # if this node is promising
            level2 = level1+1  
            # expand the node, next level
            for i in range(1, n):  
                # generate all its children, except the start node 0
                if i not in path1:
                    path2 = path1+[i]
                    if level2 == n-2:  
                        # already reach the leaf, the final node is determined
                        path2.extend(completion(path2, all_nodes))  
                        # put [the last remaining node] at the end
                        path2.append(0)  
                        # then put start node at the end
                        if length(path2) < minlen:
                            minlen = length(path2)
                            optimal_path = path2
                    else:
                        if bound(path2) < minlen:  
                            # if has not reached the leaf and the node is promising, in queue
                            tmp.append([level2, path2, bound(path2)])
    return optimal_path, minlen


if __name__ == '__main__':
    file = pd.read_csv('Project 4_Problem 2_InputData.csv', usecols=[0, 1, 2])
    f = file
    node1 = f['NodeID'].values
    node2 = f['ConnectedNodeID'].values
    distance = f['Distance'].values
    n = f['NodeID'].values[-1] + 1

    adja1 = [infinite] * (int((n * (n-1)) / 2))
    adja2 = [[infinite] * n for x in range(n)]

    for r in range(len(f)):
        adja2[node1[r]][node2[r]] = distance[r]
        if node1[r] > node2[r]:
            adja1[int((node1[r] * (node1[r] - 1)) / 2 + node2[r])] = distance[r]
    #shortest_path, min_len = travel_sales_person1(adja1)
    shortest_path, min_len = travel_sales_person2(adja2)
    print()
    print('The shortest path for Two-D array is:', shortest_path)
    print()
    print('The minimum distance is:', min_len)
    print()