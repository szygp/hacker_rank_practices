import re
S = input()
k = input()
matches = re.finditer(r'(?=('+k+'))',S)
if k not in S:
    print((-1,-1))
else:
    for match in matches:
        print((match.start(1),match.end(1)-1))
