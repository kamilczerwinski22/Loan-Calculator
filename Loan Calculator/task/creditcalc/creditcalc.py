from math import ceil, pow, sqrt, log

class LoanCalculator:
    """
    A class representing Loan Calculator.

    :param loan_principal: Int or float containing value of loan principal (default None)
    :param monthly_repaids: Dictionary containing months as a keys, and repaid amounts as values
    :param annuity_monthly_payment: Amount of money user needs to pay monthly excluding last month (default None)
    :param num_of_payments: Number of months needed to fully repay loan (default None)
    :param loan_interest: Loan interest value. Input type is int and represents % (default None)
    :type loan_principal: int/float
    :type months_and_repaids: dict
    :type annuity_monthly_payment: int/float
    :type num_of_payments: int
    :type loan_interest: int/float
    """

    def __init__(self, loan_principal=None, annuity_monthly_payment=None, num_of_payments=None, loan_interest=0):
        """Initializer"""
        self.loan_principal = loan_principal
        self.months_and_repaids = {}
        self.annuity_monthly_payment = annuity_monthly_payment
        self.num_of_payments = num_of_payments
        self.loan_interest = loan_interest

        # calculate missing arguments using helper function
        self._init_helper_function()

    def _init_helper_function(self):
        """
        Helper method for calculating missing argument in the init function. Use adequate methods for calculating
        variables which value is None after initialization.
        """
        # calculate loan interest from % to float number
        self.calculate_loan_interest()

        # if loan_principal is missing
        if self.loan_principal is None:
            self.calculate_loan_principal()

        # if monthly_payment is missing
        if self.annuity_monthly_payment is None:
            self.calculate_annuity_payment()

        # if num_of_months is missing
        if self.num_of_payments is None:
            self.calculate_num_of_monthly_payments()

    def __repr__(self):
        return f"Credit principal: {self.loan_principal} with {len(self.months_and_repaids)} months repaid"

    def __str__(self):
        return f"Loan principal: {self.loan_principal}"
    #
    # def calculate_monthly_payment_int(self):
    #     """
    #     Helper method for calculating monthly payment.
    #     :return: Return int indicating monthly payment. It does not take into consideration last month payment,
    #     which may differ from the basic installment. If you want to calculate exact payment for every month, use
    #     calculate_monthly_payment_tuple method.
    #     :rtype: int
    #     """
    #     return ceil(self.loan_principal / self.num_of_months)
    #
    # def calculate_monthly_payment_tuple(self):
    #     """
    #     Helper method for calculating monthly payment.
    #     :return: Return tuple containing monthly payments. First value is ceil of monthly payment, second value is
    #     the last loan installment. If last loan installment is the same as the monthly payment, second value in the
    #     tuple will be 0
    #     :rtype: tuple
    #     """
    #     base_monthly_payment = ceil(self.loan_principal / self.num_of_months)
    #     last_payment = self.loan_principal - ((self.num_of_months - 1) * self.monthly_payment)
    #     return (base_monthly_payment, 0 if last_payment == base_monthly_payment else last_payment)
    #
    # def monthly_payment_print(self):
    #     """Helper function for printing monthly payment"""
    #     monthly_payment_tuple = self.calculate_monthly_payment_tuple()
    #     print(f'Your monthly payment = {monthly_payment_tuple[0]}' if monthly_payment_tuple[1] == 0 else \
    #         f"Your monthly payment = {monthly_payment_tuple[0]} and the last payment = {monthly_payment_tuple[1]}.")


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

    # def get_curret_principal(self):
    #     """
    #     Method for checking, if the loan was repaid.
    #     :return: String saying that credit has been repaid or int indicating how much more money is needed to repay it
    #     :rtype: str/int
    #     """
    #     if self.loan_principal - self.total_repaid() <= 0:
    #         return "The loan has been repaid!"
    #     else:
    #         return self.loan_principal - self.total_repaid()

    def calculate_annuity_payment(self):
        """
        Method with formula for calculating annuity payment. Right now works as a setter.
        """
        self.annuity_monthly_payment = ceil(self.loan_principal * \
                                       ((self.loan_interest * pow(1 + self.loan_interest, self.num_of_payments)) /
                                        (pow(1 + self.loan_interest, self.num_of_payments) - 1)))

    def annuity_payment_print(self):
        """Helper method for printing annuity payment."""
        print(f"Your monthly payment = {self.annuity_monthly_payment}!")

    def calculate_loan_principal(self):
        """
        Method with formula for calculating loan principal. Right now works as a setter.
        """
        self.loan_principal = round((self.annuity_monthly_payment) / \
                              ((self.loan_interest * pow(1 + self.loan_interest, self.num_of_payments)) /
                               (pow(1 + self.loan_interest, self.num_of_payments) - 1)))

    def loan_principal_print(self):
        """Helper method for printing loan principal."""
        print(f"Your loan principal = {self.loan_principal}!")

    def calculate_loan_interest(self):
        """
        Method with formula for calculating loan interest for 12 months period. Right now works as a setter.
        # :return: Float number with % value converted to float value having regard to 12 moths period.
        # :rtype: float
        """
        self.loan_interest = self.loan_interest / (12 * 100) # (loan interest in %) / (12 months * 100%)

    def loan_interest_print(self):
        """Helper method for printing loan interest. Currently it doesnt need to be implemented"""
        print(self.loan_interest)

    def calculate_num_of_monthly_payments(self):
        """
        Method with formula for calculating number of months. Right now works as a setter.
        # :return: Number of months needed to repay loan - ceil of the number
        # :rtype: int
        """
        self.num_of_payments = ceil(log((self.annuity_monthly_payment /
                                         (self.annuity_monthly_payment - self.loan_interest * self.loan_principal)),
                                        1 + self.loan_interest))  # base

    def num_of_months_print(self):
        """Helper method for printing number of months in adequate form.
        :Example:
        1 = 1 month,
        3 = 3 months,
        12 = 1 year,
        13 = 1 year and 1 month,
        14 = 1 year and 2 months,
        25 = 2 years and 1 month,
        26 = 2 years and 2 months"""
        years_and_months = divmod(self.num_of_payments, 12)
        done_string = "It will take "
        if years_and_months[0] > 0:  # check how many years, if 0 skip
            done_string += "1 year" if years_and_months[0] == 1 else f"{years_and_months[0]} years"
        if years_and_months[1] > 0:  # check how many months, if 0 skip
            if years_and_months[0] > 0:  # check if at least one year
                done_string += ' and '
            done_string += "1 month" if years_and_months[1] == 1 else f"{years_and_months[1]} months"
        done_string += ' to repay this loan!'
        print(done_string)

def input_handler():
    """Input handler for showing available options ans using respective constructor."""

    print(f"What do you want to calculate?\n"
          f"type \"n\" for number of monthly payments,\n"
          f"type \"a\" for annuity monthly payment amount,\n"
          f"type \"p\" for loan principal:")

    user_choice = input()
    if user_choice == 'n':  # calculate number of monthly payments
        user_loan_principal = float(input("Enter the loan principal:"))
        user_monthly_payment = float(input("Enter the monthly payment:"))
        user_loan_interest = float(input("Enter the loan interest:"))
        loan = LoanCalculator(loan_principal=user_loan_principal,
                              annuity_monthly_payment=user_monthly_payment,
                              loan_interest=user_loan_interest)
        loan.num_of_months_print()

    elif user_choice == 'a':  # calculate annuity monthly payment amount
        user_loan_principal = float(input("Enter the loan principal:"))
        user_num_of_periods = float(input("Enter the number of periods:"))
        user_loan_interest = float(input("Enter the loan interest:"))
        loan = LoanCalculator(loan_principal=user_loan_principal,
                              num_of_payments=user_num_of_periods,
                              loan_interest=user_loan_interest)
        loan.annuity_payment_print()

    elif user_choice == 'p':  # calculate loan principal
        user_annuity_payment = float(input("Enter the annuity payment:"))
        user_num_of_periods = float(input("Enter the number of periods:"))
        user_loan_interest = float(input("Enter the loan interest:"))
        loan = LoanCalculator(annuity_monthly_payment=user_annuity_payment,
                              num_of_payments=user_num_of_periods,
                              loan_interest=user_loan_interest)
        loan.loan_principal_print()
    else:
        pass

input_handler()
