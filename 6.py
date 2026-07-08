count=5
for i in range(1,count+1):
    for j in range(1,i+1):
        if j==1 or i==count or i==j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
