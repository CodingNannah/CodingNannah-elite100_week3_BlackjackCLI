""" Start for Four-Player Option: 

state_name = input("Enter your name here: ")
print("Welcome {name} to Coding Nannah's Black Jack Game!")

seat = input("There are four seats. Choose your seat by selecting a number 1 through 4.  ")
seat_occupied = []

def picking_seats(seat):
    while seat in ["1","2","3","4"] and not in seat_occupied():
        print(f"Good choice you may take a seat at seat " + {seat} + ".")
        seat_occupied.append(int())
    elif seat in seat_occupied():
        input(f"You cannot choose seat " + {seat},"." + " That seat is already taken. Please select another seat. ")
        continue        
    else:
        print("Please try that again.")

    another_player = input("Is there another player? (Y/N)) ")
        if another_player.lower() != 'y' and another_player.lower() != 'n'
            print("Please try that again.")
            return another_player
        
        elif another_player.lower() = 'y':
            return state_name

        in another_player.lower() = 'n'
        
    print("Now that everyone is seated. Let's play {} us proceed.")

picking_seats(seat)

"""