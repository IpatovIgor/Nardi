# test_game.py
import unittest
import pygame
from Game import GameState, Washer, Base, can_move, change_move
from Cube import Cube
from timer import GameTimer


class TestGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.game_state = GameState()
        self.game_state.screen = self.screen
        self.game_state.clock = self.clock

    def test_game_state_initialization(self):
        self.assertFalse(self.game_state.move_is_going)
        self.assertEqual(self.game_state.move_color, "Black")
        self.assertEqual(self.game_state.count_of_black, 0)
        self.assertEqual(self.game_state.count_of_white, 0)

    def test_change_move(self):
        # Test initial state
        self.assertEqual(self.game_state.move_color, "Black")

        # Test first change
        change_move(self.game_state)
        self.assertEqual(self.game_state.move_color, "White")
        self.assertFalse(self.game_state.cubs_was_trow)
        self.assertEqual(self.game_state.move_index, 0)

        # Test second change
        change_move(self.game_state)
        self.assertEqual(self.game_state.move_color, "Black")

    def test_washer_creation(self):
        base = Base(self.game_state, 100, 100, 1, "Up")
        washer = Washer("Black", 100, 100, base, 0)

        self.assertEqual(washer.color, "Black")
        self.assertEqual(washer.base, base)
        self.assertEqual(washer.index, 0)
        self.assertIsNotNone(washer.normalImage)
        self.assertIsNotNone(washer.bigImage)

    def test_base_operations(self):
        base = Base(self.game_state, 100, 100, 1, "Up")
        washer = Washer("Black", 100, 100, base, 0)

        # Test adding washer
        base.add_washer(washer)
        self.assertEqual(base.count, 1)
        self.assertEqual(len(base.washers), 1)

        # Test popping washer
        base.pop_washer()
        self.assertEqual(base.count, 0)
        self.assertEqual(len(base.washers), 0)


class TestCube(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.cube = Cube()

    def test_cube_creation(self):
        self.assertEqual(len(self.cube.cube_list), 6)
        self.assertIsNotNone(self.cube.imageE)

    def test_throw_cubes_range(self):
        result = self.cube.throw_cubs(self.screen, self.clock)

        # Check that result is a list of two numbers
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

        # Check that numbers are in valid range
        self.assertGreaterEqual(result[0], 1)
        self.assertLessEqual(result[0], 6)
        self.assertGreaterEqual(result[1], 1)
        self.assertLessEqual(result[1], 6)


class TestTimer(unittest.TestCase):
    def setUp(self):
        self.timer = GameTimer()

    def test_timer_initialization(self):
        self.assertFalse(self.timer.paused)
        self.assertEqual(self.timer.total_pause_time, 0)

    def test_timer_pause_resume(self):
        # Timer should be running initially
        time1 = self.timer.get_time()
        self.assertGreaterEqual(time1, 0)

        # Pause timer
        self.timer.pause()
        self.assertTrue(self.timer.paused)

        # Resume timer
        self.timer.resume()
        self.assertFalse(self.timer.paused)

    def test_timer_reset(self):
        self.timer.reset()
        self.assertFalse(self.timer.paused)
        self.assertEqual(self.timer.total_pause_time, 0)


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.game_state = GameState()
        self.game_state.screen = self.screen
        self.game_state.clock = self.clock


if __name__ == '__main__':
    unittest.main()