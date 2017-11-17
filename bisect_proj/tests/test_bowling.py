import unittest

from bisect_proj.bowling import Game


class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        self._roll_many(20, 0)

        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        game = Game()

        for i in range(20):
            game.roll(1)

        self.assertEqual(20, game.score())

    def _roll_many(self, n, pins):
        for i in range(n):
            self.game.roll(pins)
