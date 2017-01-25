counter = 0
counter2 = 0
compare = "a"
storage = ""
for characters in s:
	counter2 = 0
	while characters > compare:
		counter2 += 1
		compare = s[counter2]
	storage = s[counter:counter2]
	counter += 1
print("Longest substring in alphabetical order is: " + str(storage))
