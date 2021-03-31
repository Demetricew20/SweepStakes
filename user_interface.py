from contestants import Contestants


class UI:
    def __init__(self):
        self.contestant_list = []

    def contestant_list(self):
        contestants_list = self.contestant_list
        return contestants_list

    def registered_statement(self, contestant):
        print(f'Contestant {contestant.registration} is registered!')


    def contestant_info(self, contestant):
        print(f'Name: {contestant.first_name} {contestant.last_name} / Email: {contestant.email} / '
              f'Registration #: {contestant.registration}')
    #Any print statements

    #Any information needed from user


user_interface = UI()
