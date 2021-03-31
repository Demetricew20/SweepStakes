from user_interface import user_interface
import sweepstakes_stack
import sweepstakes_queue


class FirmManager:
    def __init__(self):
        pass

    #Choose Manager Type
    def choice_manager_type(self):
        stack_manager = sweepstakes_stack.SweepstakesStackManager()
        queue_manager = sweepstakes_queue.SweepstakesQueueManager()
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
