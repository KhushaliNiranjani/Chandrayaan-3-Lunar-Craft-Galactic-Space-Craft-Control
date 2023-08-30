class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.position = (x, y, z)
        self.direction = direction

    def move_forward(self):
        x, y, z = self.position
        if self.direction == 'N':
            self.position = (x, y + 1, z)
        elif self.direction == 'S':
            self.position = (x, y - 1, z)
        elif self.direction == 'E':
            self.position = (x + 1, y, z)
        elif self.direction == 'W':
            self.position = (x - 1, y, z)
        elif self.direction == 'Up':
            self.position = (x, y, z + 1)
        elif self.direction == 'Down':
            self.position = (x, y, z - 1)

    def move_backward(self):
        x, y, z = self.position
        if self.direction == 'N':
            self.position = (x, y - 1, z)
        elif self.direction == 'S':
            self.position = (x, y + 1, z)
        elif self.direction == 'E':
            self.position = (x - 1, y, z)
        elif self.direction == 'W':
            self.position = (x + 1, y, z)
        elif self.direction == 'Up':
            self.position = (x, y, z - 1)
        elif self.direction == 'Down':
            self.position = (x, y, z + 1)

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):
        if self.direction != 'Up':
            self.direction = 'Up'

    def turn_down(self):
        if self.direction != 'Down':
            self.direction = 'Down'

    def execute_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
            elif command == 'u':
                self.turn_up()
            elif command == 'd':
                self.turn_down()


# Example usage
starting_position = (0, 0, 0)
initial_direction = 'N'
#commands = ["f", "r", "u", "b", "l"]

chandrayaan_3 = Spacecraft(*starting_position, initial_direction)

