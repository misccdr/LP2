def isSafe(graph, colors, vertex, color):
    # Check if any adjacent vertices have the same color
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False

    # It is safe to color the vertex with the given color
    return True


def solveGraphColoring(graph, m, colors, vertex):
    # If all vertices are colored, return True3
    if vertex == len(graph):
        return True

    # Try assigning a color to the current vertex
    for color in range(1, m + 1):
        if isSafe(graph, colors, vertex, color):
            colors[vertex] = color

            # Recursively color the remaining vertices
            if solveGraphColoring(graph, m, colors, vertex + 1):
                return True

            # If assigning the color to the current vertex doesn't lead to a solution,
            # backtrack and try the next color
            colors[vertex] = 0

    # If no color can be assigned to the current vertex, return False
    return False


n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of colors: "))

graph = []
print("Enter the adjacency matrix:")
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

colors = [0] * n

if solveGraphColoring(graph, m, colors, 0):
    print("Solution:", end=" ")
    for color in colors:
        print(color, end=" ")
    print()
else:
    print("No solution found!")
