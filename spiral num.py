c = int(input())
d = c*2-1
num1 = c
for i in range(c):
    num = c
    for j in range(i,0, -1):
        print(num, end = " ")
        num-=1
    
    for k in range(d,0,-1):
        print(num,end = " ")
    d-=2
    num2 = num1 + 1
    if i > 0:
        for m in range(i,0,-1):
            print(num2, end= " ")
            num2 += 1
    num1 -= 1
    print()

a = 1
l = 2
num1 = 2
for i in range(c-1,0,-1):
    num = c
    for j in range(i,0,-1):
        print(num, end = " ")
        num-=1
    
    for k in range(a,0,-1):
        print(l, end = " ")
    
    num2 = num1
    for m in range(i,0,-1):
        print(num2,end = " ")
        num2 += 1
    num1+=1
    a+=2
    l+= 1
    print()


    
