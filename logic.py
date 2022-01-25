from random import randint

class user:

    def __init__(self):
        #defining the attributes of the player
        self.score = 300



class Game:
    def generate_cards(self):
    #use randint to generate the card number and assign it to a variable
        card = randint(1,13)
        return card
    
    def compute_decision(self,player_choice, original_card):
        new_card = Game.generate_cards()
        
        if player_choice == 'l':
            if original_card >= new_card:
                user.score += 100
            else:
                user.score -= 75

        elif player_choice == 'h':
            if original_card < new_card:
                user.score += 100
            else:
                user.score -= 75
        return new_card