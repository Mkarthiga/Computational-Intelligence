class Graph:
    n=0
    ver=[]
    adjList=[]
    costList=[]
    def __init__(self,n,ver):
        self.n=n
        self.ver=ver
        self.adjList=[[] for i in range(len(self.ver))]
        self.costList=[ [float('inf') for j in range(len(self.ver))] for i in range(len(self.ver))]
    def addNode(self,x):
        if(x in self.ver):
            print("Can't add!! Node",x," exits")
            return
        for i in range(len(self.ver)):
            self.costList[i].append(float('inf'))
        self.ver.append(x)
        self.adjList.append([])
        self.costList.append([float('inf') for j in range(len(self.ver))])
    def addEdge(self,v1,v2,cost):
        if(v1 not in self.ver or v2 not in self.ver):
            print("Node doesn't exist")
            return
        node1=self.ver.index(v1)
        node2=self.ver.index(v2)
        self.costList[node1][node2]=cost
        self.costList[node2][node1]=cost
        self.adjList[node1].append(v2)
        self.adjList[node2].append(v1)
    def adjListDisplay(self):
        for i in range(len(self.ver)):
            print(self.ver[i],"->",self.adjList[i])
    def removeEdge(self,x,y):
        node1=self.ver.index(x)
        node2=self.ver.index(y)
        l1=self.adjList[node1]
        l2=self.adjList[node2]
        if(y not in l1 and x not in l2):
            print("Edge doesn't exists")
        else:
            self.adjList[node1].remove(y)
            self.adjList[node2].remove(x)
            self.costList[node1][node2]=float('inf')
            self.costList[node2][node1]=float('inf')
    def removeNode(self,x):
        if( x not in self.ver):
            print("Node doesn't exist")
            return
        node=self.ver.index(x)
        del self.adjList[node]
        del self.costList[node]
        for i in range(len(self.adjList)):
            if(x in self.adjList[i]):
                self.adjList[i].remove(x)
        #print("cost matrix before \n",self.costList)
        for i in range(len(self.costList)):
            #print("         i",i,self.costList[i])
            for j in range(len(self.costList[i])):
                if(j>=node and j<len(self.costList[i])-1):
                    #print("j",j,"\t",self.costList[i][j],"\t",self.costList[i][j+1])
                    self.costList[i][j]=self.costList[i][j+1]  
            self.costList[i].pop() 
         
        self.ver.remove(x)
    def bfsSearch(self,x,y):
        start=x
        goal=y
        queue=[]
        res=[]
        if(start not in self.ver or goal not in self.ver):
            print("Node doesn't exist")
            return
        queue.append(start)
        while(goal not in res):
            res.append(start)
            queue.remove(start)
            ind=self.ver.index(start)
            for i in range(len(self.adjList[ind])):
                if(self.adjList[ind][i] not in res and self.adjList[ind][i] not in queue):

                    queue.append(self.adjList[ind][i])
            if(len(queue)!=0):
                start=queue[0]
        for i in range(len(res)):
            if(i<len(res)-1):
                print(res[i],"->",end=" ")
            else:
                print(res[i])
    def dfsSearch(self,x,y):
        start=x
        goal=y
        stack=[]
        res=[]
        if(start not in self.ver or goal not in self.ver):
            print("Node doesn't exist")
            return
        stack.append(start)
        while(goal not in res):
            res.append(start)
            stack.pop()
            ind=self.ver.index(start)
            i=len(self.adjList[ind])-1
            while(i>=0):
                if(self.adjList[ind][i] not in res and self.adjList[ind][i] not in stack):
                    stack.append(self.adjList[ind][i])
                i=i-1
            if(len(stack)!=0):
                start=stack[len(stack)-1]
        for i in range(len(res)):
            if(i<len(res)-1):
                print(res[i],"->",end=" ")
            else:
                print(res[i])
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
    def uniformCostSearch(self,start,goal):
        if(start not in self.ver or goal not in self.ver):
            print("search node doesn't exist")
            return
        pathfound=False
        edgecost=0
        queue=[]
        ind=self.ver.index(start)
        queue.append([0,start,[start]]) #cost,last node in path,path
        while(pathfound==False):
            #new path update in queue(by exapnding the node)
            edgecost=queue[0][0]
            for i in range(len(self.adjList[ind])):
                l1=[x for x in queue[0][2]]
                node=self.ver.index(self.adjList[ind][i])
                if self.adjList[ind][i] not in queue[0][2]:
                    l1.append(self.adjList[ind][i])
                    cost=edgecost+self.costList[ind][node]
                    queue.append([cost,self.adjList[ind][i],l1])
            #delete the first element in queue since node is expanded
            del queue[0]
            #sort the queue according to cost
            queue.sort()
            #print the status (last node and cost)
            for i in range(len(queue)):
                print(queue[i][1],"->",queue[i][0],end="||")
            print()
            #check if last node is goal
            if(queue[0][1]==goal):
                pathfound=True
                break
            #to check whether it is a leaf node
            for i in range(len(queue)): 
                AdjNode=0
                k=self.ver.index(queue[i][1])
                path=queue[i][2]
                for j in range(len(self.adjList[k])):
                    if(self.adjList[k][j] in path): #check if all the adj nodes already exist in path
                        AdjNode+=1
                if(AdjNode==len(self.adjList[k] and queue[i][1]!=goal)):
                    del queue[i]
            if(len(queue)==0):
                print("No path found")
                return
            #index value of the node to be exapanded
            ind=self.ver.index(queue[0][1])
            print("Expand node ",queue[0][1])
        print("Path found:")
        path=queue[0][2]
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
print("MENU\n 1.ADD NODE\n 2.ADD EDGE\n 3.ADJACENCY LIST\n 4.REMOVE NODE\n 5.REMOVE EDGE\n 6.BFS SEARCH\n 7.DFS SEARCH\n 8.COST MATRIX\n 9.UNIFORM COST SEARCH ")
ch=0
while(ch<10):
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
        print("-------------BREADTH FIRST SEARCH---------")
        start=input("Enter the start node:")
        goal=input("Enter the goal node:")
        g.bfsSearch(start,goal)
    elif ch==7:
        print("-----------DEPTH FIRST SEARCH----------")
        start=input("Enter the start node:")
        goal=input("Enter the goal node:")
        g.dfsSearch(start,goal)
    elif ch==8:
        print("------------COST MATRIX----------")
        g.costMatrixDisplay()
               
    elif ch==9:
        print("---------UNIFORM SEARCH COST----------")
        start=input("Enter the start node:")
        goal=input("Enter the goal node:")
        g.uniformCostSearch(start,goal)
    else:
        print("----------INVALID CHOICE-------------")
        break