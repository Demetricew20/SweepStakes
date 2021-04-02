from queue_manager import Queue


class SweepstakesQueueManager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstakes):
        self.queue.enqueue(sweepstakes)

    def get_sweepstakes(self, sweepstakes):
        for contest in self.queue.queue:
            if contest == sweepstakes:
                return sweepstakes


