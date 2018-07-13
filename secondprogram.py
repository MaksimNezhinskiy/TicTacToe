def print_field (x):
    for i in x:
        print(''.join(i), end='\n')

def check (x, dictionary):
    if ((dictionary[1] == dictionary[2] == dictionary[3] == x[0]) or
    (dictionary[1] == dictionary[4] == dictionary[7] == x[0]) or
    (dictionary[1] == dictionary[5] == dictionary[9] == x[0]) or
    (dictionary[7] == dictionary[8] == dictionary[9] == x[0]) or
    (dictionary[7] == dictionary[5] == dictionary[3] == x[0]) or
    (dictionary[3] == dictionary[6] == dictionary[9] == x[0])):
        print (x[1])
        return False
    else:
        return True
    


playing = True
while playing:
    player_one = input("Welcome to the game \n Player 1:   X   or   O \n")
    if player_one == "X":
        player_two = ["O", "Player 2 wins \n\n"]
        player_one = ["X", "Player 1 wins \n\n"]
    else:
        player_one = ["O", "Player 1 wins  \n\n"]
        player_two = ["X", "Player 2 wins \n\n"]
    ready = input ("Are you ready to start? Enter YES or NO \n")
    if ready == "Yes":
        my_dict = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ',
                    6:' ', 7:' ', 8:' ', 9:' '}
        current_game = True
        turn_counter = 0
        while current_game and turn_counter<9:
            field = [
                [my_dict[7],'|',my_dict[8],'|',my_dict[9]],
                ['-','-','-','-','-'],
                [my_dict[4],'|',my_dict[5],'|',my_dict[6]],
                ['-','-','-','-','-'],
                [my_dict[1],'|',my_dict[2],'|',my_dict[3]]
                ]
            print_field (field)
            current_input = input ("Choose your next position: 1-9 \n")
            if my_dict[int(current_input)] == ' ':
                if turn_counter%2==0:
                    my_dict[int (current_input)] = player_one[0]
                    current_game = check (player_one, my_dict)
                else:
                    my_dict[int (current_input)] = player_two[0]
                    current_game = check (player_two, my_dict)
                turn_counter+=1
            else:
                continue
        if turn_counter == 9:
            print ("DRAW GAME")
        else:
            answer = input ("Want to player again?  YES or NO \n")
            if answer != "Yes":
                print ("See you next time!")
                break
    else:
        print ("See you next time!")
        break
