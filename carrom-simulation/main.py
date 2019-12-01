import logging

from entity.clean_strike import CleanStrike
from config.config import CARROM_CONSOLE_MESSAGE_SEQUENCE

logger = logging.getLogger("main")


def get_carrom_input(player_name: str):
    console_msg = f"""
    {player_name}: Choose an outcome from the list below
    1: {CARROM_CONSOLE_MESSAGE_SEQUENCE[1].value}
    2: {CARROM_CONSOLE_MESSAGE_SEQUENCE[2].value}
    3: {CARROM_CONSOLE_MESSAGE_SEQUENCE[3].value}
    4: {CARROM_CONSOLE_MESSAGE_SEQUENCE[4].value}
    5: {CARROM_CONSOLE_MESSAGE_SEQUENCE[5].value}
    6: {CARROM_CONSOLE_MESSAGE_SEQUENCE[6].value}
    """
    input_num = input(console_msg)

    if not input_num.isdigit() or not 1 <= int(input_num) <= 6:
        raise ValueError("Input should be between 1 to 6")

    return int(input_num)


def play_clean_strike():
    clean_strike_game = CleanStrike(coins=9)

    while clean_strike_game.get_remaining_coins() > 0:
        try:
            input_num = get_carrom_input(clean_strike_game.get_current_player_name())
            clean_strike_game.apply_strike(CARROM_CONSOLE_MESSAGE_SEQUENCE[input_num])
            print(clean_strike_game.get_current_status())
        except ValueError as e:
            logger.error(e)

    print(clean_strike_game.get_result())


if __name__ == '__main__':
    play_clean_strike()