# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
line = int(input())
for i in range(line):
    string = input()
    res = re.match(r'^[7-9]\d{0}\d{9}$',string)
    if res:
        print('YES')
    else:
        print('NO')