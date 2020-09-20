from math import ceil

print(type(ceil(10 / 3)))
# #TODO konstruktor działa, ale potem musisz wyswietlic odpowiedni tekst
# @classmethod
# def from_input(cls, principal, option):
#     """
#     Handler function for taking user input using alternative constructor.
#     :param principal: Int containing value of loan principal
#     :param option: option chosen by user when initializing an instance.
#     :type principal: int
#     :type option: str
#     """
#
#     if option == 'm':  # user choice to provide monthly payment
#         print('Enter the monthly payment:')
#         user_monthly_payment = int(input())
#         return cls(principal, monthly_payment=user_monthly_payment)
#
#     elif option == 'p':  # user choice to provide number of monthly payments
#         print('Enter the number of months:')
#         user_num_of_months = int(input())
#         return cls(principal, num_of_months=user_num_of_months)
#     else:
#         pass

# @classmethod
# def from_monthly_payment_value(cls, principal, monthly_payment_value):
#     """
#     Alternative constructor for making LoanCalculator instance using principal and monthly payment value.
#     :param principal: Int containing value of loan principal
#     :param monthly_payment_value: Int indicating value of monthly payment (loan installment)
#     :type principal: int
#     :type monthly_payment_value: int
#     """
#     return cls(principal, monthly_payment=monthly_payment_value)
#
# @classmethod
# def from_num_of_monthly_payments(cls, principal, num_of_months):
#     """
#     Alternative constructor for making LoanCalculator instance using principal and number of monthly payments.
#     :param principal: Int containing value of loan principal
#     :param num_of_months: Number of months in which user wants to repay the loan
#     :type principal: int
#     :type num_of_months: int
#     """
#     return cls(principal, num_of_months=num_of_months)