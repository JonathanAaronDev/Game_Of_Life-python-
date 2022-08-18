class Cell:
    def __init__(self, row, column, state, counter):
        self.row = row
        self.column = column
        self.state = False
        self.counter = 0

    def myfunc(self):
        print("Hello my position is " + "row: " + str(self.row) + " col: " + str(self.column) + " state is: " + str(
            self.state))

    def counterADD(self):
        self.counter = self.counter + 1
