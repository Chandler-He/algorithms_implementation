def knapsack3(w, p, W_max):
    maxProfit = 0
    nums_visited = 1  
    # set the number of nodes before finding the optimal solution

    def priority_queue_of_node(s):  
        # s = [level, profit, weight, bound_value]
        m = len(queue)
        def insert(low, high):
            if high >= low:
                mid = int((low + high) / 2)
                if s[3] <= queue[mid][3]:
                    insert(mid + 1, high)
                else:
                    insert(low, mid - 1)
            else:
                queue.insert(low, s)
        insert(0, m - 1)

    def bound(level, profit, wght):
        if wght >= W_max:
            return 0
        else:
            expectProfit = profit
            j = level + 1
            totalWeight = wght
            while j < len(w):
                if totalWeight + w[j] <= W_max:
                    totalWeight = totalWeight + w[j]
                    expectProfit = expectProfit + p[j]
                    j += 1
                else:
                    break
            if j < len(w):
                expectProfit = expectProfit + (W_max - totalWeight) * p[j] / w[j]
            return expectProfit

    queue = [[-1, 0, 0, bound(-1, 0, 0)]]  
    # initialize a queue with root. level, profit, weight, bound
    while queue:
        if queue[0][3] > maxProfit:   
            # queue[0][3] means bound

            nums_visited = nums_visited + 2  
            # visit all its children, 2
            level1 = queue[0][0] + 1

            profit1 = queue[0][1] + p[level1]  
            # lchild: pick the next item

            weight1 = queue[0][2] + w[level1]
            bound_value1 = bound(level1, profit1, weight1)

            if (profit1 > maxProfit) & (weight1 <= W_max):
                maxProfit = profit1
                
            profit2 = queue[0][1]  
            # rchild: doesn't pick the next item
            
            weight2 = queue[0][2]
            bound_value2 = bound(level1, profit2, weight2)
            
            del queue[0]
            # pop out the parent nodex
            if bound_value1 > maxProfit:
                priority_queue_of_node([level1, profit1, weight1, bound_value1])
            if bound_value2 > maxProfit:
                priority_queue_of_node([level1, profit2, weight2, bound_value2])
        else:
            del queue[0]

    return maxProfit, nums_visited


if __name__ == '__main__':
    maxProfit, nums_of_nodes = knapsack3([2, 5, 7, 3, 1], [20, 30, 35, 12, 3], 13)
    print()
    print('The max profit is:', maxProfit)
    print()
    print('The number of nodes visited before:', nums_of_nodes,'\n')