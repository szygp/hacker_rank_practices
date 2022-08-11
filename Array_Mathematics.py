import numpy
N,M = map(int,input().split())
a,b= (numpy.array([input().split() for i in range(N)],int) for i in range(2))
print(a+b,a-b,a*b,a//b,a%b,a**b,sep='\n')
