import Tactic

STARTING_SCORE = 2
MAX_SCORE = 4
SCORE_DELTA = [[0, 2],
               [-1, 1]]


def evalDiff(myTurn, opponentTurn):
    return SCORE_DELTA[1 if myTurn else 0][1 if opponentTurn else 0]


class Player():
    def __init__(self, type, i, j):
        self.i = i
        self.j = j
        self.score = STARTING_SCORE
        self.type = type
        self.tactic = Tactic.getTactic(type)
        assert self.tactic is not None, f"none tactic {i} {j} {type} l"
        self.lastCoop = {}
        pass

    def removeCoop(self, x, y):
        self.lastCoop.pop((x, y), None)

    def getType(self):
        return self.type

    def play(self, x, y):
        assert self.i != x or self.j != y, "playing against yourself"
        last = self.lastCoop[(x, y)] if (x, y) in self.lastCoop else True
        return self.tactic.play(last)

    def saveResponse(self, x, y, response, myTurn):
        self.lastCoop[(x, y)] = response
        self.score += evalDiff(myTurn, response)
        if self.score > MAX_SCORE:
            self.score = MAX_SCORE

    def isDead(self):
        return self.score < 0
