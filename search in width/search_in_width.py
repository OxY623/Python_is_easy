graph={}
graph["you"]=["alice","bob","claire"]
graph["bob"] = ["anuj", "peggy"] 
graph["alice"] = ["peggy"] 
graph["claire"] = ["thom", "jonny"] 
graph["anuj"] = [] 
graph["peggy"] = [] 
graph["thom"] = [] 
graph["jonny"] = []

from collections import deque 
search_queue = deque()
search_queue+=graph["you"]
