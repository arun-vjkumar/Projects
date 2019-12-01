import logging

from config.config import CarromActions, CLEAN_STRIKE_ACTION_CONFIG
from entity.carrom_board import CarromBoard

logger = logging.getLogger('clean_strike')


class CleanStrike(CarromBoard):
    """
    Game Specific Configurations
    """
    __NUM_OF_PLAYERS = 2
    __NUM_CONTINUOUS_FOUL_DEDUCTION = 3
    __NUM_CONTINUOUS_NO_points_DEDUCTION = 3
    __PTS_TO_DEDUCT_FOR_CONTINOUS_FOULS = 1
    __PTS_TO_DEDUCT_FOR_CONTINOUS_NOT_SCORING = 1

    def __init__(self, coins: int):
        super().__init__(coins=coins, num_of_players=self.__NUM_OF_PLAYERS)

    def __apply_player_strike_action(self, action_points: int) -> None:
        self._players[self._players_turn].played_strike(action_points=action_points)

    def __deduct_player_points(self, pts_to_deduct: int) -> None:
        self._players[self._players_turn].deduct_pts(pts_to_deduct=pts_to_deduct)

    def get_current_player_name(self) -> str:
        return self._players[self._players_turn].player_name

    def __should_deduct_points_for_continuous_fouls(self) -> bool:
        latest_continuous_fouls = 0
        for point in self._players[self._players_turn].action_points[::-1]:
            if point >= 0:
                break
            latest_continuous_fouls += 1
        if latest_continuous_fouls % (self.__NUM_CONTINUOUS_FOUL_DEDUCTION + 1) == self.__NUM_CONTINUOUS_NO_points_DEDUCTION:
            return True
        return False

    def __should_deduct_points_for_continuous_not_scoring(self) -> bool:
        latest_continuous_without_points = 0
        for point in self._players[self._players_turn].action_points[::-1]:
            if point != 0:
                break
            latest_continuous_without_points += 1
        if latest_continuous_without_points % (self.__NUM_CONTINUOUS_NO_points_DEDUCTION + 1) == self.__NUM_CONTINUOUS_NO_points_DEDUCTION:
            return True
        return False

    def get_current_status(self):
        return f"""
        Coins On Board: {self._remaining_coins}
        Red Coin present on board: {self._red_coin_on_board}
        Player 1 points: {self._players[0].current_score}
        Player 2 ponts: {self._players[1].current_score}
        """

    def apply_strike(self, action: CarromActions):
        if action not in CLEAN_STRIKE_ACTION_CONFIG:
            raise ValueError("Invalid Action")

        self._apply_carrom_action(carrom_game_config=CLEAN_STRIKE_ACTION_CONFIG[action])
        self.__apply_player_strike_action(action_points=CLEAN_STRIKE_ACTION_CONFIG[action].action_points)

        if self.__should_deduct_points_for_continuous_not_scoring():
            self.__deduct_player_points(pts_to_deduct=self.__PTS_TO_DEDUCT_FOR_CONTINOUS_NOT_SCORING)

        if self.__should_deduct_points_for_continuous_fouls():
            self.__deduct_player_points(pts_to_deduct=self.__PTS_TO_DEDUCT_FOR_CONTINOUS_FOULS)

        self._players_turn = (self._players_turn + 1) % self._num_of_players

    def get_result(self):
        if self.get_remaining_coins() > 0:
            raise RuntimeError("There are coins left on the board, result will be declared ")

        if self._red_coin_on_board:
            raise RuntimeError("Red Coin is present on the board")

        if abs(self._players[0].current_score - self._players[1].current_score) > 3:
            if self._players[0].current_score > self._players[1].current_score:
                winner, runner = self._players[0],  self._players[1]
            else:
                winner, runner = self._players[1], self._players[0]
            if winner.current_score > 5:
                return f"{winner.player_name} won the game. Final Score: {winner.current_score}-{runner.current_score}"
        return f"Game Draw : Final Score: Player 1 Score:{self._players[0].current_score} Player 2 score:{self._players[1].current_score}"
