from lib.grid import RubyGrid
from lib.robot import RubyRobot
import pytest

class TestGrid:
    def test_grid_creation(self):
        grid = RubyGrid('6 8')
        assert grid.rows == 8
        assert grid.cols == 6

    def test_boundary_exception(self):
        grid = RubyGrid('2 2')
        grid.robot_position = [2, 2]
        with pytest.raises(Exception):
            grid.move('N')

    def test_move(self):
        grid = RubyGrid('6 8')
        grid.robot_position = [2, 2]
        grid.move('N')
        grid.move('W')
        assert grid.robot_position == [1, 3]

    def test_error_move(self):
        grid = RubyGrid('5 5')
        grid.robot_position = [3, 5]
        with pytest.raises(Exception):
            grid.move('N')

    def test_error_placing(self):
        grid = RubyGrid('4 4')
        with pytest.raises(Exception):
            grid.place_robot('5 4 E')


class TestRuby:
    def test_ruby_robot(self):
        robot = RubyRobot('E')
        assert robot.direction == 'E'

    def test_turn(self):
        robot = RubyRobot('W')
        robot.turn('R')
        robot.turn('R')
        robot.turn('R')
        assert robot.direction == 'S'
