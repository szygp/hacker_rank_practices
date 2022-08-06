lower = []
Upper = []
num_odd=[]
num_even=[]
for i in input():
    if i.islower():
        lower.append(i)
    elif i.isupper():
        Upper.append(i)
    elif i.isdigit() and int(i) in [1,3,5,7,9]:
        num_odd.append(i)
    else:
        num_even.append(i)
lower.sort()
Upper.sort()
num_odd.sort()
num_even.sort()
print(''.join(lower)+''.join(Upper)+''.join(num_odd)+''.join(num_even))