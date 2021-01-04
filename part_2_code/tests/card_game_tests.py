import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card("spades", 1)
        self.card_2 = Card("hearts", 12)

        self.card_game = CardGame()

    def test_check_for_ace__returns_true(self):
        self.assertTrue(self.card_game.check_for_ace(self.card_1))

    def test_check_for_ace__returns_false(self):
        self.assertFalse(self.card_game.check_for_ace(self.card_2))