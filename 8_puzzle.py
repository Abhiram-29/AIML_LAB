import copy
from heapq import heappush, heappop
n = 3
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]
class PriorityQueue:
    def __init__(self):
        self.heap = []
    def push(self, k):
        heappush(self.heap, k)
    def pop(self):
        return heappop(self.heap)
    def empty(self):
        return len(self.heap) == 0
class Node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level
    def __lt__(self, nxt):
        return self.cost < nxt.cost
def calculate_cost(mat, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0 and mat[i][j] != final[i][j]:
                count += 1
    return count
def manhattan_distance(mat, final) -> int:
    distance = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                for x in range(n):
                    for y in range(n):
                        if final[x][y] == mat[i][j]:
                            distance += abs(x - i) + abs(y - j)
                            break
    return distance
def new_node(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final, use_manhattan):
    new_mat = copy.deepcopy(mat)
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    if use_manhattan:
        cost = manhattan_distance(new_mat, final)
    else:
        cost = calculate_cost(new_mat, final)
    return Node(parent, new_mat, new_empty_tile_pos, cost, level)
def print_matrix(mat):
    for i in range(n):
        for j in range(n):
            print(f"{mat[i][j]} ", end=" ")
        print()
def is_safe(x, y):
    return 0 <= x < n and 0 <= y < n
def print_path(root):
    if root is None:
        return
    print_path(root.parent)
    print_matrix(root.mat)
    print()
def solve(initial, final, empty_tile_pos, use_manhattan=False):
    pq = PriorityQueue()
    if use_manhattan:
        cost = manhattan_distance(initial, final)
    else:
        cost = calculate_cost(initial, final)
    root = Node(None, initial, empty_tile_pos, cost, 0)
    pq.push(root)
    while not pq.empty():
        minimum = pq.pop()
        if minimum.cost == 0:
            print_path(minimum)
            return
        for i in range(4):
            new_tile_pos = [minimum.empty_tile_pos[0] + row[i], 
                            minimum.empty_tile_pos[1] + col[i]]
            if is_safe(new_tile_pos[0], new_tile_pos[1]):
                child = new_node(minimum.mat, minimum.empty_tile_pos, 
                        new_tile_pos, minimum.level + 1, minimum, final, use_manhattan)
                pq.push(child)
def get_matrix_input(name):
    print(f"Enter the {name} matrix (3x3):")
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix
def find_empty_tile(matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                return [i, j]
initial = get_matrix_input("initial")
final = get_matrix_input("final")
empty_tile_pos = find_empty_tile(initial)
solve(initial, final, empty_tile_pos, use_manhattan=True)