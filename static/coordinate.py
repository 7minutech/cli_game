class Coordinate:

    def __init__(self, position):
        self.position = position
        self.row = position[0]
        self.col = position[1]

    def __str__(self):
        return f"Row: {self.position[0]}, Col: {self.position[1]}"
    
    def __repr__(self):
        return f"Position({self.position[0]}, {self.position[1]})"
    
    def __add__(self, other):
        return Coordinate((self.position[0] + other.position[0], self.position[1] + other.position[1]))
    
    def __eq__(self, other):
        if type(other) != Coordinate:
            return False
        return(self.row == other.row and self.col == other.col)