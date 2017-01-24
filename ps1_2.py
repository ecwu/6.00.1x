counter = 0
bob = 0
for characters in s:
    if s[counter:counter+3] == "bob":
        bob += 1
    counter += 1
print("Number of times bob occurs is: " + str(bob))