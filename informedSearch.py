class Graph:
    n=0
    ver=[]  #vertex list
    adjList=[]  #adjancency list
    costList=[] #costmatrix
    straightLine=[] #straight line distance
    def __init__(self,n,ver):
        self.n=n #number of vertex
        self.ver=ver
        self.adjList=[[] for i in range(len(self.ver))] #empty list for each node's adjacaceny list
        self.costList=[ [float('inf') for j in range(len(self.ver))] for i in range(len(self.ver))] #create a n x n cost matrix intialise all the values as infinite
    def addNode(self,x):
        if(x in self.ver):
            print("Can't add!! Node",x," exits")
            return
        for i in range(len(self.ver)):
            self.costList[i].append(float('inf')) #append a column of infinte values in cost matrix as last column to include the new node and other nodes cost
        self.ver.append(x) 
        self.adjList.append([]) #append empty adj list for the new node
        self.costList.append([float('inf') for j in range(len(self.ver))]) #append a row of inifite values in cost matrix as last row for the new node
    def addEdge(self,v1,v2,cost):
        if(v1 not in self.ver or v2 not in self.ver):
            print("Node doesn't exist")
            return
        node1=self.ver.index(v1) #get the index of the vertex1 in vertex list
        node2=self.ver.index(v2) #get the index of the vertex2 in vertex list
        self.costList[node1][node2]=cost #add the cost in cost matrix between vertex1 and vertex2
        self.costList[node2][node1]=cost #add the cost in cost matrix between vertex2 and vertex1
        self.adjList[node1].append(v2) #add the vertex2 in adj list of vertex1
        self.adjList[node2].append(v1) #add the vertex1 in adj list of vertex2
    def adjListDisplay(self):
        for i in range(len(self.ver)):
            print(self.ver[i],"->",self.adjList[i])
    def removeEdge(self,x,y):
        node1=self.ver.index(x) #get the index of the vertex1 in vertex list
        node2=self.ver.index(y) #get the index of the vertex2 in vertex list
        l1=self.adjList[node1]  #get the adjanceny list of vertex1
        l2=self.adjList[node2]  #get the adjanceny list of vertex2
        if(y not in l1 and x not in l2):
            print("Edge doesn't exists")
        else:
            self.adjList[node1].remove(y)   #remove the vertex2 from adj list of vertex1
            self.adjList[node2].remove(x)   #remove the vertex1 from adj list of vertex2
            self.costList[node1][node2]=float('inf')    #change the cost value to infinite in cost matrix between vertex1 and vertex2
            self.costList[node2][node1]=float('inf')    #change the cost value to infinite in cost matrix between vertex2 and vertex1
    def removeNode(self,x):
        if( x not in self.ver):
            print("Node doesn't exist")
            return
        node=self.ver.index(x)  #get the index of the vertex in vertex list
        del self.straightLine[node] #delete the straight line value
        del self.adjList[node]  #delete the adj list for that vertex
        del self.costList[node] #delete the cost matrix for that vertex
        for i in range(len(self.adjList)): #remove the vertex from other node's adj list
            if(x in self.adjList[i]):
                self.adjList[i].remove(x)
        for i in range(len(self.costList)): #remove cost value of vertex and other nodes from other node's cost matrix
            for j in range(len(self.costList[i])):
                if(j>=node and j<len(self.costList[i])-1): 
                    #here we replace the column in cost matrix that gives cost value of vertex and other nodes from other node's cost matrix by the next column in matrix
                    self.costList[i][j]=self.costList[i][j+1]  
            self.costList[i].pop()  #remove tha last column as it's duplicate now
        self.ver.remove(x) #remove node from the vertex list
    def straightLineDistance(self,goal):
        if(len(self.straightLine)!=0): 
            #if there exist a non empty straight line distance list already remove the values from the list
            for i in range(len(self.straightLine)):
                self.straightLine.pop()
        for i in range(len(self.ver)): 
            print("Straight line distance between",self.ver[i]," and ",goal,":",end=" ")
            dist=int(input())
            self.straightLine.append(dist) #append the values between all vertex and goal node
    def costMatrixDisplay(self):
        print(" ",end=" ")
        for i in range(len(self.ver)):
            print(self.ver[i]," ",end="\t")
        print()
        for i in range(len(self.ver)):
            print(self.ver[i],end=" ")
            for j in range(len(self.ver)):
                print(self.costList[i][j],end="\t")
            print()
    def straightLineDisplay(self):
        if(len(self.straightLine)==0):
            print("The list is empty")
            return
        for i in range(len(self.straightLine)):
            print(self.ver[i],"=",self.straightLine[i])
    def aStarSearch(self,start,goal):
        if(start not in self.ver or goal not in self.ver):
            print("search node doesn't exist")
            return
        pathfound=False
        edgecost=0
        queue=[]
        l1=[]
        ind=self.ver.index(start)
        queue.append([self.straightLine[ind],[start],0,start]) #pathcost,path,cost of last node in path,last node in path
        while(pathfound==False):
            edgecost+=queue[0][2]
            for i in range(len(self.adjList[ind])):
                l1=[]
                for j in range(len(queue[0][1])): #create list with path in 1st place in queue
                    l1.append(queue[0][1][j])
                node=self.ver.index(self.adjList[ind][i]) 
                cost=edgecost+self.straightLine[node]+self.costList[ind][node] #calculate the new pathcost(path+adjnode)
                l1.append(self.ver[node]) #join thae node with path and create new path
                queue.append([cost,l1,self.costList[ind][node],self.ver[node]]) #add the new path to queue
                del l1
            del queue[0] #remove old path from queue
            queue.sort() #sort the queue to get the queue with low cost.
            for i in range(len(queue)):
                print(queue[i][3],"->",queue[i][0],end="||") #print the path and cost
            print()
            if(queue[0][3]==goal):#check if the last node in the first path in queue is goal
                pathfound=True
                break
            for i in range(len(queue)): #check if the last node is leaf node
                AdjNode=0
                k=self.ver.index(queue[i][3])
                path=queue[i][1]
                for j in range(len(self.adjList[k])):
                    if(self.adjList[k][j] in path):
                        AdjNode+=1
                if(AdjNode==len(self.adjList[k])and queue[i][3]!=goal): #delete the path that contain no goal and reached the leaf node
                    del queue[i]   
            if(len(queue)==0): #if the queue is empty
                print("No path found")
                return
            ind=self.ver.index(queue[0][3])
            print("Expand node",queue[0][3])
        print("Path found:")  
        path=queue[0][1]
        pathcost=queue[0][0]
        for i in range(len(path)):
            if(i<len(path)-1):
                print(path[i],"->",end=" ")
            else:
                print(path[i])
        print("path cost:",pathcost)
                

vertices=[]
num=int(input("Enter the number of vertices:"))
for i in range(num):
    val=input("Enter the name of vertex:")
    vertices.append(val)
g=Graph(num,vertices)
print("MENU\n 1.ADD NODE\n 2.ADD EDGE\n 3.ADJACENCY LIST\n 4.REMOVE NODE\n 5.REMOVE EDGE\n 6.COST MATRIX\n 7.STRAIGHT LINE DISTANCE\n 8.STRAIGHT LINE DISTANCE DISPLAY\n 9.A* SEARCH")
ch=0
while(ch<11):
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("---------------ADD NODE-----------------")
        node=(input("Enter the node to be added:"))
        g.addNode(node)
    elif ch==2:
        print("---------------ADD EDGE----------------")
        x=(input("Enter the node1:"))
        y=(input("Enter the node2:"))
        c=int(input("Enter the cost:"))
        g.addEdge(x,y,c)
    elif ch==3:
        print("-------------ADJACENCY LIST--------------")
        g.adjListDisplay()
    elif ch==4:
        print("-------------REMOVE NODE-------------")
        node=(input("Enter the node to be removed:"))
        g.removeNode(node)
    elif ch==5:
        print("------------- REMOVE EDGE-------------")
        x=(input("Enter the node1:"))
        y=(input("Enter the node2:"))
        g.removeEdge(x,y)
    elif ch==6:
        print("------------COST MATRIX----------")
        g.costMatrixDisplay()
    elif ch==7:
        print("---------STRAIGHT LINE DISTANCE----------")
        goal=input("Enter the goal node:")
        g.straightLineDistance(goal)
    elif ch==8:
        print("------------STRAIGHT LINE DISTANCE DISPLAY----------")
        g.straightLineDisplay()
    elif ch==9:
        print("--------------A* SEARCH----------------")
        start=input("Enter the start node:")
        goal=input("Enter the goal node:")
        g.aStarSearch(start,goal)

    else:
        print("----------INVALID CHOICE-------------")
        break