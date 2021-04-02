import user_interface


class Contestants:
    def __init__(self, first_name, last_name, email, registration):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration = registration
        #Holds all contestants in case user does not want to register all contestants
        self.contest_list = []

    def contestants_lst(self):
        self.contest_list.append(self)

    def notify_winner(self, winner, values):
        #Pulls in winner from method in SweepStakes
        for value in values:
            email = value.email
            if value != winner[1]:
                losing_statement = user_interface.winner_statement_contestants(winner)
                user_interface.send_message(email, losing_statement)
                print(losing_statement)
            else:
                winning_statement = user_interface.winner_statement(winner)
                user_interface.send_message(email, winning_statement)
                print(winning_statement)





