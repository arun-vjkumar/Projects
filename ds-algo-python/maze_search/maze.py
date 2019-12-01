import random
from enum import Enum
from typing import NamedTuple, List


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows: int, cols: int, sparseness: float, start: MazeLocation, goal: MazeLocation):
        self._rows: int = rows
        self._columns: int = cols
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid = [[Cell.EMPTY for _ in range(cols)] for _ in range(rows)]
        self.__randomly_fill(rows, cols, sparseness)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def __randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for col in range(columns):
                if random.uniform(0, 1) < sparseness:
                    self._grid[row][col] = Cell.BLOCKED

    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "|".join([c.value for c in row]) + "\n"
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def get_all_successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []

        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))

        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))

        return locations

    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH

        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL


if __name__ == '__main__':
    maze = Maze(10, 10, 0.2, MazeLocation(0, 0), MazeLocation(9, 9))
    print(maze.__str__())

