from collections import deque

maze = {"A": ['S'],
        "B": ['C', 'D', 'S'],
        "C": ['B', 'J'],
        "D": ['B', 'G', 'S'],
        "E": ['G', 'S'],
        "F": ['G', 'H'],
        "G": ['D', 'E', 'F', 'H', 'J'],
        "H": ['F', 'G', 'I'],
        "I": ['H', 'J', 'exit'],
        "J": ['C', 'G', 'I'],
        "S": ['A', 'B', 'D', 'E']}


def search_exit(name):
    return name == 'exit'


def search(name):
    search_queue = deque()
    search_queue += maze[name]
    searched = []
    while search_queue:
        room = search_queue.popleft()
        if room not in searched:
            if search_exit(room):
                print(room + " is exit")
                return True

            else:
                search_queue += maze[room]
                searched.append(room)
    return print("There is no exit")


search("S")
