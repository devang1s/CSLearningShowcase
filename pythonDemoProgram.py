print('This is the print function. It sends a text output')

a = 'This is a variable. The value of it can be changed.'
b = input('This is the input function. It prompts the user for an input. Do you like this so far? Y/N')

if b=='Y':
    print("This is the result of an if statement. You said 'Y', right?")
elif b=='N':
    print("This is the result of the elif statement. You said 'N', right?")
else:
    print("This is the result of the else statement. You neither said 'Y', nor 'N'.")

b = input('Enter a')
ct=0

while b!='yay':
    print("This is the result of the while loop function. This will keep running until you enter 'yay', then print how many times the loop ran.")
    print("You didn't enter 'yay'")
    b = input('Enter a or yay')
    ct+=1

print("The loop ran",ct,"times, after you entered yay.")

for i in range(5,0,-1):
    print("This is the result of the FOR I IN RANGE loop. This will run",i-1,"more times")

l1 = int(input("Enter a number"))
L=[]

for i in range(1,l1+1):
    L.append(i)

for i in L:
    print("This time, this loop used a list instead of a range function. You entered",l1,". This loop has ran",i,"times.")

print("This is what the list that we just used looked like:")
print(L)
print("Thank you!")
