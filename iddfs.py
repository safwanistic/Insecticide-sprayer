import random

def dfs_vacuum_cleaner(room, visited, depth):
    print("Cleaning room", room)

    visited[room] = True

    if depth == 0:
        print("Reached depth limit, backtracking from room", room)
        return

    # Generate random neighboring rooms
    neighbors = random.sample(range(20), 4)

    for neighbor in neighbors:
        if not visited[neighbor]:
            dfs_vacuum_cleaner(neighbor, visited, depth - 1)
            if all(visited):
                return

    visited[room] = False
    print("Backtracking from room", room)

def main():
    # Initialize rooms as dirty
    rooms = [True] * 20

    # Choose a random starting room
    start_room = random.randint(0, 19)
    print("Starting room:", start_room)

    # Mark the starting room as visited
    visited = [False] * 20
    visited[start_room] = True

    # Set the initial depth limit
    depth_limit = 5

    # Clean the rooms using IDDFS
    while not all(visited):
        dfs_vacuum_cleaner(start_room, visited, depth_limit)
        depth_limit += 1

if __name__ == '__main__':
    main()
