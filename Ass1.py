#Fibonacci Series
x = -1
y = 1
n = int(input("Enter the number of terms:"))
for i in range (n):
    z = x+y
    print(z, sep =",", end = " ")
    x,y = y,z
