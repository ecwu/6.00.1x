characters = 0
counter =0
for characters in s:
    if characters == "a" or characters == "e" or characters == "i" or characters == "o" or characters == "u":
        counter += 1
print("Number of vowels: " + str(counter))