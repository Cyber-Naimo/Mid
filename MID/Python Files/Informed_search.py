# -*- coding: utf-8 -*-
"""Q4_Informed_Search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GMajNsEwXWjG3PhtWdCKvBr2DMTMIX4L
"""

from queue import PriorityQueue

graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('C', 4), ('D', 1)],
    'B': [('H', 5)],  # Add a path from 'B' to 'H' with cost 5
    'C': [],
    'D': [],
    'H': []   # Add an empty list for node 'H'
}

heuristic_table = {
    'A': 12,
    'B': 4,
    'C': 0,
    'D': 0,
    'H':0
}

def gbfs(graph, startnode, goalnode):
    visited = set()  # Initialize an empty set to store visited nodes
    queue = PriorityQueue()
    queue.put((0, startnode))
    pathcost = 0

    while not queue.empty():  # Check if the queue is not empty
        currentnode = queue.get()
        pathcost += currentnode[0]
        currentnode = currentnode[1]

        if currentnode == goalnode:
            print(currentnode)
            print("path Cost: {0}".format(pathcost))
            return
        else:
            print(currentnode, end=' ->')
        if currentnode not in graph:
            continue
        visited.add(currentnode)  # Mark the current node as visited
        for neighboredge in graph[currentnode]:
            neighbor = neighboredge[0]
            heuristic_value = heuristic_table[neighbor]

            if neighbor not in visited:
                queue.put((heuristic_value, neighbor))

    print("Goal node not found!")  # Print a message if the goal node is not found

gbfs(graph, 'S', 'H')

from queue import PriorityQueue
graph = {
    'S': [('A',1), ('G',10)],
    'A': [('B',2), ('C',1)],
    'B': [('D',5)],
    'C': [('D',3),('G',4)],
    'D': [('G',2)],
    'G': None

  }

heuristic_table = {
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'S': 5,
    'G': 0

}
def Astar(graph, startnode, goalnode, heuristic_table):
    visited = set()  # closed list
    queue = PriorityQueue()
    queue.put((0, startnode, [startnode]))  # tuple of (path cost, node, path)

    while not queue.empty():
        path_cost, current_node, path = queue.get()

        if current_node == goalnode:
            print("Path:", ' -> '.join(path))
            print("Path Cost:", path_cost)
            return

        if current_node in visited:
            continue

        visited.add(current_node)

        if graph[current_node] is None:
            continue

        for neighbor, cost in graph[current_node]:
            heuristic_value = heuristic_table[neighbor]
            new_path_cost = path_cost + cost
            new_path = path + [neighbor]
            total_cost = new_path_cost + heuristic_value
            if neighbor not in visited:
                queue.put((new_path_cost, neighbor, new_path))

    print("Goal node unreachable")
Astar(graph,'S','D',heuristic_table)

maze = [[0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 'B'],
        [0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 12, 0, 10, 9, 8, 7, 6, 5, 4, 0, 2],
        [0, 13, 0, 11, 0, 0, 0, 0, 0, 5, 0, 3],
        [0, 14, 13, 12, 0, 10, 9, 8, 7, 6, 0, 4],
        [0, 0, 0, 13, 0, 11, 0, 0, 0, 0, 0, 5],
        ['A', 16, 15, 14, 0, 12, 11, 10, 9, 8, 7, 6]]

graph = {}
start = None
goal = None
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 'A':
            start = (i, j)
        elif maze[i][j] == 'B':
            goal = (i, j)

        if maze[i][j] != '*' and maze[i][j] != 0:
            neighbors = []
            if i > 0 and maze[i-1][j] != '*' and maze[i-1][j] != 0:
                neighbors.append((i-1, j))
            if i < len(maze)-1 and maze[i+1][j] != '*' and maze[i+1][j] != 0:
                neighbors.append((i+1, j))
            if j > 0 and maze[i][j-1] != '*' and maze[i][j-1] != 0:
                neighbors.append((i, j-1))
            if j < len(maze[i])-1 and maze[i][j+1] != '*' and maze[i][j+1] != 0:
                neighbors.append((i, j+1))
            graph[(i,j)] = neighbors



# Greedy Best First Search algorithm
from queue import PriorityQueue

def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def greedy_best_first(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            break

        for next_node in graph[current]:
            if next_node not in came_from:
                priority = heuristic(next_node, goal)
                frontier.put((priority, next_node))
                came_from[next_node] = current

    # reconstructing the path and calculating the cost
    path = []
    current = goal
    total_cost = 0  # We don't have to calculate total cost for Greedy Best First Search
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Running
greedy_path = greedy_best_first(graph, start, goal)
print("Greedy Best First Search Path:", greedy_path)





















# A* Search algorithm
from queue import PriorityQueue

def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def astar_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            break

        for next_node in graph[current]:
            new_cost = cost_so_far[current] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node, goal)
                frontier.put((priority, next_node))
                came_from[next_node] = current

    # reconstructing the path and calculating the  cost
    path = []
    current = goal
    total_cost = 0
    while current != start:
        path.append(current)
        total_cost += 1
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path, total_cost

# Running
astar_path, total_cost = astar_search(graph, start, goal)
print("A* Search Path:", astar_path)
print("Total Cost:", total_cost)