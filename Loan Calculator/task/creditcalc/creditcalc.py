from math import ceil, pow, sqrt, log
import argparse

class LoanCalculator:
    """
    A class representing Loan Calculator.

    :param loan_principal: Int or float containing value of loan principal (default None)
    :param annuity_monthly_payment: Amount of money user needs to pay monthly excluding last month (default None)
    :param num_of_payments: Number of months needed to fully repay loan (default None)
    :param loan_interest: Loan interest value. Input type is int and represents % (default None), float after function call
    :type loan_principal: int or float
    :type annuity_monthly_payment: int or float
    :type num_of_payments: int
    :type loan_interest: int or float
    """

    def __init__(self, loan_principal=None, annuity_monthly_payment=None, num_of_payments=None, loan_interest=0):
        """Initializer"""
        self.loan_principal = loan_principal
        self.annuity_monthly_payment = annuity_monthly_payment
        self.num_of_payments = num_of_payments
        self.loan_interest = loan_interest
        self.overpayment = 0

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


    def calculate_and_print_diff_payment(self):
        """Method with formula for calculating differentiated payment. Overpayment need to be calculated and printed
        here for every month it's different."""
        for month in range(1, self.num_of_payments + 1):
            current_payment = ceil((self.loan_principal / self.num_of_payments) + \
                                   self.loan_interest * \
                                      (self.loan_principal - (self.loan_principal * (month - 1) /
                                           self.num_of_payments)))
            # calculate overpayment
            self.overpayment += current_payment - ceil(self.loan_principal / self.num_of_payments)
            self.diff_payment_print_helper(month, current_payment)
        print()  # enter after overpayment

    def diff_payment_print_helper(self, month, payment):
        """
        Helper method for printing differentiated payment in adequate form. Print current month and payment amount.
        :param month: Number starting from 1 indicating number of month - provided by calculate_and_print_diff_payment
        :param payment: Int number indicating payment amount - provided by calculate_and_print_diff_payment
        :type month: int
        :type payment: int
        """
        print(f"Month {month}: payment is {payment}")

    def overpayment_print(self):
        print(f"Overpayment = {self.overpayment}")

    def calculate_annuity_overpayment(self):
        """Method for calculating annuity overpayment. Works as a setter."""
        self.overpayment = (self.annuity_monthly_payment * self.num_of_payments) - self.loan_principal


def input_handler():
    """Input handler for taking values from CLI using argparse module."""

    error_message = "Incorrect parameters"


    def annuity_payments_handler(results):
        """Handler function with all possible combinations for annuity payment  - can calculate number of monthly
        payments, annuity monthly payment amount and loan principal.
        """
        if results.num_of_months is None:  # calculate number of monthly payments
            loan = LoanCalculator(loan_principal=results.principal,
                                  annuity_monthly_payment=results.monthly_payment,
                                  loan_interest=results.interest)
            loan.num_of_months_print()
            loan.calculate_annuity_overpayment()
            loan.overpayment_print()

        elif results.principal is None:  # calculate loan principal
            loan = LoanCalculator(annuity_monthly_payment=results.monthly_payment,
                                  num_of_payments=results.num_of_months,
                                  loan_interest=results.interest)
            loan.loan_principal_print()
            loan.calculate_annuity_overpayment()
            loan.overpayment_print()

        elif results.monthly_payment is None:  # calculate annuity monthly payment amount
            loan = LoanCalculator(loan_principal=results.principal,
                                  num_of_payments=results.num_of_months,
                                  loan_interest=results.interest)
            loan.annuity_payment_print()
            loan.calculate_annuity_overpayment()
            loan.overpayment_print()


    def check_arguments(results):
        """
        Function for checking if all arguments provided by user are legit and there's enough of them.
        :param results: Object containing all arguments provided from CLI
        :type results: argparse.Namespace object
        """

        # Define some helper functions for checking
        def check_loan_type(loan_type):
            """
            Helper function for checking if loan_type is in possible options. If chosen option not in available options
            exit the program.
            :param loan_type: String containing loan type chosen by user.
            :type loan_type: str
            """
            possible_options = ['diff', 'annuity']
            if loan_type not in possible_options:
                print(error_message)
                exit()


        # START CHECKING

        # Check if loan type is available
        check_loan_type(results.loan_type)

        # check if enough arguments are provided
        if len(vars(results)) < 4:
            print(error_message)
            exit()

        # Loan interest must be provided
        if results.interest is None:
            print(error_message)
            exit()

        # combination of differentiated payment and payment value is impossible
        if (results.monthly_payment is not None) and (results.loan_type == 'diff'):
            print(error_message)
            exit()

        # checking if values are greater or equal 0
        for key, value in vars(results).items():
            if (key != 'loan_type') and (value is not None):
                if value < 0:
                    print(error_message)
                    exit()


    parser = argparse.ArgumentParser(description='Loan calculator')

    # All numeric values are converted to float at the start. All user input checking will be evaluated later.
    # All default values are set for None
    parser.add_argument('--type=', action="store", dest="loan_type", type=str, default=None)
    parser.add_argument('--payment', action="store", dest="monthly_payment", type=float, default=None)
    parser.add_argument('--principal', action="store", dest="principal", type=float, default=None)
    parser.add_argument('--periods', action="store", dest="num_of_months", type=int, default=None)
    parser.add_argument('--interest', action="store", dest="interest", type=float, default=None)

    CLI_results = parser.parse_args()

    check_arguments(CLI_results)


    # differentiated payment

    if CLI_results.loan_type == 'diff':
        loan = LoanCalculator(loan_principal=CLI_results.principal,
                              num_of_payments=CLI_results.num_of_months,
                              loan_interest=CLI_results.interest)
        loan.calculate_and_print_diff_payment()
        loan.overpayment_print()

    # annuity payment
    if CLI_results.loan_type == 'annuity':
        annuity_payments_handler(CLI_results)




    # print(f"What do you want to calculate?\n"
    #       f"type \"n\" for number of monthly payments,\n"
    #       f"type \"a\" for annuity monthly payment amount,\n"
    #       f"type \"p\" for loan principal:")
    #
    # user_choice = input()
    # if user_choice == 'n':  # calculate number of monthly payments
    #     user_loan_principal = float(input("Enter the loan principal:"))
    #     user_monthly_payment = float(input("Enter the monthly payment:"))
    #     user_loan_interest = float(input("Enter the loan interest:"))
    #     loan = LoanCalculator(loan_principal=user_loan_principal,
    #                           annuity_monthly_payment=user_monthly_payment,
    #                           loan_interest=user_loan_interest)
    #     loan.num_of_months_print()
    #
    # elif user_choice == 'a':  # calculate annuity monthly payment amount
    #     user_loan_principal = float(input("Enter the loan principal:"))
    #     user_num_of_periods = float(input("Enter the number of periods:"))
    #     user_loan_interest = float(input("Enter the loan interest:"))
    #     loan = LoanCalculator(loan_principal=user_loan_principal,
    #                           num_of_payments=user_num_of_periods,
    #                           loan_interest=user_loan_interest)
    #     loan.annuity_payment_print()
    #
    # elif user_choice == 'p':  # calculate loan principal
    #     user_annuity_payment = float(input("Enter the annuity payment:"))
    #     user_num_of_periods = float(input("Enter the number of periods:"))
    #     user_loan_interest = float(input("Enter the loan interest:"))
    #     loan = LoanCalculator(annuity_monthly_payment=user_annuity_payment,
    #                           num_of_payments=user_num_of_periods,
    #                           loan_interest=user_loan_interest)
    #     loan.loan_principal_print()
    # else:
    #     pass



input_handler()
