from user_interface import user_interface
from sweepstakes_stack import SweepstakesStackManager
from sweepstakes_queue import SweepstakesQueueManager

class FirmManager:
    def __init__(self):
        self.manager_options = ['Stack Manager', 'Queue Manager']

    #Choose Manager Type
    def choice_manager_type(self):
        stack_manager = SweepstakesStackManager()
        queue_manager = SweepstakesQueueManager
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
