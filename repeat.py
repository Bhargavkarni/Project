a = "Banana"

new_string = ""

for i in a:
    if i not in new_string:
        new_string = new_string + i

print(new_string)