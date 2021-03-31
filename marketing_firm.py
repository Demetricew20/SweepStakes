from sweepstakes import SweepStakes

class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    #Create SweepStakes
    def create_sweepStakes(self, name):
        name = SweepStakes(name)


