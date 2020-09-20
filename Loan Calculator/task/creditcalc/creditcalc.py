loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

class LoanCalculator:
    """
    A class representing Loan Calculator

    :param principal: Int containing value of loan principal
    :type principal: int
    :param monthly_repaids: Dictionary containing months as a keys, and repaid amounts as values
    :type monthly_repaids: dict
    """

    def __init__(self, principal):
        """Initializer"""
        self.principal = principal
        self.monthly_repaids = {}

    def __repr__(self):
        return f"Credit principal: {self.principal} with {len(self.monthly_repaids)} months repaid"

    def __str__(self):
        return f"Loan principal: {self.principal}"


    @property
    def months(self):
        """
        Getter for monthly_repaids dictionary
        :return: String showing all months and corresponding repaid values
        :rtype: str
        """
        result = ''
        for month in self.monthly_repaids:
            result += f"Month {month}: repaid {self.monthly_repaids[month]}" + "\n"
        return result.rstrip("\n")  # strip last \n

    @months.setter
    def months(self, months_dict):
        """
        Setter for adding months with repaid values to instance monthly_repaids variable
        :param months_dict: Dictionary with months and values. Same keys are overwritten
        :type months_dict: dict
        """
        self.monthly_repaids = {**self.monthly_repaids, **months_dict}

    def total_repaid(self):
        """
        Method for total repaid
        :return: Sum of all repaid amounts (all values in monthly_repaids dictionary)
        :rtype: int
        """
        return sum(self.monthly_repaids.values())

    def get_curret_principal(self):
        """
        Method for checking, if loan was repaid.
        :return: String saying that credit has been repaid or int indicating how much more money is needed to repay it
        :rtype: str/int
        """
        if self.principal - self.total_repaid() <= 0:
            return "The loan has been repaid!"
        else:
            return self.principal - self.total_repaid()

loan = LoanCalculator(1000)
loan.months = {1: 250, 2: 250, 3: 500}
print(loan, loan.months, loan.get_curret_principal(), sep='\n')