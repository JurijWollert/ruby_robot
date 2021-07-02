import argparse
from lib.grid import RubyGrid

parser = argparse.ArgumentParser(description='Let loose the Ruby Robot!')
parser.add_argument(
    "input",
    type=str,
    help="Provide path to input file here, necessarily as the first input."
)

args = parser.parse_args()
path = args.input

with open(path, 'r') as instructions:
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









