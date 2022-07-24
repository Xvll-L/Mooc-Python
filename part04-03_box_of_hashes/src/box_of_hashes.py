# Copy here code of line function from previous exercise
from re import I


def line(a,b):
    if b == "":
        print(a*"*")
    else:
        print(a * b[0])

def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 0
    while i < height:
        i = i + 1
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
