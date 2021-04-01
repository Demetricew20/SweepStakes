import marketing_firm_creator
import sweepstakes
import sweepstakes_stack, sweepstakes_queue


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    #Create SweepStakes
    def create_sweepStakes(self):
        manager_selection = marketing_firm_creator.FirmManager.choice_manager_type(self.manager)
        created_sweepstakes = sweepstakes.SweepStakes(self.manager)
        if manager_selection == 'Stack':
            sweepstakes_stack.SweepstakesStackManager.insert_sweepstakes(self.manager, created_sweepstakes)
        elif manager_selection == 'Queue':
            sweepstakes_queue.SweepstakesQueueManager.insert_sweepstakes(self.manager, created_sweepstakes)


marketing_firm = MarketingFirm('Name')
marketing_firm.create_sweepStakes()

