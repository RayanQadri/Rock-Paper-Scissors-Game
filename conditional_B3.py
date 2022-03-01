while True:
    print "Time to play Rock,Paper,Scissors!"
    player1=input("Player #1 Type the number corresponding with each option. 1)Rock 2)Paper 3)Scissors: ")
    player2=input("Player #2 Type the number corresponding with each option. 1)Rock 2)Paper 3)Scissors: ")
    
    if player1 == "0":
        break
    
    
    if player1==1 and player2==1:
        print "Tie Game!"
    if player1==1 and player2==2:
        print "Player 2 Wins!"
    if player1==1 and player2==3:
        print "Player 1 Wins!"
    if player1==2 and player2==1:
        print "Player 1 Wins!"
    if player1==2 and player2==2:
        print "Tie Game!"
    if player1==2 and player2==3:
        print "Player 2 Wins!"
    if player1==3 and player2==1:
        print "Player 2 Wins!"
    if player1==3 and player2==2:
        print "Player 1 Wins!"
    if player1==3 and player2==3:
        print "Tie Game!"