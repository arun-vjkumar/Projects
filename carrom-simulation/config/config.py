from enum import Enum
from typing import NamedTuple


class CarromActions(Enum):
    STRIKE = 'Strike'
    MULTI_STRIKE = 'MULTI_STRIKE'
    RED_STRIKE = 'RED_STRIKE'
    STRIKER_STRIKE = 'STRIKER_STRIKE'
    DEFUNCT_COIN = 'DEFUNCT_COIN'
    NONE = 'NONE'


class CarromActionsPointsConf(NamedTuple):
    action: CarromActions
    action_points: int
    coins_to_remove_from_board: int


class CarromConsoleSequence(NamedTuple):
    action: CarromActions
    message: str


CARROM_CONSOLE_MESSAGE_SEQUENCE = {
    1: CarromActions.STRIKE,
    2: CarromActions.MULTI_STRIKE,
    3: CarromActions.RED_STRIKE,
    4: CarromActions.STRIKER_STRIKE,
    5: CarromActions.DEFUNCT_COIN,
    6: CarromActions.NONE
}


CLEAN_STRIKE_ACTION_CONFIG = {
    CarromActions.STRIKE: CarromActionsPointsConf(action=CarromActions.STRIKE,
                                                  action_points=1,
                                                  coins_to_remove_from_board=1),
    CarromActions.MULTI_STRIKE: CarromActionsPointsConf(action=CarromActions.MULTI_STRIKE,
                                                        action_points=2,
                                                        coins_to_remove_from_board=2),
    CarromActions.RED_STRIKE: CarromActionsPointsConf(action=CarromActions.RED_STRIKE,
                                                      action_points=3,
                                                      coins_to_remove_from_board=0),
    CarromActions.STRIKER_STRIKE: CarromActionsPointsConf(action=CarromActions.STRIKER_STRIKE,
                                                          action_points=-1,
                                                          coins_to_remove_from_board=0),
    CarromActions.DEFUNCT_COIN: CarromActionsPointsConf(action=CarromActions.DEFUNCT_COIN,
                                                        action_points=-2,
                                                        coins_to_remove_from_board=1),
    CarromActions.NONE: CarromActionsPointsConf(action=CarromActions.NONE,
                                                action_points=0,
                                                coins_to_remove_from_board=0)
}
