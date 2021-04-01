from os import system, name


def registered_statement(contestant):
    print(f'Contestant {contestant.first_name} {contestant.last_name} with registration number'
          f' {contestant.registration} is registered!')


def contestant_info(contestant):
    print(f'Name: {contestant.first_name} {contestant.last_name} / Email: {contestant.email} / '
          f'Registration #: {contestant.registration}')


def winner_statement(contestant):
    print(f'Contestant {contestant["First"]} {contestant["Last"]} with number {contestant["Registration"]} has won!')


def winner_statement_contestants(contestant):
    print(f'The sweepstakes have ended and {contestant["First"]} {contestant["Last"]} with number '
          f'{contestant["Registration"]} has won!')


def sweepstakes_name_selection():
    user_input = input('Enter name of sweepstake: ')
    return user_input


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


def clear_console():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

