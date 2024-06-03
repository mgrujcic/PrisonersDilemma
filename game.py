from Tactic import randomType
from Player import Player
import random


class Game:
    def __init__(self, configPath):
        self.board = []
        self.loadConfig(configPath)
        self.history = []
        self.time = 0
        #self.saveState()

    def randomConfig(self, x, y):
        self.board = [[Player(randomType(), i, j) for j in range(y)]
                      for i in range(x)]

    def loadConfig(self, path):
        try:
            with open(path, 'r') as file:
                firstLine = file.readline()
                self.x, self.y = map(int, file.readline().split(' '))

                if firstLine.startswith('PRECONFIG'):
                    for i in range(self.x):
                        lineSetup = file.readline().split(' ')
                        assert len(lineSetup) == self.y
                        self.board.append([Player(type.strip(), i, j)
                                           for j, type
                                           in enumerate(lineSetup)])

                else:
                    self.randomConfig(self.x, self.y)

        except FileNotFoundError:
            print(f"File '{path}' not found.")
            return None

    def getState(self):
        return [[self.board[i][j].getType()
                for j in range(self.y)]
                for i in range(self.x)]

    def saveState(self):
        self.history.append(self.getState())

    def validNeighbours(self, i, j):
        neighbours = set()
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (di != 0 and dj != 0) and (0 <= i+di and i+di < self.x) and (0 <= j+dj and j+dj < self.y):
                    neighbours.add((i+di, j+dj))
        return neighbours

    def generatePairs(self):
        pairs = []
        allPairs = set([(i, j) for i in range(self.x) for j in range(self.y)])

        failedIters = 0
        while failedIters < 10:
            i1, j1 = random.choice(list(allPairs))
            neighbours = self.validNeighbours(i1, j1) & allPairs
            if not neighbours:
                failedIters += 1
                continue
            else:
                failedIters = 0
                i2, j2 = random.choice(list(neighbours))
                allPairs.remove((i1, j1))
                allPairs.remove((i2, j2))
                pairs.append(((i1, j1), (i2, j2)))
        return pairs

    def nextIteration(self):
        pairs = self.generatePairs()
        for pair in pairs:
            a, b = pair
            i1, j1 = a
            i2, j2 = b
            turn12 = self.board[i1][j1].play(i2, j2)
            turn21 = self.board[i2][j2].play(i1, j1)
            self.board[i1][j1].saveResponse(i2, j2, turn21, turn12)
            self.board[i2][j2].saveResponse(i1, j1, turn12, turn21)

        for i in range(self.x):
            for j in range(self.y):
                player = self.board[i][j]
                if player.isDead():
                    neighbourTypes = []
                    for i_n, j_n in self.validNeighbours(i, j):
                        #print(f"{i_n} {j_n}")
                        neighbourTypes.append(self.board[i_n][j_n].getType())
                        self.board[i_n][j_n].removeCoop(player.i, player.j)
                    self.board[i][j] = Player(random.choice(neighbourTypes), i, j)

        self.time += 1
        #self.saveState()

    def __iter__(self):
        return self

    def __next__(self):
        retTime = self.time
        retState = self.getState()
        self.nextIteration()
        return retTime, retState





if __name__ == "__main__":
    game_instance = Game(5, 5, None)
    print("X coordinate:", game_instance.x)
    print("Y coordinate:", game_instance.y)


class SimulatedGame:

    def __init__(self, configPath):
        self.game = []
        self.loadConfig(configPath)
        self.time = 0

    def loadConfig(self, path):
        try:
            with open(path, 'r') as file:
                firstLine = file.readline()
                assert firstLine.startswith('SIMULATED'), "The file does not contain a simulated game"
                self.x, self.y, self.turns = map(int, file.readline().split(' '))
                for t in range(self.turns):
                    board = []
                    for i in range(self.x):
                        lineSetup = file.readline().split(' ')
                        assert len(lineSetup) == self.y
                        board.append([lineSetup[j].strip() for j in range(self.y)])
                    self.game.append(board)
                    file.readline()

        except FileNotFoundError:
            print(f"File '{path}' not found.")
            return None


    def getState(self):
        return self.game[self.time if self.time < self.turns else -1]

    def nextIteration(self):
        self.time += 1

    def __iter__(self):
        return self

    def __next__(self):
        retTime = self.time
        retState = self.getState()
        self.nextIteration()
        return retTime, retState

        