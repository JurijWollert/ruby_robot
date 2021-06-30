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

    def test_error_grid(self):
        pass

    def test_error_placing(self):
        pass


class TestRuby:
    def test_ruby_robot(self):
        robot = RubyRobot('E')
        assert robot.getter_direction() == 'E'  # real getter function?

    def test_move(self):
        grid = RubyGrid('6 8')
        grid.robot_position = [2, 2]
        grid.move('N')
        assert grid.robot_position == [2, 3]

    def test_turn(self):
        robot = RubyRobot('W')
        robot.evaluate_action('R')
        assert robot.getter_direction() == 'N'  # real getter function?

    def test_error_move(self):
        pass
