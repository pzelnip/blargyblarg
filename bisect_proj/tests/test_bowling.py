import unittest

from bisect_proj.bowling import Game


class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        n = 20
        pins = 0
        for i in range(n):
            self.game.roll(pins)

        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        game = Game()

        for i in range(20):
            game.roll(1)

        self.assertEqual(20, game.score())
