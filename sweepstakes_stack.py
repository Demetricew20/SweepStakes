from sweepstakes import SweepStakes

class SweepstakesStackManager:
    def __init__(self):
        pass

    #insert sweepstakes
    def insert_sweepstakes(self, sweepstakes):
        sweepstakes = SweepStakes(sweepstakes)
        ## print statement when entering sweepstake


    #get sweepstakes
    def get_sweepstakes(self, sweepstakes):
        ##Clarity on what get sweepstakes mean
        pass

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(-1)
