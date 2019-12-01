from unittest import TestCase

from config.config import CarromActions
from entity.clean_strike import CleanStrike


class TestCleanStrike(TestCase):
    def test_apply_strike(self):
        """
        Test Current Status
        """
        expected_response = """
        Coins On Board: 6
        Red Coin present on board: True
        Player 1 points: 1
        Player 2 ponts: 2
        """
        clean_strike = CleanStrike(coins=9)
        clean_strike.apply_strike(action=CarromActions.STRIKE)
        clean_strike.apply_strike(action=CarromActions.MULTI_STRIKE)
        self.assertEqual(expected_response, clean_strike.get_current_status())

        """
        Test Non scoring deduction
        """
        expected_response = """
        Coins On Board: 4
        Red Coin present on board: False
        Player 1 points: 6
        Player 2 ponts: 1
        """

        clean_strike.apply_strike(action=CarromActions.RED_STRIKE)
        clean_strike.apply_strike(action=CarromActions.NONE)
        clean_strike.apply_strike(action=CarromActions.NONE)
        clean_strike.apply_strike(action=CarromActions.NONE)
        clean_strike.apply_strike(action=CarromActions.MULTI_STRIKE)
        clean_strike.apply_strike(action=CarromActions.NONE)
        self.assertEqual(expected_response, clean_strike.get_current_status())

        """
        Test Fouls deduction
        """
        expected_response = """
        Coins On Board: 0
        Red Coin present on board: False
        Player 1 points: 2
        Player 2 ponts: 3
        """
        clean_strike.apply_strike(CarromActions.DEFUNCT_COIN)
        clean_strike.apply_strike(CarromActions.STRIKE)
        clean_strike.apply_strike(CarromActions.DEFUNCT_COIN)
        clean_strike.apply_strike(CarromActions.STRIKE)
        self.assertEqual(expected_response, clean_strike.get_current_status())

    def test_result(self):
        clean_strike = CleanStrike(coins=9)
        clean_strike.apply_strike(action=CarromActions.STRIKE)
        clean_strike.apply_strike(action=CarromActions.MULTI_STRIKE)

        self.assertRaises(RuntimeError, clean_strike.get_result)

        expected_results = 'Player 1 won the game. Final Score: 8-4'
        clean_strike.apply_strike(action=CarromActions.STRIKE)
        clean_strike.apply_strike(action=CarromActions.MULTI_STRIKE)
        clean_strike.apply_strike(action=CarromActions.STRIKE)
        clean_strike.apply_strike(action=CarromActions.NONE)
        clean_strike.apply_strike(action=CarromActions.RED_STRIKE)
        clean_strike.apply_strike(action=CarromActions.NONE)
        clean_strike.apply_strike(action=CarromActions.MULTI_STRIKE)
        self.assertEqual(expected_results, clean_strike.get_result())
