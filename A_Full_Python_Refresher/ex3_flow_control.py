#Modify the code so that the evens list contains only the even numbers of the numbers list. You do not need to print anything.
my_list=[6,4,13,34,67,56,89,23]
evens=[]
for even in my_list:
    if even%2==0:evens.append(even)

#using filter
evens=list(filter(lambda x:x%2==0,my_list))

#For part 2, add a clause to the if statement such that if the user's input is "q", your program prints "Quit" .
add=0
while True:
    inp=input("Enter the value you want to add.q to quit: ")
    if inp=='q':
        print("Quit")
        break
    add+=int(inp)
    print(f"The sum is {add}")