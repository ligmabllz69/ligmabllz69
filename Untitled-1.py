def counting_game():
    current_number = 1
    player = 1  

    print("Welcome to the Counting Game!")
    print("Rules:")
    print("- Players take turns choosing 1, 2, or 3 numbers in sequence.")
    print("- The player who says 15 loses.")
    print("- The game starts from 1.\n")

    while current_number <= 15:
        print(f"\nCurrent number: {current_number - 1}")
        print(f"Player {player}'s turn.")

        
        while True:
            try:
                count = int(input("How many numbers will you choose (1, 2, or 3)? "))
                if 1 <= count <= 3:
                    break
                else:
                    print("Invalid input! Choose between 1 and 3.")
            except ValueError:
                print("Please enter a number between 1 and 3.")

      
        print("Numbers chosen:", end=" ")
        for i in range(count):
            print(current_number, end=" ")
            if current_number == 15:
                print(f"\nPlayer {player} said 15 and LOSES!")
                print(f"Player {3 - player} WINS!")
                return
            current_number += 1
        print()

        
        player = 2 if player == 1 else 1
counting_game()