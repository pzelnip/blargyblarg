import unittest

from bisect_proj.bowling import Game


class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        self._roll_many(20, 0)

        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        self._roll_many(20, 1)

        self.assertEqual(20, self.game.score())

    def _roll_many(self, n, pins):
        for i in range(n):
            self.game.roll(pins)
