
class Guard:
    
    def __init__(self, position: tuple[int, int], direction: str, carte: list[str]):
        self.position: tuple[int, int] = position
        self.direction: str = direction
        self.positions_traveled: set[tuple] = set()
        self.positions_traveled.add((position[0], position[1])) # initial position
        self.stuck_positions: list[tuple] = list()
        self.is_looping: bool = False
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
                    self.position = (self.position[0], char_index-1)
                    self.direction = "South"
                    self.stuck_positions.append(self.position)
                    if self.stuck_positions.count(self.position) > 1:
                        self.is_looping = True
                    break
                else: # le garde avance
                    self.positions_traveled.add((self.position[0], char_index))
        if self.direction != "South": 
            # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
            self.position = tuple()

    def to_West(self) -> None:
        after_guard: bool = False
        for char_index, char in reversed(list(enumerate(self.map[self.position[0]]))):
            # trouver la position du garde sur la ligne :
            if char_index == self.position[1]:
                after_guard = True
                continue
            if after_guard:
                if char == "#":
                    self.position = (self.position[0], char_index+1)
                    self.direction = "North"
                    self.stuck_positions.append(self.position)
                    if self.stuck_positions.count(self.position) > 1:
                        self.is_looping = True
                    break
                else:
                    self.positions_traveled.add((self.position[0], char_index))
        if self.direction != "North": 
            # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
            self.position = ()

    def to_South(self) -> None:
        after_guard: bool = False
        for line_index, line in enumerate(self.map):
            # trouver la ligne du garde
            if line_index == self.position[0]:
                after_guard = True
            if after_guard:
                if line[self.position[1]] == '#':
                    self.position = (line_index-1, self.position[1])
                    self.direction = "West"
                    self.stuck_positions.append(self.position)
                    if self.stuck_positions.count(self.position) > 1:
                        self.is_looping = True
                    break
                else:
                    self.positions_traveled.add((line_index, self.position[1]))
        if self.direction != "West": 
            # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
            self.position = ()

    def to_North(self) -> None:
        after_guard: bool = False
        for line_index, line in reversed(list(enumerate(self.map))):
            # trouver la ligne du garde
            if line_index == self.position[0]:
                after_guard = True
            if after_guard:
                if line[self.position[1]] == '#':
                    self.position = (line_index+1, self.position[1])
                    self.direction = "East"
                    self.stuck_positions.append(self.position)
                    if self.stuck_positions.count(self.position) > 1:
                        self.is_looping = True
                    break
                else:
                    self.positions_traveled.add((line_index, self.position[1]))
        if self.direction != "East": 
            # si aucun '#' n'a été atteint, alors le garde est sorti de la carte
            self.position = ()
    
    def travel(self):
        while self.position != () and not self.is_looping:
            if self.direction == 'North':
                self.to_North()
                continue
            if self.direction == 'East':
                self.to_East()
                continue
            if self.direction == 'South':
                self.to_South()
                continue
            if self.direction == 'West':
                self.to_West()
                continue


def get_guard_initial_position(carte: list[str]) -> tuple[int, int]:
    result: tuple
    for line_index, line in enumerate(carte):
        index = line.find("^")
        if index >= 0:
            result = (line_index, index)
            break
    return result


def generate_new_map(initial_map: list[str], obstruction_position: tuple[int, int]) -> list[str]:
    
    line = initial_map[obstruction_position[0]]
    if obstruction_position[1] == len(line)-1: # s'il s'agit du dernier caractère de la ligne
        new_line = line[:obstruction_position[1]] + "#"
    else:
        new_line = line[:obstruction_position[1]] + "#" + line[obstruction_position[1]+1:]
    initial_map[obstruction_position[0]] = new_line
    return initial_map