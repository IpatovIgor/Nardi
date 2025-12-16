# run_tests.py
import unittest
import sys


def run_tests():
    # Discover and run all tests in the current directory
    loader = unittest.TestLoader()
    start_dir = '.'
    pattern = 'test_*.py'
    suite = loader.discover(start_dir, pattern=pattern)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Return appropriate exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())