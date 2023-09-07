import random

class Card:
    #these tuples indicate the only suits and values permitted for a card.
    allowed_suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    allowed_values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')  
    def __init__(self, suit, value):
        if suit not in Card.allowed_suits:
            raise ValueError
        self.suit = suit
        if value not in Card.allowed_values:
            raise ValueError
        self.value = value
    
    #the repr method will return something like K of Spades when printing an instance of the card class.
    def __repr__(self):
        return (f'{self.value} of {self.suit}')
    



class Deck:
    def __init__(self):
        #The nested list comprehensions below concatenate the each value in the allowed_suits tuple with each value in the allowed_values tuple.
        self.cards = [f'{value} {suit}' for suit in Card.allowed_suits for value in Card.allowed_values]
        #Below is working code using nested for loops
        '''self.cards = []
        for suit in Card.allowed_suits:
            for value in Card.allowed_values:
                self.cards.append(value + suit)'''
        
    #the repr method will return something like Deck of 52 cards when printing an instance of the card class.  
    def __repr__(self):
        return (f'Deck of {self.count()} cards')
    
    #This makes the deck iterable.
    def __iter__(self):
        return iter(self.cards)
    
    def count(self):
        return len(self.cards)
    
    def _deal(self, num):
        try:
            #Checking to see if the deck has any cards to deal. If not, raise ValueError
            if self.count() == 0:
                raise ValueError('All Cards have been dealt')
            else:
                #if the number passed in is exactly one, the last card from self.cards is removed and returned.
                if num == 1:
                    return self.cards.pop(-1)
                #if the number of cards passed in is greater than the amount of cards left in the deck, then set num equal to the amount left in the deck.
                elif self.count() < num:
                    num = self.count()
                #if the number passed in is NOT equal to 1 and is NOT greater than the number of cards in the deck, then do nothing.
                else:
                    pass
                #This while loop is removing the last card from self.cards and adding it to a dealt list while the number of cards to deal is greater than 0. 
                dealt = []
                while num > 0:  
                    dealt.append(self.cards.pop(-1))
                    num -= 1
                return dealt
        #typeerror is thrown if the num argument is not an int or float.
        except TypeError as err:
            print('Num must be an int or float')
            print(err)
            raise
                
    
    #This method shuffles the deck only if there are 52 cards in it.
    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError('Only full decks can be shuffled')
        else:
            return random.shuffle(self.cards)
    #this method will remove a single card from self.cards and return it.    
    def deal_card(self):
        return self._deal(1)
    #this method removes the specified number of cards from self.cards and returns it in a list.
    def deal_hand(self,num):
        return self._deal(num)






# for Card repr method testing
#test = Card('Diamonds', '9')
#print(repr(test))


#deck1 = Deck()
#deck1.cards = ['A Spades']

#print(deck1.deal_card())


#for testing the Deck deal method
'''deck1.cards = ['A Spades', 'K Clubs']
print(deck1.cards)
deck1._deal('1')
print(deck1.cards)'''

#For Deck repr method testing
#print(repr(deck1))

#For testing what is actually in the deck of cards
#print(deck1.cards)

#for testing the Deck shuffle method
'''print(deck1.cards)
deck1.shuffle()
print(deck1.cards)
deck1._deal(5)
print(deck1.count())
deck1.shuffle()'''

#for testing the deal_card method
#print(deck1.cards)
#print(deck1.deal_hand(52))
#print(deck1.cards)
#deck1.deal_card()

#for testing the deah_hand method
#print(deck1.cards)
#print(deck1.deal_hand(5))
#print(deck1.cards)

#[print(card) for card in deck1]

#deck1.deal_hand('a')