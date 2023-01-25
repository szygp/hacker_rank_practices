N, X = map(int,input().split())
list_s = []
list_ID = []
for i in range(X):
    list_s.append(list(map(float,input().split())))

for a in zip(*list_s):
    #zip的object
    print(sum(a)/X)
