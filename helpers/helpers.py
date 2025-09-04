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
        return path_exists(board, start, target, queue, visited)\

def shortest_path_start(start, target):
    return shortest_path(start, target)[1]

def shortest_path(start, target, queue=None, visited=None, parent_map=None):
    if queue is None:
        queue = [start]
        visited = set()
        parent_map = {start: None}

    if not queue:
        return None
    
    current_tile = queue.pop(0)
    visited.add(current_tile)

    if current_tile == target:
        return(path(start, target, parent_map))
    
    for neighbor in current_tile.neighbors:
        if neighbor not in visited and neighbor not in queue: 
            queue.append(neighbor)
            parent_map[neighbor] = current_tile 
    
    return shortest_path(start, target, queue, visited, parent_map)

def path(start, target, parent_map):
    if start == target:
        return None
    path = [target]
    parent = parent_map[target]
    while parent != start and parent is not None:
        path.append(parent)
        parent = parent_map[parent]
    path += [parent]
    path.reverse()
    return path

    

    