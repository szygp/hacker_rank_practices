#option 1
import re
String = input()
pattern = re.compile(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])')
x = pattern.finditer(String)
temp = None
for temp in x:
    print(temp.group())
if not temp:
    print(-1)

#or!!!!! option 2
import re
s = input()
pattern = re.compile(r"(?<![AEIOU])([AEIOU]{2,})(?![AEIOU]).", re.I)
fi = pattern.findall(s)
if fi:
    print(*fi, sep='\n')
else:
    print(-1)