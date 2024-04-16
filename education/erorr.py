a=int(input())
is_same = True
b=a%10
while a != 0:
    if b > a%10:
        is_same = False
    b=a%10
    a//= 10
if is_same:
    print("YES")
elif is_same == False:
    print("NO")
