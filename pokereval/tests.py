import unittest
from test import support as test_support 

from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator


class TwoCardsTestCase(unittest.TestCase):

    def test_two_cards(self):
        hole = [Card(2, 1), Card(2, 2)]
        board = []
        score = HandEvaluator.evaluate_hand(hole, board)
        self.assertEqual(score, 0.52337858220211153)


class FiveCardsTestCase(unittest.TestCase):

    def test_five_cards(self):
        hole = [Card(2, 1), Card(2, 2)]
        board = [Card(2, 3), Card(3, 3), Card(4, 3)]
        score = HandEvaluator.evaluate_hand(hole, board)
        self.assertEqual(score, 0.9250693802035153)


class SixCardsTestCase(unittest.TestCase):

    def test_five_cards(self):
        hole = [Card(2, 1), Card(2, 2)]
        board = [Card(2, 3), Card(3, 3), Card(4, 3), Card(5, 3)]
        score = HandEvaluator.evaluate_hand(hole, board)
        self.assertEqual(score, 0.4405797101449275)


class SevenCardsTestCase(unittest.TestCase):

    def test_five_cards(self):
        hole = [Card(2, 1), Card(2, 2)]
        board = [Card(2, 3), Card(3, 3), Card(4, 3), Card(5, 3), Card(5, 4)]
        score = HandEvaluator.evaluate_hand(hole, board)
        self.assertEqual(score, 0.8909090909090909)


def test_main():
    test_support.run_unittest(TwoCardsTestCase,
                              FiveCardsTestCase,
                              SixCardsTestCase,
                              SevenCardsTestCase,
                             )


if __name__ == "__main__":
    test_main()
