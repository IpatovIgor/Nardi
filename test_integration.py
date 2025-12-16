# test_integration.py
import unittest
import pygame
from GameControl import start_game
from GameSaver import save, restore_game, over_write
from Game import GameState


class TestIntegration(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()


    def test_save_restore_functionality(self):
        # Create a game state and test save/restore
        game_state = GameState()
        game_state.screen = self.screen
        game_state.clock = self.clock
        game_state.count_of_black = 2
        game_state.count_of_white = 1

        # Test saving
        try:
            save(game_state)
        except Exception as e:
            self.fail(f"Saving failed with error: {e}")

        # Test restoring
        try:
            new_game_state = GameState()
            new_game_state.screen = self.screen
            new_game_state.clock = self.clock
            restore_game(new_game_state)

            # Check if counts were restored
            self.assertEqual(new_game_state.count_of_black, 2)
            self.assertEqual(new_game_state.count_of_white, 1)
        except Exception as e:
            self.fail(f"Restoring failed with error: {e}")


def run_all_tests():
    # Run unit tests
    import test_game
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_game)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Run integration tests
    suite2 = loader.loadTestsFromTestCase(TestIntegration)
    result2 = runner.run(suite2)

    return result.wasSuccessful() and result2.wasSuccessful()


if __name__ == '__main__':
    run_all_tests()