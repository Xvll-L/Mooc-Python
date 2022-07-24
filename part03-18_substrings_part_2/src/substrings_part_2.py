# Write your solution here

string = input("Please type in a string:")

i = len(string)

while True:
    i = i - 1
    print(string[i:len(string)])
    if i == 0:
        break