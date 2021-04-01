import user_interface
import random
from collections import defaultdict
from contestants import *


class SweepStakes:
    def __init__(self, name):
        self.name = name
        self.registered_contestants = defaultdict(list)

    def register_new_contestant(self, contestant):
        lst = [('Name', f'{contestant.first_name} {contestant.last_name}'), ('Email', contestant.email),
               ('Registration', contestant.registration)]
        #Check for duplicates using registration
        if contestant.registration in self.registered_contestants['Registration']:
            return None, print(f'{contestant.first_name} {contestant.last_name} has already been registered.')
        else:
            #Append values to dictionary for each contestant
            for key, val in lst:
                self.registered_contestants[key].append(val)
                #Validation Statement
            user_interface.registered_statement(contestant)

    def print_contestant_info(self, contestant):
        user_interface.contestant_info(contestant)

    def pick_winner(self):
        #Notify winner
        randint = random.randint(0, len(self.registered_contestants) - 1)
        for i in range(0, len(self.registered_contestants)):
            winner = self.registered_contestants[randint]
            return winner



# sweep = SweepStakes('name')
# sweep.register_new_contestant(contestant1)
# sweep.register_new_contestant(contestant2)
# sweep.register_new_contestant(contestant3)
# sweep.print_contestant_info(contestant1)



