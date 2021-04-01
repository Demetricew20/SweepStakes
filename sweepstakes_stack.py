from stack_manager import Stack


class SweepstakesStackManager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)

    def get_sweepstakes(self, sweepstakes):
        #Retrieve Sweepstake
        for contest in self.stack.stack:
            if contest == sweepstakes:
                return sweepstakes



