import random

def evaluate():
    key={1: "Rock", 2: "paper", 3: "scissors"}
    {"Rock": 1, "paper": 2,"scissors": 3}
    choice = int(input("rock paper or scissors\n1: Rock, 2: paper, 3: scissors\nYou can use numbers instead of words\n"))
    options = [1,2,3]
    choice_comp = random.choice(options)

    print(choice_comp)
    user_points = 0
    comp_points = 0
    
    if choice_comp == choice:
        print("You choose ", key[choice])
        print("Computer chooses ", key[choice_comp])
        print("It's a Tie")
        print("You: " ,user_points)
        print("Comp: " ,comp_points)
        return user_points
    elif choice == 1:
        if choice_comp == 2:
            print("You choose ", key[choice])
            print("Computer chooses ", key[choice_comp])
            print( "You Loose")
            comp_points += 1
            print("You: ", user_points)
            print("Comp: ", comp_points)
        
        elif choice_comp == 3:
            print("You choose ", key[choice])
            print("Computer chooses ", key[choice_comp])
            print( "You Win")
            user_points += 1
            print("You: " ,user_points)
            print("Comp: " ,comp_points)
            
        else:
            print("Error in your input")
        
    elif choice == 2:
        if choice_comp == 1:
            comp_points += 1
            print("You choose ", key[choice])
            print("Computer chooses ", key[choice_comp])
            print("You Loose")
            print("You: " ,user_points)
            print("Comp: " ,comp_points)
        elif choice_comp == 3:
            print("You choose ", key[choice])
            print("Computer chooses ", key[choice_comp])
            user_points += 1
            print("You Win")
            print("You: " ,user_points)
            print("Comp: " ,comp_points)
        else:
            print("Error in your input")
            return user_points
        
    elif choice == 3:
        if choice_comp == 2:
            user_points += 1
            print("You choose ", key[choice])
            print("Computer chooses ", key[choice_comp])
            print("You Win")
            print("You: " ,user_points)
            print("Comp: " ,comp_points)
        elif choice == 1:
            user_points -= 1
            print("You choose ", key[choice])
            print("Computer chooses ", key[choice_comp])
            print("You Loose")
            print("You: " ,user_points)
            print("Comp: " ,comp_points)
        else:
            print("Error in your input")

    
#number_to_choice()
#choice_to_number(choice)
#dict_to_choice(options)

for _ in range(10):
    evaluate()
    print("---------------------------------------------------------------------")








