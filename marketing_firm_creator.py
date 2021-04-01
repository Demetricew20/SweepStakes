import user_interface


class FirmManager:
    def __init__(self):
        pass

    #Choose Manager Type
    def choice_manager_type(self):
        stack_manager = 'Stack'
        queue_manager = 'Queue'
        while True:
            user_input = user_interface.manager_options()
            if user_input == '0':
                return stack_manager
            if user_input == '1':
                return queue_manager
            else:
                return False


firm_manager = FirmManager()
firm_manager.choice_manager_type()
