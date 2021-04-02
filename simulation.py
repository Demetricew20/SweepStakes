import user_interface
from marketing_firm import MarketingFirm
import contestants


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        marketing_firm = MarketingFirm()
        marketing_firm.create_sweepstakes()
        marketing_firm.sweepstakes.sweepstake_name()
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
                for contestant in new_contestants:
                    marketing_firm.sweepstakes.register_new_contestant(contestant)
            elif user_input == '2':
                marketing_firm.sweepstakes.pick_winner(new_contestants[0])
            else:
                user_interface.clear_console()
                running = False







