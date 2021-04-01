import user_interface
from sweepstakes_stack import SweepstakesStackManager
from sweepstakes_queue import SweepstakesQueueManager


class FirmManager:
    def __init__(self):
        self.stack_manager = SweepstakesStackManager()
        self.queue_manager = SweepstakesQueueManager()

    #Choose Manager Type
    def choice_manager_type(self):
        while True:
            user_input = user_interface.manager_options()
            if user_input == '0':
                return user_input
            if user_input == '1':
                return user_input
            else:
                return False

