n = int(input())
m = input()
list_number = list(map(str,m.split()))
list_number_int = list(map(int,m.split()))
result1 = any(list_number[i] in ['1','2','3','4','5','6','7','8','9'] for i in range(n))
result2 = all(list_number[i]==list_number[i][::-1] for i in range(n))
result3 = all(list_number_int[i]> 0 for i in range(n))
def result_true():
    if result1 or result2:
        return True
    else:
        return False
if result3 and result_true():
    print(True)
else:
    print(False)