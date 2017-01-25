alphabet = "abcdefghijklmnopqrstuvwxyz"
characters = 0
counter1 = 0
saver1 = ""#save output strings
memory = 0#store the characters index
for characters in s:
    memory = alphabet.find(characters)
    if alphabet.find(characters) > int(memory):
        saver += characters
        counter1 += 1
    else:
        saver2 = saver1
        saver1 = ""
print("Longest substring in alphabetical order is: " + saver1)