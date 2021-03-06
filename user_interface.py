import smtplib, ssl
from email.message import EmailMessage

#User Selections


def menu_selection_contestants():
    validate_option = (False, None)
    while validate_option[0] is False:
        print("\tPress -0- To Add Contestants")
        print("\tPress -1- To Register Contestants")
        print("\tPress -2- To Pick Winner")
        print("\tPress -3- to terminate program")
        user_input = input('Press number: ')
        validate_user_selection = validate_manager_options(user_input)
        return validate_user_selection[1]


def manager_options():
    print('Please choose from available management options: Stack Manager or Queue Manager')
    validate_option = (False, None)
    while validate_option[0] is False:
        print("\tPress -0- for Stack Manager")
        print("\tPress -1- for Queue Manager")
        print("\tPress -2- to terminate program")
        user_input = input('Press number: ')
        validate_user_selection = validate_manager_options(user_input)
        return validate_user_selection[1]


def validate_manager_options(user_input):
    """Validation function that checks if 'user_input' argument is an int 0-3. No errors."""
    switcher = {
        '0': (True, '0'),
        '1': (True, '1'),
        '2': (True, '2'),
    }
    return switcher.get(user_input, (True, None))


def sweepstakes_name_selection():
    user_input = input('Enter name of sweepstake: ')
    return user_input

#Create contestant


def create_contestant_first_name():
    f_name_input = input('Enter first name: ')
    return f_name_input


def create_contestant_last_name():
    l_name_input = input('Enter last name: ')
    return l_name_input


def create_contestant_email():
    email = input('Enter email address: ')
    return email


def create_contestant_registration():
    register = input('Enter registration number: ')
    return register

#Print Statements


def registered_statement(contestant):
    print(f'Contestant {contestant.first_name} {contestant.last_name} with registration number'
          f' {contestant.registration} is registered!')


def contestant_info(contestant):
    print(f'Name: {contestant.first_name} {contestant.last_name} / Email: {contestant.email} / '
          f'Registration #: {contestant.registration}')


def winner_statement(winner):
    statement = f'{winner[1].first_name} {winner[1].last_name} congratulations! You are the winner of our sweepstakes!'
    return statement


def winner_statement_contestants(winner):
    statement = f'The sweepstakes has ended and {winner[1].first_name} {winner[1].last_name} with registration number ' \
                f'{winner[1].registration} has won. Please try again in our next contest.'
    return statement

#Email & Console


def send_message(recipients, statement):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    #From
    sender_email = "your@gmail.com"
    #To
    receiver_email = recipients
    # Ask for user email password. Remove input and place email password for automatic approval of emails
    # password = input("Type your password and press enter:")
    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Sweepstakes!'
    message.set_payload(statement)
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        try:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.send_message(message)

        except:
            print('Error')

        finally:
            server.quit()


def clear_console():
    print('\n' * 10)
