

class Game(object):
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        score = 0
        frame_index = 0
        for frame in range(10):
            if self._is_spare(frame_index):
                score += 10 + self._rolls[frame_index + 2]
            else:
                score += self._rolls[frame_index] + self._rolls[frame_index + 1]
            frame_index += 2
        return score

    def _is_spare(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1] == 10
