import numpy
N = int(input())
list_A = []
for i in range(N):
    list_A.append(list(map(int,input().split())))
list_B = []
for i in range(N):
    list_B.append(list(map(int,input().split())))
print (numpy.dot(list_A,list_B))