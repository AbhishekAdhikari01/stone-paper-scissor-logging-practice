import random 
user_score = 0
comp_score = 0
tie = 0 
print("""choices are 
1. rock
2. paper
3. scissors """)
while True:
    choice =int(input("Enter your choice from 1-3: "))
    while choice > 3 or choice < 1 :
        choice = int(input("enter valid input"))
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"
    print("Ther user choice is: ", user_choice)   

    print("Now it is computer turns")

    computer = random.randint(1,3)

    if computer == 1:
       comp_choice = "Rock"
    elif computer == 2:
       comp_choice = "Paper"
    else:
       comp_choice = "Scissors"

    print("The computer choice is :",comp_choice)

    if (user_choice == "Paper" and comp_choice == "Stone") or (user_choice == "Stone" and comp_choice == "Paper"):
        print("Paper wins")   
        result = "paper"
    
    elif (user_choice == "Scissors" and comp_choice == "Stone" ) or (user_choice == "Stone" and comp_choice == "Scissors"):
        print("Rock wins")
        result = "Stone"
    elif (user_choice == comp_choice):
        print("its a Tie")
    else:
        print("Scissors wins")
        result = "Scissors"
    if result == "Tie":
        tie += 1
    elif result == user_choice:
        print("user wins")
        user_score += 1
    else:
        print("computer wins")
        comp_score +=1
    print("press no to quit the game")
    game = input("")
    if game == "no":
        break

    
print("score are")
print("user score is ", user_score)
print("comp_score is ",comp_score)
print("number of tie",tie)