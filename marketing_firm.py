from marketing_firm_creator import FirmManager
from sweepstakes_queue import SweepstakesQueueManager
from sweepstakes_stack import SweepstakesStackManager
from sweepstakes import SweepStakes


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager
        self.manager_options = FirmManager()
        self.sweepstakes = SweepStakes(self.manager)
        self.stack = SweepstakesStackManager()
        self.queue = SweepstakesQueueManager()

    #Create SweepStakes
    #Valid manager options to select... Import from Firm Manager??
    def create_sweepstakes(self):
        sweepstake = self.sweepstakes
        self.manager_options = self.manager_options.choice_manager_type()
        # insert into stack manager when sweepstake is created
        if self.manager_options == '0':
            self.stack.insert_sweepstakes(sweepstake)
        elif self.manager_options == '1':
            self.queue.insert_sweepstakes(sweepstake)
        return sweepstake



marketing_firm = MarketingFirm('Stack')
marketing_firm.create_sweepstakes()

