# Write your solution here

String_Input = input("Please type in a string")

if String_Input[1] == String_Input[len(String_Input) - 2]:
    print("The second and the second to last characters are", String_Input[1])
else:
    print("The second and the second to last characters are different")

