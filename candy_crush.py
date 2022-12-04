elements=['👾','🤖','🧠','🫀']
boardlist=[]
#randomly populate 25 items in board list
import random
for item in range(25):
    boardlist.append(random.choice(elements))

print(boardlist)    
def printBoard(lst):
    pos=0
    for i in range(5):
        for j in range(5):
            print(lst[pos],end= ' ')
            pos +=1
        print("")
printBoard( boardlist )