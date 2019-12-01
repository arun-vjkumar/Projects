from unittest import TestCase

from config.config import CarromActions
from entity.clean_strike import CleanStrike


class TestCarromBoard(TestCase):
    def test_get_remaining_coins(self):
        clean_strike = CleanStrike(coins=9)
        clean_strike.apply_strike(action=CarromActions.STRIKE)
        clean_strike.apply_strike(action=CarromActions.MULTI_STRIKE)

        self.assertEqual(6, clean_strike.get_remaining_coins())

    def test_apply_carrom_action(self):
        clean_strike = CleanStrike(coins=9)
        clean_strike.apply_strike(action=CarromActions.STRIKE)
        clean_strike.apply_strike(action=CarromActions.RED_STRIKE)
        self.assertRaises(ValueError, clean_strike.apply_strike, CarromActions.RED_STRIKE)