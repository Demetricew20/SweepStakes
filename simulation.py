import user_interface
from marketing_firm import MarketingFirm


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        marketing_firm = MarketingFirm(user_interface.marketing_firm_manager_selection())
        marketing_firm.create_sweepstakes()
        user_interface.menu_selection_contestants()

        # Create menu selection to add new contestants and register contestants


