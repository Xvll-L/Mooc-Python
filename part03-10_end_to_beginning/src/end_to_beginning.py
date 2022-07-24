# Write your solution here
word = input('give word!!! ')
value = len(word) - 1


while True:
    print(word[value])
    value = value - 1
    if value == -1:
        break