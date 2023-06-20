class calculatorROI():
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashFlow = 0
        self.coc_roi = 0
        self.investment = 0

    def total_income(self):
        rent = input("Please enter your current rent for the property: ")
        laundry = input("Please enter your current laundry rate for the property: ")
        storage = input("Please enter your current storage value for the property: ")
        misc = input("Please enter your current MISC value for the property: ")
        self.income = int(rent) + int(laundry) + int(storage) + int(misc)
        print(f"Your total income is: {self.income}")

    def total_expenses(self):
        tax = input("Enter your current tax value for the property: ")
        insurance = input("Enter your current insurance value for the property: ")
        utilities = input("Enter your total amount of utilities for the property: ")
        hoa = input("Enter your current HOA fees for the property: ")
        yard_care = input("Enter your current lawn care expense for the property: ")
        repairs = input("Enter your current repairs expense for the current property: ")
        capex = input("Enter your current capex expense for the property: ")
        management = input("Enter your current management expense fees for the property: ")
        mortgage = input("Enter your current mortgage expense for the property: ")
        self.expenses = int(tax) + int(insurance) + int(utilities) + int(hoa) + int(yard_care) + int(repairs) + int(capex) + int(management) + int(mortgage)
        print(f"Your total expenses are: {self.expenses}")
    
    def total_cashFlow(self):
        self.cashFlow = (self.income - self.expenses) * 12
        print(self.cashFlow)

    def ROI(self):
        down_payment = input("Enter your down payment of your property: ")
        closing_costs = input("Enter your closing costs of the property: ")
        rehab_budget = input("Enter your rehab budget for the property: ")
        misc_other = input("Enter your misc budget for the property: ")
        self.investment = int(down_payment) + int(closing_costs) + int(rehab_budget) + int(misc_other)
        self.coc_roi = int(self.cashFlow)/int(self.investment) * 100
        print(f"Your Cash on Cash ROI is: {self.coc_roi}%")

    def run(self):
        while True:
            print("""
            1. Find your total income
            2. Find your total expenses
            3. Find your total cashflow, annually
            4. Find your Cash on Cash ROI
            5. Exit            
            """)
            choice = input("Enter your choice: ")

            if choice == "1":
                roi.total_income()
            elif choice == "2":
                roi.total_expenses()
            elif choice == "3":
                roi.total_cashFlow()
            elif choice == "4":
                roi.ROI()
            elif choice == "5":
                break
            else:
                print("Thats not a valid option")


roi = calculatorROI()
roi.run()