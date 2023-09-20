string = input("Enter a String :  ")

alphabets = 0
digits = 0
specialChars = 0

for i in string:
    if i.isalpha():
        alphabets = alphabets + 1
    elif i.isdigit():
        digits = digits + 1
    else:
        specialChars = specialChars + 1

print("alphabets =", alphabets)
print("Digits = ", digits)
print("SpecialChars = ", specialChars)