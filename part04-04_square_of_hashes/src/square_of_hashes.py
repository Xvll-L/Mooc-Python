# Copy here code of line function from previous exercise
def line(a,b):
    if b == "":
        print(a*"*")
    else:
        print(a * b[0])
def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        i = i + 1
        
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
