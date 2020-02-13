import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code


#########################################
##### Name: Joe Soonthornsawad      #####
##### Uniqname: joesoon             #####
#########################################

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 

    # 1. Is rank 12 a queen?
    def test_1_queen(self):
        card = cards.Card(0,12)
        self.assertEqual(card.rank_name, "Queen")

    # 2. Is it clubs?
    def test_2_clubs(self):
        card = cards.Card(1, 1)
        self.assertEqual(card.suit_name, "Clubs")

    # 3. If you invoke the __str__ method of a card instance that is created 
    # with suit=3, rank=13, it returns the string "King of Spades"
    def test_3_str_method_spades(self):
        card = cards.Card(3,13)
        self.assertEqual(str(card), "King of Spades")

    # 4. Test that if you create a deck instance, 
    # it will have 52 cards in its cards instance variable
    def test_deck_52(self):
        deck = cards.Deck()
        self.assertEqual(len(deck.cards), 52)

    # 5. Test that if you invoke the deal_card method on a deck, 
    # it will return a card instance. --- 
    def deal_card_returns_card(self):
        deck = cards.Deck()
        self.assertIsInstance(deck.deal_card(), cards.Card)

    # 6. Test that if you invoke the deal_card method on a deck,
    # the deck has one fewer cards in it afterwards.
    def deal_card_minus_one(self):
        deck = cards.Deck()
        deck_len_before = len(deck.cards)
        deck.deal_card()
        deck_len_after = len(deck.cards)
        self.assertEqual(deck_len_before, deck_len_after)

    # 7. Test that if you invoke the replace_card method, the deck 
    # has one more card in it afterwards. (Please note that you 
    # want to use deal_card function first to remove a card from the 
    # deck and then add the same card back in)

    def replace_card_test(self):
        deck = cards.Deck()
        card_removed = deck.deal_card()
        restored_deck = deck.replace_card(card_removed)
        self.assertEqual(len(deck.cards), len(restored_deck.cards))

    # 8. Test that if you invoke the replace_card method with a card that is 
    # already in the deck, the deck size is not affected.(The function must 
    # silently ignore it if you try to add a card that’s already in the deck)

    def replace_existing_card(self):
        deck = cards.Deck()
        card_in_deck = deck.cards[0]
        deck_attempt_replace = deck.replace_card(card_in_deck)
        self.asserteEqual(len(deck.cards), len(deck_attempt_replace.cards))
        

############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
