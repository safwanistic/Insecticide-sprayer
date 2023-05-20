import random
import time


def dfs_vacuum_cleaner(room, visitedRooms):
    time.sleep(0.7)
    print("Cleaning room #", room)

    visitedRooms[room] = True

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
    rooms = [True] * 20
    print("Vacuum to be placed in any of the 20 rooms")
    time.sleep(.85)

    start_room = random.randint(0, 19)

    time.sleep(.85)
    
    print("Starting room: ", start_room)

    visitedRooms = [False] * 20
    visitedRooms[start_room] = True

    dfs_vacuum_cleaner(start_room, visitedRooms)

if __name__ == '__main__':
    main()
