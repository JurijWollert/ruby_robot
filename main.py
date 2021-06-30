from lib.grid import RubyGrid
with open('input/robot_actions.txt', 'r') as instructions:
    lines = instructions.read().splitlines()

gridsize = lines.pop(0)
grid = RubyGrid(gridsize)
while len(lines) > 0:
    robot_params = lines.pop(0)
    actions = lines.pop(0)
    grid.place_robot(robot_params)
    for action in actions:
        grid.perform_action(action)
    grid.print_state()









