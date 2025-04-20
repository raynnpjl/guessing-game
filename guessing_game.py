from random import randint

def guessing_game(x, y):
    random_number = randint(x, y)
    user_guess = int(input('Make a guess: '))
    number_of_guess = 1
    all_the_guess = [user_guess]
    while user_guess != random_number:
        if user_guess < random_number:
            user_guess = int(input('Guess again with a larger value: '))
            number_of_guess += 1
            all_the_guess.append(user_guess)
        elif user_guess > random_number:
            user_guess = int(input('Guess again with a smaller value: '))
            number_of_guess += 1
            all_the_guess.append(user_guess)
    print('Number of guess: ' + str(number_of_guess))
    for i in all_the_guess:
        print(i)
