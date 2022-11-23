from collections import deque

maze = {"Exit": ["i"], "i": ["j", "h"], "j": ["g", "c"], "h": ["g", "f"], "g": ["f", "e", "d"], "c": ["b"], "f": ["g"],
        "e": ["g", "s"], "d": ["s", "b", "g"], "s": ["a", "b", "Entrance"], "b": ["s", "c"], "Entrance": ["s"]}


def search_exit(name):
    return name == "Exit"


def search(name):
    search_queue = deque()
    search_queue += maze[name]
    searched = []
    while search_exit:
        room = search_queue.pop()
        if not room in searched:
            if search_exit(room):
                print(room)
                return True
        else:
            search_queue += maze[room]
            searched.append(room)
    return False


search("Entrance")