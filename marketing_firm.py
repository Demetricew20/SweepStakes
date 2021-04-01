from sweepstakes_queue import SweepstakesQueueManager
from sweepstakes_stack import SweepstakesStackManager
from sweepstakes import SweepStakes
from marketing_firm_creator import FirmManager
import user_interface



class MarketingFirm:
    def __init__(self):
        self.manager = FirmManager().choice_manager_type()

    def create_sweepstakes(self):
        #Create name for sweepstakes
        user_input = self.manager
        while True:
            if user_input == '0':
                sweepstakes = SweepStakes()
                SweepstakesStackManager().insert_sweepstakes(sweepstakes)
                return sweepstakes
            elif user_input == '1':
                sweepstakes = SweepStakes()
                SweepstakesQueueManager().insert_sweepstakes(sweepstakes)
                return sweepstakes
            elif user_input == '2':
                return False


