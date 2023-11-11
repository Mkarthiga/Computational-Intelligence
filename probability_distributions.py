import math
import random
def gaussian_dist(mean,std):
    x=int(random.random())
    return ((1/std*math.sqrt(2*math.pi))*math.exp(-(x-mean)**2/(2*(std**2))))

print(gaussian_dist(float(input("mean:")),float(input("std:"))))

def poisson_dist(rate):
    k=int(random.random())
    return ((math.exp(-rate)*(rate**k))/math.factorial(k))

print(poisson_dist(float(input("rate:"))))

def binomial_dist(num,prob):
    k=int(random.random())
    return (math.comb(num,k)*(prob**k)*((1-prob)**(num-k)))

print(binomial_dist(int(input("number of trails:")),float(input("probabilty of success:"))))

def bernoulli_dist(prob):
    k=float(random.uniform(0.0,1.0))
    if(k>=prob):
        return 1
    else:
        return 0

print(bernoulli_dist(float(input("probability:"))))

def Categorical_dist(l1):
    l1.sort()
    k=float(random.uniform(l1[0][0],1.0))
    print(k)
    i=len(l1)-1
    while(i>=0):
        if(k>=l1[i][0]):
            return l1[i][1]
        i=i-1
    
print("enter the number of categorical values:")
num=int(input())
l=[]
for i in range(0,num):
    l.append([float(input("probability:")),input("value:")])
print(Categorical_dist(l))