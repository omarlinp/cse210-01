from random import randint
#defining user

class User:

    def __init__(self):
        #defining the attributes of the player
        self.score = 75



class Card:
    def __init__(self):
        self.card = 0
#create the function to generate the card number
    def generate_cards(self):
    #use randint to generate the card number and assign it to a variable
        card = randint(1,13)
        return card

player = User()
cards = Card()

def compute_decision(player_choice, original_card):
    new_card = cards.generate_cards()
    
    if player_choice == 'l':
        if original_card >= new_card:
            player.score += 100
        else:
            player.score -= 75

    elif player_choice == 'h':
        if original_card < new_card:
            player.score += 100
        else:
            player.score -= 75
    return new_card
            
    
staring_card = cards.generate_cards()
print(f'You have {player.score}')

while player.score > 0:
    
    
    
    
    print(f'The card is: {staring_card}')
    
    player_decision = input('Higher or lower [h/l] ').lower()
    staring_card = compute_decision(player_decision,staring_card)
    print(f'Next card was: {staring_card}')
    print(f'You have {player.score}')
    if player.score > 0:
        continue_game = input('Play again? [y/n] ').lower()
        if continue_game == 'n':
            break
        else:
            continue
