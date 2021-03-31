

class Contestants:
    def __init__(self, first_name, last_name, email, registration):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration = registration
        self.contestant_list = []

    def add_to_contestant_list(self):
        self.contestant_list.append(self)



new_contestant = Contestants('John', 'Doe', 'jd@gmail.com', 5555)
new_contestant.add_to_contestant_list()



