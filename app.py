player1 = input("Player1...rock,paper,or scissors?")
player2 = input("Player2...rock, paper, or scissors?")
if player1 == player2:
    print("tie")
if player1 == "rock": 
    if player2 == "paper":
        print("Player2 wins!")
    elif player2 == "scissors":
        print("Player1 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("PLayer1 wins!")
    elif player2 == "scissors":
        print("player2 wins!")
elif player1 == "scissors":
    if player2 == "rock":
        print("Player2 wins!")
    elif player2 == "paper":
        print("Player1 wins!")
    