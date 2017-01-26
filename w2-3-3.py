# Exercise: guess my number
typeinnum = int(input("Please think of a number between 0 and 100!"))
guess = 50
print('Is your secret number ' + str(guess) + '?')
usertypein = str(input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly."))
while usertypein != "c":
	if usertypein == "h":
		guess = int(guess/2)
	else :
		guess = int(guess + guess/2)
	print('Is your secret number ' + str(guess) + '?')
	usertypein = str(input("Enter 'h' to indicate the guess is too high. \
	Enter 'l' to indicate the guess is too low. \
	Enter 'c' to indicate I guessed correctly."))
print('Game over. Your secret number was: ' + str(guess))