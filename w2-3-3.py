# Exercise: guess my number
print("Please think of a number between 0 and 100!")
guess = 50
amnum=50
print('Is your secret number ' + str(guess) + '?')
usertypein = str(input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly."))
while usertypein != "c":
    amnum = amnum/2
    if usertypein == "h":
        guess = guess-amnum
    else :
        guess = guess+amnum
    print('Is your secret number ' + str(int(guess)) + '?')
    usertypein = str(input("Enter 'h' to indicate the guess is too high. \
    Enter 'l' to indicate the guess is too low. \
    Enter 'c' to indicate I guessed correctly."))
print('Game over. Your secret number was: ' + str(int(guess)))