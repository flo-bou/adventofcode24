
def get_guard_initial_position(carte: list[str]) -> list[int, int]:
    result = list()
    for line_index, line in enumerate(carte):
        index = line.find("^")
        if index >= 0:
            result = [line_index, index]
            break
    return result


class Guard:
    
    def __init__(self, position: list[int, int], direction: str, carte: list[str]):
        self.position: list[int, int] = position
        self.direction: str = direction
        self.positions_traveled: set[tuple] = set()
        self.positions_traveled.add((position[0], position[1])) # initial position
        self.map: list[str] = carte

    def to_East(self) -> None:
        after_guard: bool = False
        for char_index, char in enumerate(self.map[self.position[0]]):
            # trouver la position du garde sur la ligne :
            if char_index == self.position[1]:
                after_guard = True
                continue
            if after_guard:
                if char == "#":
                    self.position = [self.position[0], char_index-1]
                    self.direction = "South"
                    break
                else: # le garde avance
                    self.positions_traveled.add((self.position[0], char_index))
        if self.direction != "South": 
            # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
            self.position = []

    def to_West(self) -> None:
        after_guard: bool = False
        for char_index, char in reversed(list(enumerate(self.map[self.position[0]]))):
            # trouver la position du garde sur la ligne :
            if char_index == self.position[1]:
                after_guard = True
                continue
            if after_guard:
                if char == "#":
                    self.position = [self.position[0], char_index+1]
                    self.direction = "North"
                    break
                else:
                    self.positions_traveled.add((self.position[0], char_index))
        if self.direction != "North": 
            # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
            self.position = []

    def to_South(self) -> None:
        after_guard: bool = False
        for line_index, line in enumerate(self.map):
            # trouver la ligne du garde
            if line_index == self.position[0]:
                after_guard = True
            if after_guard:
                if line[self.position[1]] == '#':
                    self.position = [line_index-1, self.position[1]]
                    self.direction = "West"
                    break
                else:
                    self.positions_traveled.add((line_index, self.position[1]))
        if self.direction != "West": 
            # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
            self.position = []

    def to_North(self) -> None:
        after_guard: bool = False
        for line_index, line in reversed(list(enumerate(self.map))):
            # trouver la ligne du garde
            if line_index == self.position[0]:
                after_guard = True
            if after_guard:
                if line[self.position[1]] == '#':
                    self.position = [line_index+1, self.position[1]]
                    self.direction = "East"
                    break
                else:
                    self.positions_traveled.add((line_index, self.position[1]))
        if self.direction != "East": 
            # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
            self.position = []

