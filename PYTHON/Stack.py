# the collection (deque way of using the stack and its similar to the table thing )
from collections import deque   

stack=deque()

stack.append("Minecraft")
stack.append("Skyrim")
stack.append("DOOM")
stack.append("Borderlands")
stack.append("FFVII")
FavGame= stack.index("FFVII")
print(FavGame)   