from enum import Enum

# Allows us to use this direction enum across different classes
# Prewritten for you - no changes needed
class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

    def get_delta_x(self):
        return 1
    def get_delta_y(self):
        return 1