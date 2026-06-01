# Defined a function that handles all the inputs
# It checks if whether your inputs are positive
# and whether if your inputs are numbers, in this case, floats
def get_positive_float(prompt, error_msg):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print(error_msg)
        except ValueError:
            print("Invalid choice or format.")
# A nice title. Cuz why not
print("------COMPOUND INTEREST CALCULATOR------")
# All them variables and inputs
initialAmount = get_positive_float("Enter the Principal amount: $", "Please enter a valid amount.")
interestRate = get_positive_float("Enter the interest rate: ", "Please enter a valid amount.")
time = get_positive_float("Enter the investment period (in year): ", "Please enter a valid amount.")
# the calculations
finalAmount = initialAmount * (1 + (interestRate / 100)) ** time
profit = finalAmount - initialAmount

print(f" in {time} years time,\n with {interestRate}% interest rate,\n You will have a total of ${finalAmount:,.2f}.\n And you will profit ${profit:,.2f}.")
