from levelup.position import Position
from typing import Tuple
from levelup.direction import Direction

class Map ():

    starting_position = Position(0,0)
    positions = []
    size: Tuple[int, int] = (10, 10)

    # Exists for easy testing
    num_positions = size[0]*size[1]

    def __init__(self):
        self.positions = [Position(x, y) for x in range(self.size[0]) for y in range(self.size[1])]

    def is_position_valid(self, position :Position) -> bool:
        return 0 <= position.x < self.size[0] and 0 <= position.y < self.size[1]       

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        new_x=current_position.x
        new_y=current_position.y
        if(direction==Direction.EAST):
            new_x = current_position.x + 1
        if(direction==Direction.WEST):
            new_x=current_position.x-1
        if(direction==Direction.NORTH):
            new_y = current_position.y + 1
        if(direction==Direction.SOUTH):
            new_y = current_position.y -1


        new_position = Position(new_x, new_y)

        if self.is_position_valid(new_position):
            return new_position
        else:
            return current_position
