#Card Busters
#Claire Moore 14/1/2024

play_one_list = [10, 6, 8, 9, 7, 12, 7]
play_two_list = [7, 6, 9, 5, 2, 8, 11]

round_no = 0
play_one_wins = 0
play_two_wins = 0

# Calculate each round
for i in range(len(play_one_list)):
    round_no += 1
    if play_one_list[i] > play_two_list[i]:  
        play_one_wins += 1
        print(f"Round number {round_no}: Player 1 wins the round, with {play_one_list[i]} beating {play_two_list[i]}")
    elif play_one_list[i] < play_two_list[i]:  
        play_two_wins += 1
        print(f"Round number {round_no}: Player 2 wins the round, with {play_two_list[i]} beating {play_one_list[i]}")
    else:
        print(f"Round number {round_no}: This round has ended in a draw")

# Print final scores
if play_one_wins > play_two_wins:
    print(f"Player 1 wins the game, by {play_one_wins} wins to {play_two_wins}")
elif play_two_wins > play_one_wins:
    print(f"Player 2 wins the game, by {play_two_wins} wins to {play_one_wins}")
else:
    print(f"This game was a draw with Player one winning {play_one_wins} games and Player Two winning {play_two_wins} games")
    


    

    

