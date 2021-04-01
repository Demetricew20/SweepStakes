from stack_manager import Stack
from marketing_firm import MarketingFirm

class SweepstakesStackManager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)




    def get_sweepstakes(self, sweepstakes):
        #Retrieve Sweepstack
        for contest in self.stack.stack:
            if contest == sweepstakes:
                return sweepstakes



