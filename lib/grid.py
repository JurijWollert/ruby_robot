from lib.robot import RubyRobot

class RubyGrid:
    def __init__(self, gridsize):
        self.create_grid(gridsize)

    def create_grid(self, gridsize: str):
        try:
            cols, rows = gridsize.split(' ')
            rows = int(rows)
            cols = int(cols)
        except:
            raise Exception(
                f'RubyGrid.create_grid.malformed_input_error: Recieved {gridsize}')
        self.rows = rows
        self.cols = cols

    def place_robot(self, combined_input: str):
        try:
            *position, direction = combined_input.split(' ')
            position = [int(i) for i in position]
        except:
            raise Exception(
                f'RubyGrid.place_robot.malformed_input_error: Recieved {combined_input}')
        self.robot = RubyRobot(direction)
        self.robot_position = position

    def move(self, direction): ## check if robot is placed?
        if direction == 'N':
            self.robot_position[1] += 1
        if direction == 'S':
            self.robot_position[1] -= 1
        if direction == 'E':
            self.robot_position[0] += 1
        if direction == 'W':
            self.robot_position[0] -= 1
        self._verify_position()

    def _verify_position(self):
        x_valid = 0 <= self.robot_position[1] < self.rows
        y_valid = 0 <= self.robot_position[0] < self.cols

        if not x_valid & y_valid:
            raise Exception('RubyGrid.verify_position.out_of_bounds_error')

    def perform_action(self, activity: str):
        action = self.robot.evaluate_action(activity)
        if action == 'move':
            self.move(self.robot.getter_direction())
        elif action == 'turn':
            pass
        else:
            raise Exception(
                f'RubyGrid.perform_action.unkown_action_error: Recieved {action}')

    def print_state(self):
        print(
            self.robot_position[0],
            self.robot_position[1],
            self.robot.getter_direction()
        )
