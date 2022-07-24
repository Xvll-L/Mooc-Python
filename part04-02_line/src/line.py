# Write your solution here
# You can test your function by calling it within the following block
def line(a,b):
    if b == "":
        print(a*"*")
    else:
        print(a * b[0])

if __name__ == "__main__":
    line(5, "x")
    line(7, "%")
    line(10, "LOL")
    line(3, "")