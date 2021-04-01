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

    def notify_winner(self, winner):
        for contestant in self.contest_list:
            if winner == contestant:
                user_interface.winner_statement(winner)
            else:
                user_interface.winner_statement_contestants(winner)


contestant1 = Contestants('John', 'Doe', 'jd@gmail.com', 5555)
contestant2 = Contestants('Alex', 'Smith', 'as@gmail.com', 4444)
contestant3 = Contestants('Ryan', 'Johnson', 'rj@gmail.com', 3333)
contestant1.contestants_lst()
contestant2.contestants_lst()
contestant2.contestants_lst()




