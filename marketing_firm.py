import marketing_firm_creator
import sweepstakes


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    #Create SweepStakes
    def create_sweepStakes(self):
        marketing_firm_creator.FirmManager.choice_manager_type(self.manager)
        sweepstakes.SweepStakes(self.manager)


marketing_firm = MarketingFirm('Name')
marketing_firm.create_sweepStakes()

