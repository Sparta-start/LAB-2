a = int(input())
b = int(input())
c = int(input())
if ((a*b)<c):
    print("NO")
elif ((((a*b)-c)%a == 0) or (((a*b)-c)%b == 0)):
    print("YES")
else:
    print("NO")