'''
1. Breakdown of rules and draw the pattern of the game.
2. Inputs the player names and assigning the signs to each player.
3. Putting the input between ( 1-9 ), if they dont direct them to previous state.
4. Put sign to exact spot.
5. Print the game(structure of game) after each input.
6. Check the winner and then show the winner of the game.
'''

rules = ''' 
TIC TAC TOE GAME
Positions are as follows:
    1 | 2  | 3
  ----|----|----
    4 | 5  | 6
  ----|----|----
    7 | 8  | 9 
How to play??
1. Enter the spot number (1-9) to place your mark.
2. Player 1 will use "X". and Player 2 will use "0".
3. Player_1 will go first and then Player_2.
4. Players take turns until someone will WIN or all the 9 spots will be filled.
'''
box = []
for i in range(9):
      box.append(' ')

def show_game():
     game = f'''
          {box[0]}  | {box[1]}  | {box[2]}
        -----|----|------
          {box[3]}  | {box[4]}  | {box[5]}
        -----|----|------
          {box[6]}  | {box[7]}  | {box[8]}
'''

     print(game)

index_list = []
def take_input(player_identity):
     while True:
          try:
              x = int(input(f"{player_identity}:"))
              x-=1
              if 0 <= x < 10:
                 if x in index_list:
                     print("Already taken,this spott is blocked,Choose another one.")
                     continue
                 index_list.append(x)
                 return x
              else:
                   print("Wrong Choice,PLease enter number between 1-9")
          except ValueError:
               print("Invalid input! Onlty numbers are allowed.")

    

def check_winner(p1,p2):
    if  box[0] == box[1] == box[2] == 'X' or box[1] == box[4] == box[7] == 'X' or box[0] == box[4] == box[8] == 'X' or box[2] == box[5] == box[8] == 'X' or box[3] == box[4] == box[5] == 'X' or box[2] == box[4] == box[6] == 'X' or box[6] == box[7] == box[8] == 'X' or box[0] == box[3] == box[6] == 'X' :
            print(f"Yayyy!!! {p1} Wins the Match.")
            print("Byee. JazakAllah for joining.")
            return True
    elif box[0] == box[1] == box[2] == 'O' or box[1] == box[4] == box[7] == 'O' or box[0] == box[4] == box[8] == 'O' or box[2] == box[5] == box[8] == 'O' or box[3] == box[4] == box[5] == 'O' or box[2] == box[4] == box[6] == 'O' or box[6] == box[7] == box[8] == 'O' or box[0] == box[3] == box[6] == 'O' :
             print(f"Yayyy!!! {p2} Wins the Match.")
             print("Byee. JazakAllah for joining.")
             return True
    return False




def start_game():
    print("Welcome to tIC TAC TOE!")
    player_1 = input("Enter palyer_1 identity:")
    player_2 = input("Enter player_2 identity:")
    print(f"JazakAllah for joining {player_1} and {player_2  }")

    print(rules)
    print(f"{player_1}'s sign is - X")
    print(f"{player_2}'s sign is - O")
    print("Enter any key to start the game:")
    show_game()

    for i in range(9):
        if i % 2 == 0:
             index = take_input(player_1)
             box[index] = 'X'
        else:
             index = take_input(player_2)
             box[index] = 'O'
        show_game()
        if check_winner(player_1,player_2):
             return

    print("Opps, it's a tie. Nobody Won's The Match. Play Again")
             
 

start_game()