import user_interface
from marketing_firm import MarketingFirm
import contestants
import sweepstakes
from marketing_firm_creator import FirmManager
from sweepstakes_stack import SweepstakesStackManager
from sweepstakes_queue import SweepstakesQueueManager


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        marketing_firm = MarketingFirm()
        marketing_firm.create_sweepstakes()
        sweepstakes.SweepStakes().sweepstake_name()
        new_contestants = []
        running = True
        while running is True:
            user_input = user_interface.menu_selection_contestants()
            if user_input == '0':
                contestant = contestants.Contestants(user_interface.create_contestant_first_name(),
                                                     user_interface.create_contestant_last_name(),
                                                     user_interface.create_contestant_email(),
                                                     user_interface.create_contestant_registration())
                contestant.contestants_lst()
                new_contestants.append(contestant)
            elif user_input == '1':
                ##register contestant
                for contestant in new_contestants:
                    sweepstakes.SweepStakes().register_new_contestant(contestant)
            elif user_input == '2':
                running = False


        # Create menu selection to add new contestants and register contestants






