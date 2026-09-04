from random import shuffle
from random import choice
from game_records import get_current_time
from game_records import add_record
from game_records import see_record
import matplotlib.pyplot as plt
#16 bit - python expects 4 characters (U0000-UFFFF)\u
#32 bit - python expects 8 characters(precede with zeros ex. U0001F4B4)\U
cards = {'a 2' : ['🂢','🂲','🃂','🃒'],
        'a 3' : ['🂣','🂳','🃃','🃓'],
        'a 4' : ['🂤','🂴','🃄','🃔'],
        'a 5' : ['🂥','🂵','🃅','🃕'],
        'a 6' : ['🂦','🂶','🃆','🃖'],
        'a 7' : ['🂧','🂷','🃇','🃗'],
        'an 8' : ['🂨','🂸','🃈','🃘'],
        'a 9' : ['🂩','🂹','🃉','🃙'],
        'a 10' : ['🂪','🂺','🃊','🃚'],
        'a Jack' : ['🂫','🂻','🃋','🃛'],
        'a Queen' : ['🂭','🂽','🃍','🃝'],
        'a King' : ['🂮','🂾','🃎','🃞'],
        'an Ace' : ['🂡','🂱','🃁','🃑']
        }

card_rank = {'a 2' : 2,
            'a 3' : 3,
            'a 4' : 4,
            'a 5' : 5,
            'a 6' : 6,
            'a 7' : 7,
            'an 8' : 8,
            'a 9' : 9,
            'a 10' : 10,
            'a Jack' : 11,
            'a Queen' : 12,
            'a King' : 13,
            'an Ace' : 14
            }

#print('\U0001F0AE\n\U0001F0BE\n\U0001F0CE\n\U0001F0DE')
def find_next_card(current_card,card_deck):
    card_index = card_deck.index(current_card)
    if card_index + 1 == len(card_deck):
        return ''
    else:
        next_card = card_deck[card_index+1]
        return next_card

def higher_or_lower(current_card,card_deck):
    next_card = find_next_card(current_card,card_deck)
    if card_rank.get(current_card) > card_rank.get(next_card):
        return ['lower','l']
    else:
        return ['higher','h']
    
def play_again(question):
    yes_or_no = str(input(f'{question} ')).strip().lower()
    while yes_or_no not in ['y','yes','true','t','no','n','false','f','quit']:
        print('This is a YES or NO question!')
        yes_or_no = str(input(f'{question} ')).strip().lower()
    if yes_or_no in ['y','yes','true','t']:
        return True
    else:
        return False
def main():
    while True:
        card_deck = list(cards.keys())
        shuffle(card_deck)
        current_deck = []
        current_round = 1
        #print(card_deck)
        for card in card_deck:
            if card_deck.index(card) == len(card_deck) - 1:#if we reach the last card, the loop ends
                continue
            else:
                card_face = choice(cards.get(card))
                current_deck.append(card_face)
                next_card = find_next_card(card,card_deck)
                #print(current_deck)
                print(f'Round {current_round}')
                print(' '.join(current_deck))
                print(f'The current card is {card}')
                user_guess = str(input('Higher or lower? ')).lower().strip()
                while user_guess not in ['higher','lower','quit','l','h']:
                    print('\nPlease respond with \'higher\' or \'lower\' or \'quit\'')
                    print(f'{card_face}\nThis is a {card}')
                    user_guess = str(input('Higher or lower? ')).lower().strip()
                
                check_guess = higher_or_lower(card,card_deck)
                #current_deck.append(next_card)
                #print(next_card)
                
                if user_guess in check_guess:
                    print(f'That is correct. It was indeed {check_guess[0]}. '
                        f'The next card was {next_card} :)\n')
                    current_round += 1
                    continue
                elif user_guess == 'quit':
                    break
                else:
                    print(f'That\'s wrong. It was actually {check_guess[0]} :(.'
                        f' The next card was {next_card}.\nThanks for playing.')
                    
                    break
        else:
            print('Congratulations! You have won this round :)')

        if user_guess != 'quit' or current_round != 1:
            curr_time = get_current_time()+f',{current_round},{' '.join(current_deck)}'
            add_record(curr_time)#records your attempt

        print(f"{'':=^70s}")#prints a dashed line
        
        new_round = False
        while new_round == False:
            #new_round = str(input(' ')).strip().lower()
            new_round = play_again('Would you like to play a new round?(y/n)')
            if new_round:
                continue
            
            #see_history = str(input( ')).strip().lower()
            see_history = play_again('Would you like to view your game history?')   

            if see_history:
                see_graph = play_again('Would you like to see a graph?(y/n)')
                print(f'Timestamp\t\tHighest Round reached\t\tCard Deck revealed')
                see_record()
                if see_graph:
                    print('\nGraph is being made...')
                    x_axis = see_record(stat=True).keys()
                    y_axis = see_record(stat=True).values()
                    color_scheme = ['yellow','red','blue','green','orange','grey','black','brown','violet','pink','indigo','gold']
                    shuffle(color_scheme)
                    plt.close(fig='all')
                    plt.figure(figsize=[50,20])
                    plt.bar(x_axis,y_axis,color=color_scheme)
                    plt.show(block=False)
                    print('Graph is made')
                
                continue
            else:    
                print('Thanks for playing!')
                print(f"{'':=^70s}")#prints a dashed lineb
                break
        else:
            print(f"{'':=^70s}")#prints a dashed lineb
            continue
        break

if __name__ == '__main__':
    print('HIGHER or lower\n\nThis game consists of 12 rounds where each card of a shuffled '
    'deck of 13 cards is revealed.\nThe objective of each round is to guess whether '
    'the next card in the deck is \'higher\' or \'lower\'. To end the round, you can:'
    '\n\nWIN - Guess correctly and keep guessing until you have completed all 12 rounds.' 
    '\nHint: The \'Ace\' card is the highest while the lowest is the \'2\' card'
    '\n\nLOSE - Guess incorrectly, causing the round to end and start a new round.' 
    '\n\nQUIT - Type \'quit\' at any time to end your current round and start a new round.\n')
    main()