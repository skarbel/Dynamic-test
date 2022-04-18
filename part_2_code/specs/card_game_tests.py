import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Clubs", 7)
        self.card_game = CardGame()
        self.cards = [self.card1, self.card2]
        self.total = self.card1.value + self.card2.value
        
    
    def test_check_for_ace(self):
        self.assertEqual(1, self.card1.value)

    def test_highest_card(self):
        self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(7, self.card2.value)

    def test_cards_total(self):
        self.card_game.cards_total(self.cards)
        self.assertEqual(8, self.total)

