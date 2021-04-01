import user_interface
from marketing_firm import MarketingFirm


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        user_input = user_interface.marketing_firm_manager_selection()
        if user_input == "0":
            marketing_firm = MarketingFirm(StackManager())

        marketing_firm.create_sweepstakes()
        # Create menu selection to add new contestants and register contestants
        user_interface.menu_selection_contestants()





