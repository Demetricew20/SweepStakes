from marketing_firm_creator import FirmManager
from sweepstakes_queue import SweepstakesQueueManager
from sweepstakes_stack import SweepstakesStackManager
from sweepstakes import SweepStakes
import user_interface


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager
        self.manager_options = FirmManager()
        self.name = ""
        self.sweepstakes = SweepStakes(self.name)
        self.stack = SweepstakesStackManager()
        self.queue = SweepstakesQueueManager()

    def create_sweepstakes(self):
        #Create name for sweepstakes
        self.name = user_interface.sweepstakes_name_selection()
        #Select manager
        self.manager_options = self.manager_options.choice_manager_type()
        sweepstake = self.sweepstakes
        self.manager.insert_sweepstakes(sweepstake)
        # Insert into stack manager when sweepstake is created
        if self.manager_options == '0':
            self.stack.insert_sweepstakes(sweepstake)
        elif self.manager_options == '1':
            self.queue.insert_sweepstakes(sweepstake)
        return sweepstake


