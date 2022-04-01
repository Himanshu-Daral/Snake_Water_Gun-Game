import random

chances = 10


def game() :

    print("WELCOME IN THE GAME")
    print(" S for Snake \n G for Gun \n W for Water")
    lst = ["S", "W", "G"]
    i = 0
    human_point = 0
    computer_points = 0


    while(i < 10) :
        cat = input("Enter your choice : ")
        choice = random.choice(lst)

        # if cat == choice :
        #     print("Tie")
        if cat == "S" and choice == "S":
            print("Same Choice TIE")

        elif cat == "G" and choice == "G":
            print("Same Choice TIE")

        elif cat == "W" and choice == "W":
            print("Same Choice TIE")
            
        elif cat == "S" and choice == "W" :
            print("Computer Choice :",choice)
            print("You Won")
            human_point = human_point + 1

        elif cat == "S" and choice == "G":
            print("Computer Choice :",choice)
            print("You Lose")
            computer_points = computer_points + 1

        elif cat == "W" and choice == "S" :
            print("Computer Choice :",choice)
            print("You Lose")
            computer_points = computer_points + 1

        elif cat == "W" and choice == "G" :
            print("Computer Choice :",choice)
            print("You Won")
            human_point = human_point + 1

        elif cat == "G" and choice == "S" :
            print("Computer Choice :",choice)
            print("You Won")
            human_point = human_point + 1

        elif cat == "G" and choice == "W" :
            print("Computer Choice :",choice)
            print("You Lose")
            computer_points = computer_points + 1

        else :
            ("Invalid Input")

        i = i + 1
        print(f"{chances - i} left out of {chances}")
        print("Your Wins are : ",human_point)
        print("Your Loses are: ",computer_points)

    if human_point > computer_points:
        print("You Win this Game")

    elif computer_points > human_point:
        print("You Losses this Game")

    else:
        print("Score Tied")

game()


