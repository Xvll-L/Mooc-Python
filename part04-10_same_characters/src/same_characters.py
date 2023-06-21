# Write your solution here

def same_chars(text, num1,num2):
    if num1 >= len(text) or num2 >= len(text):
        return False

    if text[num1] == text[num2]:
        return True
    return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 12))