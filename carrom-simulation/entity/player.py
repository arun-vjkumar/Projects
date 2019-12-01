from typing import List


class Player:

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__current_points: int = 0
        self.__action_points: List[int] = []

    @property
    def player_name(self) -> str:
        return self.__name

    @property
    def current_score(self) -> int:
        return self.__current_points

    @property
    def action_points(self) -> List[int]:
        return self.__action_points

    def played_strike(self, action_points: int) -> None:
        self.__action_points.append(action_points)
        self.__current_points += action_points

    def deduct_pts(self, pts_to_deduct: int) -> None:
        self.__current_points -= pts_to_deduct
