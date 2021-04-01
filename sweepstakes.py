import random
from contestants import *

class SweepStakes:
    def __init__(self):
        self.name = ""
        self.registered_contestants = {}

    def sweepstake_name(self):
        name = user_interface.sweepstakes_name_selection()
        self.name = name
        return self.name

    def register_new_contestant(self, contestant):
        self.registered_contestants[contestant.registration] = contestant
        #Check for duplicates using registration
        if contestant.registration in self.registered_contestants:
            return None, print('Contestant has already been registered')
        user_interface.registered_statement(contestant)

    def print_contestant_info(self, contestant):
        user_interface.contestant_info(contestant)

    def pick_winner(self):
        #Choose Random Winner
        items = self.registered_contestants.items()
        values = self.registered_contestants.values()
        winner = random.choice(list(items))
        contestant.notify_winner(winner, values)
        return winner





# sweep = SweepStakes('name')
# sweep.register_new_contestant(contestant1)
# sweep.register_new_contestant(contestant2)
# sweep.register_new_contestant(contestant3)
# sweep.print_contestant_info(contestant1)
# sweep.pick_winner()



