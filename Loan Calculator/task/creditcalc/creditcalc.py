from math import ceil, pow, sqrt, log

class LoanCalculator:
    """
    A class representing Loan Calculator.

    :param loan_principal: Int containing value of loan principal (default None)
    :param monthly_repaids: Dictionary containing months as a keys, and repaid amounts as values
    :param monthly_payment: Amount of money user needs to pay monthly excluding last month (default None)
    :param num_of_months: Number of months needed to fully repay loan (default None)
    :param loan_interest: TODO
    :type loan_principal: int
    :type months_and_repaids: dict
    :type monthly_payment: int
    :type num_of_months: int
    :type loan_interest: TODO
    """

    def __init__(self, loan_principal=None, monthly_payment=None, num_of_months=None, loan_interest=None):
        """Initializer"""
        self.loan_principal = loan_principal
        self.months_and_repaids = {}
        self.monthly_payment = monthly_payment
        self.num_of_months = num_of_months
        self.loan_interest = loan_interest

        # calculate missing arguments using helper function
        self._init_helper_function()
        #TODO
        # if is missing
        # if is missing
        # if is missing
        # if monthly payment is provided, calculate number of months
        if self.num_of_months is None and self.monthly_payment is not None:
            self.num_of_months = self.calculate_num_of_months()

        # if number of months is provided, calculate monthly payment
        if self.num_of_months is not None and self.monthly_payment is None:
            self.monthly_payment = self.calculate_monthly_payment_int()

    #TODO init helper
    def _init_helper_function(self):
        """Helper method for calculating missing argument in the init function"""
        pass

    def __repr__(self):
        return f"Credit principal: {self.loan_principal} with {len(self.months_and_repaids)} months repaid"

    def __str__(self):
        return f"Loan principal: {self.loan_principal}"

    def calculate_monthly_payment_int(self):
        """
        Helper method for calculating monthly payment.
        :return: Return int indicating monthly payment. It does not take into consideration last month payment,
        which may differ from the basic installment. If you want to calculate exact payment for every month, use
        calculate_monthly_payment_tuple method.
        :rtype: int
        """
        return ceil(self.loan_principal / self.num_of_months)

    def calculate_monthly_payment_tuple(self):
        """
        Helper method for calculating monthly payment.
        :return: Return tuple containing monthly payments. First value is ceil of monthly payment, second value is
        the last loan installment. If last loan installment is the same as the monthly payment, second value in the
        tuple will be 0
        :rtype: tuple
        """
        base_monthly_payment = ceil(self.loan_principal / self.num_of_months)
        last_payment = self.loan_principal - ((self.num_of_months - 1) * self.monthly_payment)
        return (base_monthly_payment, 0 if last_payment == base_monthly_payment else last_payment)

    def monthly_payment_print(self):
        """Helper function for printing monthly payment"""
        monthly_payment_tuple = self.calculate_monthly_payment_tuple()
        print(f'Your monthly payment = {monthly_payment_tuple[0]}' if monthly_payment_tuple[1] == 0 else \
            f"Your monthly payment = {monthly_payment_tuple[0]} and the last payment = {monthly_payment_tuple[1]}.")

    def num_of_months_print(self):
        """Method function for printing number of months"""
        print(f"It will take 1 month to repay the loan" if self.calculate_num_of_months() == 1 else \
                f"It will take {self.calculate_num_of_months()} months to repay the loan")

    def calculate_num_of_months(self):
        """
        Helper method for calculating number of months needed to fully repay the loan.
        :return: Number of months needed to repay loan - ceil of the number
        :rtype: int
        """
        return ceil(self.loan_principal / self.monthly_payment)

    @property
    def months_repaids(self):
        """
        Getter for monthly_repaids dictionary.
        :return: String showing all months and corresponding repaid values
        :rtype: str
        """
        result = ''
        for month in self.months_and_repaids:
            result += f"Month {month}: repaid {self.months_and_repaids[month]}" + "\n"
        return result.rstrip("\n")  # strip last \n

    @months_repaids.setter
    def months_repaids(self, months_dict):
        """
        Setter for adding months with repaid values to instance monthly_repaids variable.
        :param months_dict: Dictionary with months and values. Same keys are overwritten
        :type months_dict: dict
        """
        self.months_and_repaids = {**self.months_and_repaids, **months_dict}

    def total_repaid(self):
        """
        Method for total repaid (sum of all values in the months_and_repaids dictionary).
        :return: Sum of all repaid amounts (all values in monthly_repaids dictionary)
        :rtype: int
        """
        return sum(self.months_and_repaids.values())

    def get_curret_principal(self):
        """
        Method for checking, if the loan was repaid.
        :return: String saying that credit has been repaid or int indicating how much more money is needed to repay it
        :rtype: str/int
        """
        if self.loan_principal - self.total_repaid() <= 0:
            return "The loan has been repaid!"
        else:
            return self.loan_principal - self.total_repaid()

    #TODO
    def calculate_annuity_payment(self):
        """Method with formula for calculating annuity payment"""
        pass

    #TODO
    def annuity_payment_print(self):
        pass

    #TODO
    def calculate_loan_principal(self):
        """Method with formula for calculating loan principal"""
        pass

    #TODO
    def loan_principal_print(self):
        pass

    #TODO
    def calculate_loan_interest(self):
        pass

    #TODO
    def loan_interest_print(self):
        pass

def input_handler():
    """Input handler for showing available options ans using respective constructor."""
    principal = int(input("Enter the loan principal:"))
    # print(f"What do you want to calculate?\n"
    #       f"type \"m\" - for number of monthly payments,\n"
    #       f"type \"p\" - for the monthly payment:")
    print(f"What do you want to calculate?\n"
          f"type \"n\" for number of monthly payments,\n"
          f"type \"a\" for annuity monthly payment amount,\n"
          f"type \"p\" for loan principal:")
    user_choice = input()
    if user_choice == 'n':  # user choice to provide monthly payment
        print('Enter the monthly payment:')
        user_monthly_payment = int(input())
        loan = LoanCalculator(loan_principal=principal, monthly_payment=user_monthly_payment)
        loan.num_of_months_print()

    elif user_choice == 'p':  # user choice to provide number of monthly payments
        print('Enter the number of months:')
        user_num_of_months = int(input())
        loan = LoanCalculator(loan_principal=principal, num_of_months=user_num_of_months)
        loan.monthly_payment_print()

    else:
        pass

input_handler()
