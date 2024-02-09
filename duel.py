import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    •    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ •       │",
        "│         │",
        "│       • │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ •       │",
        "│    •    │",
        "│       • │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ •     • │",
        "│         │",
        "│ •     • │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ •     • │",
        "│    •    │",
        "│ •     • │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ •  •  • │",
        "│         │",
        "│ •  •  • │",
        "└─────────┘")
}

def duel():
    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")

    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)
    print()
    print(f"{player1} rolled a {player1_roll}!")
    print(f"{player2} rolled a {player2_roll}!")
    print()
    
    for line in range(5):
        print(dice_art[player1_roll][line], dice_art[player2_roll][line])


    if player1_roll > player2_roll:
        print(f"{player1} wins the duel!")
    elif player1_roll < player2_roll:
        print(f"{player2} wins the duel!")
    else:
        print("The duel is a draw!")

duel()
