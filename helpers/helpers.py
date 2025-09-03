import random
import pdb

def hit_roll(percentage):
    if percentage > 100.0:
        return False
    return random.randint(1,100) <= (percentage * 100)

def path_exists(board, start, target, queue=None, visited=None):
        if queue is None and visited is None:
            queue = [start]
            visited = []
        current_tile = queue[0]
        if current_tile == target:
            return True
        for neighbor in current_tile.neighbors:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
        visited.append(queue.pop(0))
        if len(queue) == 0:
            return False
        return path_exists(board, start, target, queue, visited)

def shortest_path_start(start, target, queue=None, visited=None):
    if queue is None:
        queue = [start]
        path = {}
        visited = []
    if start == target:
        return path[1]
    current_tile = queue.pop(0)
    visited.append(current_tile)
    for neighbor in current_tile.neighbors:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)
            path[neighbor] = current_tile
    shortest_path_start(queue[0], target, queue, visited)

def find_parent(start, target, parent_map):
    path = [target]
    parent = parent_map[target]
    while parent != start:
        path.append(parent)
        parent = parent_map[parent]
    path += [parent]
    path.reverse()
    return path

    

    