n = int(input())
f = 0
while n!=0:
    c = n%10
    f = f+1
    n = n//10
if f==10:
    print("Valid")
else:
    print("Invalid")
    