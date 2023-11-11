class Graph:
    n=0
    ver=[]
    adjList=[]
    def __init__(self,n,ver):
        self.n=n
        self.ver=ver
        self.adjList=[[] for i in range(len(self.ver))]
       
    def addNode(self,x):
        if(x in self.ver):
            print("Can't add!! Node",x," exits")
            return
        self.ver.append(x)
        self.adjList.append([])
        
    def addEdge(self,v1,v2):
        if(v1 not in self.ver or v2 not in self.ver):
            print("Node doesn't exist")
            return
        node1=self.ver.index(v1)
        node2=self.ver.index(v2)
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

    def removeNode(self,x):
        if( x not in self.ver):
            print("Node doesn't exist")
            return
        node=self.ver.index(x)
        del self.straightLine[node]
        del self.adjList[node]
        for i in range(len(self.adjList)):
            if(x in self.adjList[i]):
                self.adjList[i].remove(x)
        self.ver.remove(x)
   
    def dlsSearch(self,start,goal,limit):
        if(start not in self.ver or goal not in self.ver):
            print("Node doesn't exist")
            return
        stack = [(start, [start], 0)]  # Stack to store nodes, their paths, and their depths
        visited = set()  # Set to keep track of visited nodes

        while stack:
            node, path, depth = stack.pop()  # Pop the last node from the stack

            if node == goal:
              # Target node found, return the path
                print("Path for depth limt ",limit,":")
                for i in range(len(path)):
                    if(i<len(path)-1):
                        print(path[i],"->",end=" ")
                    else:
                        print(path[i])
                return True


            if depth < limit:
                if node not in visited:
                    visited.add(node)
                    ind=self.ver.index(node)
                    neighbors = self.adjList[ind]  # Get the neighbors of the current node

                for neighbor in neighbors:
                    new_path = path + [neighbor]  # Add the neighbor to the current path
                    stack.append((neighbor, new_path, depth + 1))  # Push neighbors to the stack with increased depth and updated path

        print("No path found")
        return  # Target node not found within the depth limit
        
    def idsSearch(self,start,goal,max_depth):
        if(start not in self.ver or goal not in self.ver):
            print("Node doesn't exist")
            return
        for depth_limit in range(0,max_depth+1): #runs iteratively for depth value 0,1,2,3......
            path =self.dlsSearch(start,goal, depth_limit)
            if path:
                return  # Target node found, return the path

        print("No path found")
        return  # Target node not found within the maximum depth
        
    
vertices=[]
num=int(input("Enter the number of vertices:"))
for i in range(num):
    val=input("Enter the name of vertex:")
    vertices.append(val)
g=Graph(num,vertices)
print("MENU\n 1.ADD NODE\n 2.ADD EDGE\n 3.ADJACENCY LIST\n 4.REMOVE NODE\n 5.REMOVE EDGE\n 6.DLS SEARCH\n 7.IDS SEARCH")
ch=0
while(ch<8):
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("---------------ADD NODE-----------------")
        node=(input("Enter the node to be added:"))
        g.addNode(node)
    elif ch==2:
        print("---------------ADD EDGE----------------")
        x=(input("Enter the node1:"))
        y=(input("Enter the node2:"))
        g.addEdge(x,y)
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
        print("------------DEPTH LIMIT SEARCH----------")
        start=input("Enter the start node:")
        goal=input("Enter the goal node:")
        limit=int(input("Enter the depth limit:")) #limit (value given in question)
        g.dlsSearch(start,goal,limit)
        

    elif ch==7:
        print("--------------ITERARTIVE DEEPING SEARCH----------------")
        start=input("Enter the start node:")
        goal=input("Enter the goal node:")
        max_depth=int(input("Enter the maximum depth of the tree:")) #maximum depth of the graph(longest path in graph tree)
        g.idsSearch(start,goal,max_depth)

    else:
        print("----------INVALID CHOICE-------------")
        break