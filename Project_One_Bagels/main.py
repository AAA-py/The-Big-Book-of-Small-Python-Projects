import random




def opening_text():
    print("Bagels, Bagels, a deductive logic game.")
    print("Inspired by Al Sweigart al@inventwithpython.com\n")
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:    That means: \n" 
    "Pico         One digit is correct but in the wrong position.\n" 
    "Fermi        One digit is correct and in the right position.\n" 
    "Bagels       No digit is correct.\n")

def generate_random_number():
    rand_number = random.randint(100, 999)

    print("I have thought up a number")
    print("You have 10 guesses to get it")
    return rand_number


def converting_number(num_1, num_2):
    num_1_list = []
    num_2_list = []

    for digit in str(num_1):
        num_1_list.append(digit)
    
    for digit in str(num_2):
        num_2_list.append(digit)
    
    return num_1_list, num_2_list


def verifying_number(list_one, list_two):
    text = ""
    for digit in range(len(list_two)):
        if list_one == list_two:
            text = "You got it!"
        elif list_two[digit] == list_one[digit]:
            text += "Fermi "
        elif list_two[digit] in list_one:
            text += "Pico "

    if text == "":
        print("Bagels")
    else:
        print(text)


    




game_start = True



opening_text()
number = generate_random_number()

countdown = 1

while game_start:
    while countdown <= 10:
         guess = input(f"Guess #{countdown}: ")
         l_one, l_two = converting_number(number, guess)
         answer = verifying_number(l_one, l_two)


         if l_one == l_two:
            game_start = False
            countdown = 12
            
         else:
            countdown += 1
    else:
        if countdown == 11:
            print(f"You ran out of guesses! You lose! The number was {number}")
            keep_playing =input("Do you want to continue? (Y/N) ").lower()
            if keep_playing == "n":
                game_start = False
            elif keep_playing == "y":
                game_start = True
                countdown = 1
                number = generate_random_number()
        elif countdown == 12:
            keep_playing =input("Do you want to continue? (Y/N) ").lower()
            if keep_playing == "n":
                game_start = False
            elif keep_playing == "y":
                game_start = True
                countdown = 1
                number = generate_random_number()

    

    

   
    





    
