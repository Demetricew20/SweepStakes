import random
import user_interface


class SweepStakes:
    def __init__(self):
        self.name = ""
        self.registered_contestants = {}

    def sweepstake_name(self):
        name = user_interface.sweepstakes_name_selection()
        self.name = name
        return self.name

    def register_new_contestant(self, contestant):
        #Check for duplicates using registration
        if contestant.registration in self.registered_contestants:
            return None, print('Contestant has already been registered')
        else:
            self.registered_contestants[contestant.registration] = contestant
        user_interface.registered_statement(contestant)

    def print_contestant_info(self, contestant):
        user_interface.contestant_info(contestant)

    def pick_winner(self, contestant):
        items = self.registered_contestants.items()
        values = self.registered_contestants.values()
        #Choose Random Winner
        winner = random.choice(list(items))
        contestant.notify_winner(winner, values)
        return winner








