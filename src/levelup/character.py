from levelup.position import Position
from levelup.direction import Direction
from levelup.map import Map

DEFAULT_CHARACTER_NAME = "Character"
class Character:
    # In python, we don't use getters. So no getPosition or getName for this class
    name = ""
    current_position :Position = Position(0,0)
    current_map :Map = Map()

    # Since python doesn't do method overloading, this is how we support a constructor with optional parameters
    def __init__(self, character_name=DEFAULT_CHARACTER_NAME):
        if character_name.strip() == '':
            self.name = DEFAULT_CHARACTER_NAME
        else:
            self.name = character_name

    def move(self, direction :Direction) -> None:
        new_position = self.current_map.calculate_new_position(self.current_position,direction)
        if self.current_map.is_position_valid(new_position):
            self.current_position = new_position
    
    def enter_map(self, map :Map) -> None:
        self.current_map = map
