import random as r

roll = r.randint(1, 6)

while True:
    players = input("Enter the number of players: ")

    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Enter a valid number (1-4)")

print(f"Number of players: {players}")

max_score = 50
player_score = [0] * players
current_score = [0] * players

while max(player_score) < max_score:
    for i in range(players):
        yeno = input(f"Player {i+1}, do you want to roll the dice? (y/n) ")
        if yeno.lower() == "y":
            roll = r.randint(1, 6)
            print(f"Player {i+1} got the value {roll}")
            if roll == 1:
                print(f"Player {i+1} got a 1, their current score is 0.")
                current_score[i] = 0
            else:
                current_score[i] += roll
                print(f"Player {i+1}'s current score is {current_score[i]}")

            player_score[i] += current_score[i]
            print(f"Player {i+1} score: {player_score[i]}")

        if max(player_score) >= max_score:
            print("Game over!")
            break
    else:
        continue
    break
    
    

    

    
      
