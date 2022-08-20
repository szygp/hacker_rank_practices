iter_num = int(input())
list_room_number = list(map(int,input().split()))
set_multiples = set(list_room_number)

m = 0
n = 0
for x in set_multiples:
    m += x*iter_num
for y in list_room_number:
    n += y
captain = int((m - n)/(iter_num-1))

print(captain)