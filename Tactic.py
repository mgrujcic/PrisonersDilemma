import random

validTactics = ['T', 'A', 'D', 'C']


def randomType():
    return random.choice(validTactics)


def getTactic(type):
    if type == 'T':
        return TitForTat()
    elif type == 'A':
        return AntiTitForTat()
    elif type == 'D':
        return Defector()
    elif type == 'C':
        return Cooperator()
    else:
        return None


class Tactic():
    def __init__(self):
        pass

    def play(self, lastCoop):
        pass


class TitForTat(Tactic):
    def __init__(self):
        super().__init__()

    def play(self, lastCoop):
        return lastCoop


class AntiTitForTat(Tactic):
    def __init__(self):
        super().__init__()

    def play(self, lastCoop):
        return not lastCoop


class Defector(Tactic):
    def __init__(self):
        super().__init__()

    def play(self, lastCoop):
        return False


class Cooperator(Tactic):
    def __init__(self):
        super().__init__()

    def play(self, lastCoop):
        return True
