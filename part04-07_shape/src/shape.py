# Copy here code of line function from previous exercise and use it in your solution
def line(a,b):
    if b == "":
        print(a * "*")
    else:
        print(a * b[0])

def shape(a,b,c,d):
    i = 0
    j = 0

    while i < a:
        i = i + 1
        line(i, b)

    while j < c:
        j = j + 1
        line(a, d)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")