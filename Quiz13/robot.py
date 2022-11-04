def robot(distance):
    if backtrack(steps, distance):
        if distance == 0:
            res.append(steps[:])
        else:
            for i in range(1, 4):
                steps.append(i)
                robot(distance - i)
                steps.pop()


def backtrack(steps, distance):
    if distance < 0:
        return False

    for i in range(len(steps) - 1):
        if steps[i] > steps[i + 1]:
            return False

    return True


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    for n in nums:
        steps = []
        res = []
        robot(n)
        print()
        print(res)
