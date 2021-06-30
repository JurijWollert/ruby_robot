
class RubyRobot:
    TURN_ACTIONS = {
        'R': 1,
        'L': -1
    }

    MOVE_ACTIONS = ['M']

    DIRECTIONS = ['N','E','S','W']

    def __init__(self, direction: str):
        self.set_direction(direction)

    def getter_direction(self) -> str:
        return self.DIRECTIONS[self.direction]

    def evaluate_action(self, activity: str) -> str:
        if activity in self.TURN_ACTIONS.keys():
            self.turn(activity)
            return 'turn'
        elif activity in self.MOVE_ACTIONS:
            return 'move'
        else:
            raise Exception("RubyRobot.evaluate_action.unknown_action_error")

    def turn(self, turn_action: str):
        self.direction += self.TURN_ACTIONS[turn_action]
        self.direction %= 4

    def set_direction(self, direction: str):
        try:
            self.direction = self.DIRECTIONS.index(direction)
        except:
            raise Exception("RubyRobot.set_directions.unknown_direction_error")

