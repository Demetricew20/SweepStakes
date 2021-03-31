from contestants import Contestants


class UI:
    def __init__(self):
        pass

    def add_contestants(self, first_name, last_name, email, registration_number):
        contestants = Contestants(first_name, last_name, email, registration_number)
        return contestants

    #Any print statements

    #Any information needed from user


user_interface = UI()

