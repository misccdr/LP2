V = 7

G = [
[ 0, 5, 1, 4, 0, 0, 0 ],
[ 5, 0, 0, 8, 0, 6, 0 ],
[ 1, 0, 0, 3, 2, 0, 0 ],
[ 4, 8, 3, 0, 0, 8, 0 ],
[ 0, 0, 2, 0, 0, 7, 9 ],
[ 0, 6, 0, 8, 7, 0, 0 ],
[ 0, 0, 0, 0, 9, 0, 0 ]
]

visit = [False] * V
edge = 0

visit[0] = True

print("Edge : Weight")

while edge < V - 1:
    minimum = float('inf')
    x = 0
    y = 0

    for i in range(V):
        if visit[i] == True:
            for j in range(V):
                if visit[j] == False and G[i][j] != 0:
                    if G[i][j] < minimum:
                        minimum = G[i][j]
                        x = i
                        y = j

    print(f"{x} ---> {y} : {G[x][y]}")
    visit[y] = True
    edge += 1
