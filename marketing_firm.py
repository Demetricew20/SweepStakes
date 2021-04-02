from sweepstakes_queue import SweepstakesQueueManager
from sweepstakes_stack import SweepstakesStackManager
from sweepstakes import SweepStakes
from marketing_firm_creator import FirmManager
import user_interface
import sys


class MarketingFirm:
    def __init__(self):
        #Utilizes method in FirmManager to set manager
        self.manager = FirmManager().choice_manager_type()
        self.sweepstakes = ''

    def create_sweepstakes(self):
        user_input = self.manager
        while True:
            if user_input == '0':
                sweepstakes = SweepStakes()
                #Inserts newly created sweepstakes to Stack Manager
                SweepstakesStackManager().insert_sweepstakes(sweepstakes)
                self.sweepstakes = sweepstakes
                return self.sweepstakes
            elif user_input == '1':
                sweepstakes = SweepStakes()
                #Inserts newly created sweepstakes to Queue Manager
                SweepstakesQueueManager().insert_sweepstakes(sweepstakes)
                self.sweepstakes = sweepstakes
                return self.sweepstakes
            else:
                user_interface.clear_console()
                return False, sys.exit()


