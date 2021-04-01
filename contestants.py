import user_interface


class Contestants:
    def __init__(self, first_name, last_name, email, registration):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration = registration

    def notify_winner(self, winner):
        user_interface.winner_statement(winner)
        user_interface.winner_statement_contestants(winner)

# contestant1 = Contestants('John', 'Doe', 'jd@gmail.com', 5555)
# contestant2 = Contestants('Alex', 'Smith', 'as@gmail.com', 4444)
# contestant3 = Contestants('Ryan', 'Johnson', 'rj@gmail.com', 3333)
