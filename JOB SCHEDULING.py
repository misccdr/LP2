def printJobScheduling(arr, n):
    arr.sort(key=lambda x: x[2], reverse=True)

    result = [None] * n
    slot = [False] * n

    for i in range(n):
        for j in range(min(n, arr[i][1])-1, -1, -1):
            if slot[j] == False:
                result[j] = i
                slot[j] = True
                break

    for i in range(n):
        if slot[i] == True:
            print(arr[result[i]][0], end=" ")

jobs = [
    ('j1', 5, 200),
    ('j2', 3, 180),
    ('j3', 3, 190),
    ('j4', 2, 300),
    ('j5', 4, 120),
    ('j6', 2, 100)

]

printJobScheduling(jobs, len(jobs))
