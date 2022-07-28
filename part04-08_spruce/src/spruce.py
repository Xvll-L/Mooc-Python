# Write your solution here
from re import I


def spruce(a):
    print("a spruce!")
    i = 0
    data = "*"
    space = a - 1
    print(f"{space * ' '}{data}")
    loopval = a - 1
    while i < loopval:
        i = i + 1
        space = space - 1
        data = data + "**"
        print(f"{space * ' '}{data}")
    print(f"{(a - 1)* ' '}*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)

print(len("*********"))