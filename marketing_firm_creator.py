from user_interface import user_interface

class FirmCreation:
    def __init__(self):
        self.manager_options = ['Stack Manager', 'Queue Manager']

    #Choose Manager Type
    def choice_manager_type(self):
        user_interface.manager_options()
        if user_interface.manager_options() == 0:
            ## run stack manager
            pass
        elif user_interface.manager_options() == 1:
            ## run queue manager
            pass
        else:
            user_interface.clear_console()
