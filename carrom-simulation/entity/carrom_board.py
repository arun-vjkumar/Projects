from typing import List

from config.config import CarromActions, CarromActionsPointsConf
from entity.player import Player


class CarromBoard:
    def __init__(self, coins: int, num_of_players: int) -> None:
        if not 2 <= num_of_players <= 4:
            raise ValueError("Number of player should be greater than 1 and less than 4")

        self._remaining_coins = coins
        self._red_coin_on_board = True
        self._num_of_players = num_of_players
        self._players_turn: int = 0
        self._players: List[Player] = [Player(name=f'Player {i + 1}') for i in range(num_of_players)]

    def get_remaining_coins(self):
        return self._remaining_coins

    def _apply_carrom_action(self, carrom_game_config: CarromActionsPointsConf) -> None:
        if carrom_game_config.action == CarromActions.RED_STRIKE:
            if self._red_coin_on_board:
                self._red_coin_on_board = False
            else:
                raise ValueError("Invalid action red coin is already pocketed")

        if carrom_game_config.coins_to_remove_from_board <= self._remaining_coins:
            self._remaining_coins -= carrom_game_config.coins_to_remove_from_board
        else:
            raise ValueError("Pocketed coins should be less than coins on board")
