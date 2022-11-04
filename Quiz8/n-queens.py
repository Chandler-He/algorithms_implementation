#test case 4,8,10,12

def n_queens(i):
    global outputs
    if promising(i):
        if i == k-1:
            outputs += 1
        else:
            for j in range(k):
                col[i + 1] = j
                n_queens(i + 1)

def promising(i):
    s = 0
    switch = True
    while s < i and switch:
        if col[i] == col[s] or abs(col[i] - col[s]) == i - s:
            switch = False
        s += 1
    return switch

if __name__ == "__main__":
    testcase = [4,8,10,12]
    for k in testcase:
        outputs = 0
        col = [-1] * k
        n_queens(-1)
        print(outputs)

