def BackTracking(pre, curr):
    if len(curr) == n:
        res.append(curr[ : ])
        return

    for i in range(pre, m):
        curr.append(hashset[i])
        BackTracking(i + 1, curr)
        curr.pop()


if __name__ == '__main__':
    testcase = [3, 5, 7]
    for m in testcase:
        hashset = list(range(1, m + 1))
        res = []
        for n in range(m + 1):
            BackTracking(0, [])
        print()
        print(res)
        print()
        print('Total Subset Count:', len(res))
        print()