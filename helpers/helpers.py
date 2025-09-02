import random

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