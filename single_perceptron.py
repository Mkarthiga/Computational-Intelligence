def CalculateYin(input_list,w_list,bias):
   res=0
   for i in range(len(input_list)):
      res=res+input_list[i]*w_list[i]
   yin=bias+res
   return yin
def CalculateY(yin,activation_list):
   for i in range(len(activation_list)):
      if(yin<activation_list[i][0] and yin>=activation_list[i][1]):
         return activation_list[i][2]
def Updation(w_list,bias,learn_rate,input_list,output):
    wnew_list=[]
    diffw_list=[]
    for i in range(len(w_list)):
      k=round(w_list[i]+(learn_rate*input_list[i]*output),3)
      wnew_list.append(k)
      diffw_list.append(w_list[i]-k)
    bnew=round(bias+(learn_rate*output),3)
    diffb=bias-bnew
    return wnew_list,bnew,diffw_list,diffb

#main function
n=int(input("Number of inputs:"))
ip_list=[]
op_list=[]
w_list=[]
activation_list=[]
for i in range(0,2**n):
   l1=[]
   print("Input",i+1,":")
   for j in range(0,n):
      print("Enter x",j+1,":")
      l1.append(int(input()))
   ip_list.append(l1)
   del l1
   print("Output",i+1,":")
   op_list.append(int(input()))
bias=float(input("Enter the bias:"))
for i in range(0,n):
   print("Enter the intial w",i+1,":")
   w_list.append(float(input()))
learn_rate=float(input("Enter the learning rate:"))
ac=int(input("Number of values in activation function:"))
print("Enter -999 for negative infinite and +999 for positive infinite")
for i in range(0,ac):
   r1=float(input("Range from:"))
   r2=float(input("Range to:"))
   act_val=float(input("Activation value:"))
   activation_list.append([r2,r1,act_val])
updationNeeded=True
for i in range(0,n):
   print("x",i+1,end="\t")
print("t\tyin\ty",end="\t")
for i in range(0,n):
   print("diffw",i+1,end="\t")
print("diffb",end="\t")
for i in range(0,n):
   print("w",i+1,end="\t")
print("b")
print("---------------------------------------------------------------------------------------------")
it=0

while(updationNeeded):
   it=it+1
   print("Iterations:",it)
   print("---------------------------------------------------------------------------------------------")
   count=0
   for i in range(len(ip_list)):
        input_list=ip_list[i]
        output=op_list[i]
        for j in range(len(input_list)):
            print(input_list[j],end="\t")
        print(output,end="\t")
        yin=round(CalculateYin(input_list,w_list,bias),3)
        y=CalculateY(yin,activation_list)
        print(yin,"\t",y,end="\t")
        if(y!=output):
            w_list,bias,diffw_list,diffb=Updation(w_list,bias,learn_rate,input_list,output)
        else:
            diffw_list=[]
            count=count+1
            for j in range(len(w_list)):
              diffw_list.append(0)
            diffb=0
        for j in range(len(diffw_list)):
           print(round(diffw_list[j],3),end="\t")
        print(round(diffb,3),end="\t")
        for j in range(len(w_list)):
           print(w_list[j],end="\t")
        print(round(bias,3))
        if(count==len(ip_list)):
           updationNeeded=False
   print("---------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------")
print("Total iterations:",it)
print("Final weights:")
for i in range(len(w_list)):
   print("w",i+1,":",w_list[i])
print("Final bias:",round(bias,3))
print("-------------------------------------------------------------------------------------------------")