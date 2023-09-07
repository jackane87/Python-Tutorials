import unittest
from deck_of_cards_PassesExerciseTests_madeiterable import Card, Deck

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card('Hearts', '10')
    
    def test_suit_ValueError(self):
        '''ValueError should be raised if card creation attempted with suit other than Spades, Hearts, Clubs or Diamonds'''
        with self.assertRaises(ValueError):
            Card('Clover', '9')

    def test_value_ValueError(self):
        '''ValueError should be raised if card creation attempted with value other than A, 2, 3, 4, 5, 6, 7, 8 9 10, J, Q, K'''
        with self.assertRaises(ValueError):
            Card('Clubs', '13')
            Card('Spades', 'Jack')

    def test_init(self):
        '''Initialized card should have a valid suit and value.'''
        self.assertEqual(self.card.value, '10')
        self.assertEqual(self.card.suit, 'Hearts')

    def test_repr(self):
        '''repr function should return the card in the format "Value of Suit"'''
        self.assertEqual(repr(self.card), '10 of Hearts')


class DeckTests(unittest.TestCase):
    '''This is run before each test which essentially starts each test with a prestine deck.'''
    def setUp(self):
        self.deck = Deck()
    
    def test_Deck_init(self):
        '''Initialized deck is a list of 52 cards'''
        self.assertEqual(len(self.deck.cards), 52)
        self.assertTrue(isinstance(self.deck.cards, list))

    def test_count(self):
        '''Count method should return the current number of cards in the deck'''
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)
        self.deck.cards.clear()
        self.assertEqual(self.deck.count(), 0)

    def test_deal_sufficientcards(self):
        '''_deal method should return a list containing the number of cards passed in as well as remove the number of cards passed in from the Deck'''
        hand = self.deck._deal(5)
        self.assertEqual(len(hand), 5)
        self.assertEqual(len(self.deck.cards), 47)

    def test_deal_singlecard(self):
        '''_deal method should return the single card as a string even if there is only one card remaining in the deck'''
        self.deck.cards = ['K Clubs']
        hand = self.deck._deal(1)
        self.assertEqual(hand, 'K Clubs')
        self.assertEqual(self.deck.cards, [])

    def test_deal_insufficientcards(self):
        '''_deal method will remove the number of cards passed in from the deck in reverse and return the values in a list.
        If the number passed in is greater than the number of cards remaining in the deck, then all the remaining cards
        are removed from the deck and returned in a list in the order that the were removed, starting with the first removed card.'''
        '''
        This is the first part of the test. Deck has more than one card remaining, but more than the number of cards remaining
        is passed into _deal. As such, all remaining cards are removed from the deck and returned in a list in the order in which they were removed.
        '''
        self.deck.cards = ['A Spades', 'Q Hearts']
        hand = self.deck._deal(3)
        self.assertEqual(hand, ['Q Hearts', 'A Spades'])
        self.assertEqual(self.deck.cards, [])
        '''
        This marks the second part of the test where only a single card is left in the deck, but 2 was passed into _deal. As such,
           it is expected that the single card will be removed from the deck and returned in a list.
        '''
        self.deck.cards = ['Q Hearts']
        hand2 = self.deck._deal(2)
        self.assertEqual(hand2, ['Q Hearts'])
        self.assertEqual(self.deck.cards, [])
        

    def test_deal_nocards(self):
        '''_deal method should return a value error if there are no cards left in the deck.'''
        self.deck._deal(52)
        with self.assertRaises(ValueError) as err:
            self.deck._deal(1)
        self.assertEqual(str(err.exception), 'All Cards have been dealt')
    
    def test_deal_incorrecttype(self):
        '''_deal method should raise a typeerror if a value other than an int or float is passed in.'''
        with self.assertRaises(TypeError) as err:
            self.deck._deal('a')
        self.assertEqual(str(err.exception), "'<' not supported between instances of 'int' and 'str'")

    def test_deck_shuffle_notenoughcards(self):
        self.deck.cards.pop()
        with self.assertRaises(ValueError) as err:
            self.deck.shuffle()
        self.assertEqual(str(err.exception), 'Only full decks can be shuffled')
    
    def test_deck_shffle_enoughcards(self):
        shuffled = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, shuffled)

    def test_repr(self):
        '''repr function should return the deck in the format "Deck of Deck.count() cards"'''
        self.assertEqual(repr(self.deck),'Deck of 52 cards' )

    def test_dealcard(self):
        '''deal_card method should remove a single card from the deck and add it to a hand'''
        last_card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(last_card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_dealhand(self):
        '''deal_hand method should remove the number of passed in cards from the deck and add them to a hand'''
        last_cards = self.deck.cards[:-6:-1]
        dealt_cards = self.deck.deal_hand(5)
        self.assertEqual(last_cards, dealt_cards)
        self.assertEqual(self.deck.count(), 47)




if __name__ == '__main__':
    unittest.main()