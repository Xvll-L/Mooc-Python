# Write your solution here

userInput = input("Please type in a sentence:")
i = 0; 
print(userInput[0])
while i < len(userInput):
    
    j = 0
    
    while j < len(userInput):
        
        if userInput[i] == " ":
            print(userInput[i+1])
            break
        j = j + 1 
    i= i + 1
