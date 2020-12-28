x = 1
while x :
    guess = input('Do you want to enter the game(Y/N) : ')
    if guess == 'Y' or guess == 'y':
        counter =1
        while counter <= 5:
            print("Type in the", counter, "number")
            global number
            number = int(input('Enter the number : '))
            counter = counter +1
            if number == 10 :
                print("Good Guess")
                break
            else:
                print("Try again!")
        if number == 10:
            print ('Game Over')
        else :
            print("Sorry but that was not very successful")
    else:
        print('See you later')
        x = 0