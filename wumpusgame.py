def matrix(order): 
    world=[]
    space=" "
    for i in range(0,order):
        l1=[[space,space,space] for _ in range(0,order)]
        world.append(l1)
    return world
def indexToBePlaced(l1):
    space=" "
    for i in range(len(l1)):
            if(l1[i]==space):
                return i
def markAdjcent(x,y,marking,place):
    if(x<3):
        if(marking not in place[x+1][y]):
            place[x+1][y][indexToBePlaced(place[x+1][y])]=marking
    if(y<3):
        if(marking not in place[x][y+1]):
            place[x][y+1][indexToBePlaced(place[x][y+1])]=marking
    if(x>0):
        if(marking not in place[x-1][y]):
            place[x-1][y][indexToBePlaced(place[x-1][y])]=marking
    if(y>0):
        if(marking not in place[x][y-1]):
            place[x][y-1][indexToBePlaced(place[x][y-1])]=marking
    return place
def addWumpus(x,y,world):
    pit="P"
    stench="S"
    if(x==0 and y==0):
        print("Wumpus should not be placed in initial state")
        return world
    else:
        if(pit not in world[x][y]):
            world[x][y][indexToBePlaced(world[x][y])]="W"
        else:
            print("There is pit in position(",x+1,",",y+1,")")
            return world
        world=markAdjcent(x,y,stench,world)
        return world
def addPit(x,y,world):
    wumpus="W"
    breeze="B"
    if(x==0 and y==0):
        print("Pit should not be placed in initial state")
        return world
    else:
        if(wumpus not in world[x][y]):
            world[x][y][indexToBePlaced(world[x][y])]="P"
        else:
            print("There is wumpus in position(",x+1,",",y+1,")")
            return world
        world=markAdjcent(x,y,breeze,world)
        return world
def addGold(x,y,world):
    pit="P"
    if(pit not in world[x][y]):
        world[x][y][indexToBePlaced(world[x][y])]="$"
    else:
        print("There is pit in the position(",x+1,",",y+1,")")
    return world
def displayWorld(world):
    print("DETAILS\nB=>Breeze\tS=>Stench\tP=>Pit\nW=>Wumpus\t$=>Gold")
    i=3
    while(i>=0):
        print("-----------------------")
        for j in range(0,4):
            print("|",world[i][j][0],"|",end="")
        print()
        for j in range(0,4):
            print("|",world[i][j][1],"|",end="")
        print()
        for j in range(0,4):
            print("|",world[i][j][2],"|",end="")
        print()
        i=i-1
    print("------------------------")


def displayEnv(env):
    print("DETAILS\n\tV=>Visted\tO=>Safe Place\tA=>Agent\tB=>Breeze\tS=>Stench")
    i=3
    while(i>=0):
        print("-----------------------")
        for k in range(0,5):
            for j in range(0,4):
                print("|",env[i][j][k],"|",end="")
            print()
        i=i-1
    print("------------------------")
def moveAgent(x,y,env,world):
    safePlace="O"
    visited="V"
    wumpus="W"
    flag=1
    for i in range(len(env)):
        for j in range(len(env[i])):
            if(safePlace in env[i][j] and visited not in env[i][j] ):
                if((i==x+1 and j==y)or(i==x and j==y+1)or(i==x-1 and j==y)or(i==x and j==y-1)):
                    return i,j
    for i in range(len(env)):
        for j in range(len(env[i])):
           if(safePlace in env[i][j]):
              if((i==x+1 and j==y)or(i==x and j==y+1)or(i==x-1 and j==y)or(i==x and j==y-1)):
                   return i,j
                
def markAgent(x,y,env):
    env[x][y][indexToBePlaced(env[x][y])]="A"
    if("V" not in env[x][y]):
        env[x][y][indexToBePlaced(env[x][y])]="V"
    displayEnv(env)
    return env
def genPerceptSeq(x,y,world,shooted):
    perceptSeq=[None for i in range(0,5)]
    stench="S"
    breeze="B"
    gold="$"
    wumpus="W"
    if(stench in world[x][y]):
        perceptSeq[0]="Stench"
    if(breeze in world[x][y]):
        perceptSeq[1]="Breeze"
    if(gold in world[x][y]):
        perceptSeq[2]="Glitter"
    if(shooted==False and wumpus in world[x][y]):
        perceptSeq[4]="Scream"
    return perceptSeq
def markSafePlace(perceptSeq,x,y,env):
    sw=[]
    nw=[]
    se=[]
    ne=[]
    stench="S"
    breeze="B"
    visted="V"
    safePlace="O"
    if(x>0):
        if(y>0):
            sw=env[x-1][y-1]
        if(y<3):
            nw=env[x-1][y+1]
    if(x<3):
        if(y>0):
            se=env[x+1][y-1]
        if(y<3):
            ne=env[x+1][y+1]
    if(perceptSeq[0]=="Stench"):
        if(stench not in ne or stench not in sw):
            if(x<3):
                if(safePlace not in env[x+1][y]):
                    env[x+1][y][indexToBePlaced(env[x+1][y])]=safePlace
        if(stench not in se or stench not in nw):
            if(x>0):
                if(safePlace not in env[x-1][y]):
                    env[x-1][y][indexToBePlaced(env[x-1][y])]=safePlace
        if(stench not in se or stench not in sw):
            if(y>0):
                if(safePlace not in env[x][y-1]):
                    env[x][y-1][indexToBePlaced(env[x][y-1])]=safePlace
        if(stench not in ne or stench not in nw):
            if(y<3):
                if(safePlace not in env[x][y+1]):
                    env[x][y+1][indexToBePlaced(env[x][y+1])]=safePlace
    if(perceptSeq[0]=="Breeze"):
        if(breeze not in ne or breeze not in sw):
            if(x<3):
                if(safePlace not in env[x+1][y]):
                    env[x+1][y][indexToBePlaced(env[x+1][y])]=safePlace
        if(breeze not in se or breeze not in nw):
            if(x>0):
                if(safePlace not in env[x-1][y]):
                    env[x-1][y][indexToBePlaced(env[x-1][y])]=safePlace
        if(breeze not in se or breeze not in sw):
            if(y>0):
                if(safePlace not in env[x][y-1]):
                    env[x][y-1][indexToBePlaced(env[x][y-1])]=safePlace
        if(breeze not in ne or breeze not in nw):
            if(y<3):
                if(safePlace not in env[x][y+1]):
                    env[x][y+1][indexToBePlaced(env[x][y+1])]=safePlace
        
    if((all(element == perceptSeq[0] for element in perceptSeq))or "Scream" in perceptSeq):
        markAdjcent(x,y,safePlace,env)
    return env       
def playAgent(x,y,world):
    env=[]
    path=[]
    space=" "
    for i in range(0,4):
        l1=[[space,space,space,space,space,space] for j in range(0,4)]
        env.append(l1)
    notfoundGold=True
    shooted=False
    breeze="B"
    stench="S"
    safePlace="O"
    giltter="G"
    cnt=0
    flag=1
    env[x][y][indexToBePlaced(env[x][y])]=safePlace
    while(notfoundGold):
        path.append([x,y])
        print("----------------MOVE",cnt,"------------------")
        percept_seq=genPerceptSeq(x,y,world,shooted)
        print("Percept Sequence",percept_seq)
        if("Glitter" in percept_seq):
            notfoundGold=False
            print("Gold found in position(",x+1,y+1,")")
            flag=0
        if("Scream" in percept_seq):
            print("Wumpus killed!!")
        if("Stench" in percept_seq):
            if(stench not in env[x][y]):
                env[x][y][indexToBePlaced(env[x][y])]=stench
        if("Breeze" in percept_seq):
            if(breeze not in env[x][y]):
                env[x][y][indexToBePlaced(env[x][y])]=breeze
        if(flag==1):
            markSafePlace(percept_seq,x,y,env)
        if(flag==0):
            env[x][y][indexToBePlaced(env[x][y])]=giltter
        markAgent(x,y,env)
        env[x][y]= list(map(lambda x: x.replace('A', space), env[x][y]))
        x,y=moveAgent(x,y,env,world)
        cnt=cnt+1
    print("Total number of moves:",cnt-1)
    print("Path traveled by the agent:")
    for i in range(len(path)):
        print("(",path[i][0]+1,path[i][1]+1,")",end=" ")
        if(i!=len(path)-1):
            print("=>",end=" ")
    print()


dim=int(input("Enter the order of the maze:"))
w=matrix(dim)
print("-----WUMPUS WORLD -----\n1.Add Wumpus\n2.Add Gold\n3.Add Pit\n4.Display World\n5.PlayGame")
ch=0
while(ch<7):
    print("Enter your choice:")
    ch=int(input())
    if(ch==1):
        print("---------------ADD WUMPUS-----------")
        print("Enter the location of wumpus:")
        x=int(input("Enter the row number:"))
        y=int(input("Enter the column number:"))
        if(x-1>3 or x-1<0 or y-1>3 or y-1<0):
            print("Position doesn't exist!!")
            continue
        addWumpus(x-1,y-1,w)
    elif(ch==2):
        print("---------------ADD GOLD-----------")
        print("Enter the location of Gold:")
        x=int(input("Enter the row number:"))
        y=int(input("Enter the column number:"))
        if(x-1>3 or x-1<0 or y-1>3 or y-1<0):
            print("Position doesn't exist!!")
            continue
        addGold(x-1,y-1,w)
    elif(ch==3):
        print("---------------ADD PIT-----------")
        k=int(input("Enter the number of pits:"))
        for j in range(0,k):
            print("Enter the location of pit ",j+1,":")
            x=int(input("Enter the row number:"))
            y=int(input("Enter the column number:"))
            if(x-1>3 or x-1<0 or y-1>3 or y-1<0):
                print("Position doesn't exist!!")
                continue
            addPit(x-1,y-1,w)
    elif(ch==4):
        print("-----------------WUMPUS WORLD-----------------")
        displayWorld(w)
    elif(ch==5):
        print("--------------WUMPUS GAME-------------")
        print("Enter the starting location:")
        x=int(input("Enter the row number:"))
        y=int(input("Enter the column number:"))
        playAgent(x-1,y-1,w)
    elif(ch==6):
        print("----------EXIT------------")
        break
        
    else:
        print("--------INVALID CHOICE----------")
        break

