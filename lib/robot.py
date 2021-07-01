class RubyRobot:
    TURN_ACTIONS = {
        'R': 1,
        'L': -1
    }

    MOVE_ACTIONS = ['M']

    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, direction: str):
        self.direction = direction

    @property
    def direction(self) -> str:
        return self.DIRECTIONS[self.__direction]

    def evaluate_action(self, activity: str) -> str:
        if activity in self.TURN_ACTIONS.keys():
            self.turn(activity)
            return 'turn'
        elif activity in self.MOVE_ACTIONS:
            return 'move'
        else:
            raise Exception(
                f"RubyRobot.evaluate_action.unknown_action_error: Recieved {activity}"
            )

    def turn(self, turn_action: str):
        current_direction = self.DIRECTIONS.index(self.direction)
        current_direction += self.TURN_ACTIONS[turn_action]
        current_direction %= 4
        self.direction = self.DIRECTIONS[current_direction]

    @direction.setter
    def direction(self, direction: str):
        try:
            self.__direction = self.DIRECTIONS.index(direction)
        except:
            raise Exception(
                f"RubyRobot.set_directions.unknown_direction_error:  Recieved {direction}"
            )
