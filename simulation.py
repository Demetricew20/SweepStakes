import user_interface
from marketing_firm import MarketingFirm
from marketing_firm_creator import FirmManager
from sweepstakes_stack import SweepstakesStackManager
from sweepstakes_queue import SweepstakesQueueManager


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        marketing_firm = MarketingFirm()
        marketing_firm.create_sweepstakes()


        # Create menu selection to add new contestants and register contestants
        # user_interface.menu_selection_contestants()





