# Write your solution here



while True:
    userInput = int(input("Please type in a number: "))
    i = 1
    results = 1
    while i < userInput:
        
        i = i + 1
        results = results * i
        
        
    


    if userInput <= 0:
        break
        
    print(f"The factorial of the number {userInput} is {results}")  
     
print("Thanks and bye!")        