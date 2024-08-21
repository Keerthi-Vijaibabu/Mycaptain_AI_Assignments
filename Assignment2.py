#To print the positive numbers in a list

List = list(eval(input("Enter a list: ")))
for i in List:
    if i<0:
        List.remove(i)

print(List)
