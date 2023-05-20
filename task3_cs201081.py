import random
import time


def dfs_vacuum_cleaner(room, visitedRooms):
    time.sleep(0.7)
    print("Cleaning room #", room)

    visitedRooms[room] = True

    # Generate random neighboring rooms
    neighbors = random.sample(range(20), 4)

    for neighbor in neighbors:
        if not visitedRooms[neighbor]:
            dfs_vacuum_cleaner(neighbor, visitedRooms)
            time.sleep(.95)
            break
    else:
        print("Backtracking from Room #", room)
        time.sleep(.95)

def main():
    # Initialize rooms as dirty
    rooms = [True] * 20
    print("Vacuum to be placed in any of the 20 rooms")
    time.sleep(.85)
    # Choose a random starting room
    start_room = random.randint(0, 19)
    time.sleep(.85)
    print("Starting room: ", start_room)

    # Mark the starting room as visitedRooms
    visitedRooms = [False] * 20
    visitedRooms[start_room] = True

    # Clean the rooms using DFS
    dfs_vacuum_cleaner(start_room, visitedRooms)

if __name__ == '__main__':
    main()
