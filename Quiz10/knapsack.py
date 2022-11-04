def Knapsack(w, prof, Weight):
    include = ['no'] * len(w)
    maxProfit = [0]
    bestset = [[]]
    
    def knapsack(i, profit, weight):
        if(weight <= Weight) & (profit > maxProfit[0]):
            maxProfit[0] = profit
            bestset[0] = include[:]
        if promising(i, profit, weight):
            include[i+1] = 'Yes'
            knapsack(i+1, profit + prof[i+1], weight + w[i+1])
            include[i+1] = 'No'
            knapsack(i + 1, profit, weight)

    def promising(i, profit, weight):
        if weight >= Weight:
            return False
        else:
            totalWeight = weight
            bound = profit
            j = i+1

            while j < len(w):
                if totalWeight + w[j] <= Weight:
                    totalWeight = totalWeight + w[j]
                    bound = bound + prof[j]
                else:
                    break

                j = j+1
            if j < len(w):
                bound = bound + (Weight - totalWeight) * prof[j] / w[j]
            return bound > maxProfit[0]
    
    knapsack(-1, 0, 0)
    return maxProfit[0], bestset[0]

if __name__ == '__main__':
    maxProfit, bestset = Knapsack([2, 5, 7, 3, 1], [20, 30, 35, 12, 3], 9)
    print()
    print('The maximum profit is:', maxProfit)
    print()
    print('The best set for each items are:', bestset)
    print()