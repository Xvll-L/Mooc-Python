# Write your solution here
B = 1
word = "1"
Total = 1

A =  int(input("Limit:"))

while Total < A:
  
    B = B + 1 
    Total = Total + B
    word = word + f" + {B}"
    

print("The consecutive sum: ",word , "=" ,Total )