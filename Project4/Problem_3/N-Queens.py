import numpy as np

def n_queens_3D(Q, i, j, k):
    if Promising(Q, i, j, k):
        if Q == n:
            dp = np.zeros((n, n, n), dtype = int)

            for q in range(1, n+1):
                dp[queens[q][0]][queens[q][1]][queens[q][2]] = 1
            dp = dp.tolist()
            if dp not in results:
                results.append(dp)
            # global solutions
            # solutions = solutions+1

        else:
            Q += 1
            for z in range(k, n):
                for x in range(n):
                    for y in range(n):
                        #nested coordinates
                        queens[Q] = [x, y, z]
                        n_queens_3D(Q, x, y, z)


def Promising(Q, x, y, z):
    for q in range(1, Q):
        i, j, k = queens[q][0], queens[q][1], queens[q][2]

        # Case1: when two queens are in the same layer
        if z == k:        
            if x == i or y == j or abs(x-i) == abs(y-j):
                return False
                
        # Case2: When two queens are in different layers
        else:  
            if x == i and y == j:
                return False
            elif abs(x-i) == abs(z-k) or abs(y-j) == abs(z-k):
                return False

    return True


if __name__ == '__main__':
    test = [2, 3, 4, 5]
    for n in test:
        solutions = 0
        queens = np.zeros((n+1, 3), dtype = int)  
        # store x,y,z coordinates of nth queen
        results = []
        n_queens_3D(0, 0, 0, 0)
        print('The number of legal Q configurations for Q={} is:'.format(n), len(results))
