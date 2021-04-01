import user_interface
import random

class SweepStakes:
    def __init__(self, name):
        self.name = name
        #Place multiple contestants ****
        self.registered_contestants = [{'First': "", 'Last': "", 'Email': "", 'Registration': ""}, ]

    def register_new_contestant(self, contestant):
        #Iterate through all contestants to register them, check for duplicates ****
        self.registered_contestants[0]['First'] = contestant.first_name
        self.registered_contestants[0]['Last'] = contestant.last_name
        self.registered_contestants[0]['Email'] = contestant.email
        self.registered_contestants[0]['Registration'] = contestant.registration
        user_interface.registered_statement(contestant)

    def print_contestant_info(self, contestant):
        user_interface.contestant_info(contestant)

    def pick_winner(self):
        #Notify All Contestants
        randint = random.randint(0, len(self.registered_contestants) - 1)
        for i in range(0, len(self.registered_contestants)):
            winner = self.registered_contestants[randint]
            return winner and user_interface.winner_statement_firm(winner)






