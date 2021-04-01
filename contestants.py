import user_interface


class Contestants:
    def __init__(self, first_name, last_name, email, registration):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration = registration
        self.contest_list = []

    def contestants_lst(self):
        self.contest_list.append(self)

    def notify_winner(self, winner, values):
        for value in values:
            if value != winner[1]:
                user_interface.winner_statement_contestants(winner)
            else:
                user_interface.winner_statement(winner)



contestant1 = Contestants('John', 'Doe', 'jd@gmail.com', 1)
contestant2 = Contestants('Alex', 'Smith', 'as@gmail.com', 2)
contestant3 = Contestants('Ryan', 'Johnson', 'rj@gmail.com', 3)
contestant1.contestants_lst()
contestant2.contestants_lst()
contestant3.contestants_lst()





