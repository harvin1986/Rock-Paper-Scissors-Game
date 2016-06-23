import random
NAME = input("Hello Player!\nEnter your name: ")

def main():
    again = 'y'

    while again == 'y' or again == 'Y':

        comp = random.randint(1, 3)

        if comp == 1:
            comp = 'ROCK'
        if comp == 2:
            comp = 'PAPER' 
        if comp == 3:
            comp = 'SCISSORS'
        
        player = input('\nEnter your selection; ROCK, PAPER, SCISSORS: \n{ENTER SELECTION IN ALL UPPERCASE!} \n')

        print('\n',NAME,': ',player, sep='')
        print('Computer:',comp,'\n')

        if player == 'ROCK':
            if comp == 'PAPER':
                print('>>> YOU JUST TOOK A MEEK MILLS SON! HA HA HA!!!')
            if comp == 'SCISSORS':
                print('>>> You Win!')
        if player == 'SCISSORS':
            if comp == 'PAPER':
                print('>>> You Win!')
            if comp == 'ROCK':
                print('>>> YOU JUST TOOK A MEEK MILLS SON! HA HA HA!!!')
        if player == 'PAPER':
            if comp == 'ROCK':
                print('>>> You Win!\n')
            if comp == 'SCISSORS':
                print('>>> YOU JUST TOOK A MEEK MILLS SON! HA HA HA!!!')
        if comp == player:
                print('>>> TIE')
                

        again = input('\nWould you like to continue? {y = yes, any other key = no}\n')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
main()
        
