list1=[]
length=int(input("Enter How Many Fibonacci Terms you want: "))

for n in range(length):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        list1.append(0)
    elif n == 1 or n == 2:
        list1.append(1)
 
    else:
        list1.append(list1[n-1]+list1[n-2])

print(list1)
