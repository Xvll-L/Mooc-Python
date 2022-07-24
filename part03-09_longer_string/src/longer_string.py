# Write your solution here

A = input("Please type in string 1: ")

B = input("Please type in string 2: ")

if len(A) > len(B):
    print(A, "is longer")
elif len(B) > len(A):
    print(B, "is longer")
else:
    print("The strings are equally long")