from sweepstakes import SweepStakes

class SweepstakesQueueManager:
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


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)