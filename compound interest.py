# Compound Interest Calculator

def compound_interest(principal, rate, time, compounding_periods):
    """
    Calculates the final amount after compound interest is applied.

    Args:
        principal (float): The initial amount of money.
        rate (float): The annual interest rate as a decimal.
        time (int): The number of years the money is invested.
        compounding_periods (int): The number of times the interest is compounded per year.

    Returns:
        float: The final amount after compound interest is applied.
    """
    amount = principal * (1 + (rate / compounding_periods)) ** (compounding_periods * time)
    return amount

# Example usage
principal = float(input("Enter the initial principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
time = int(input("Enter the number of years: "))
compounding_periods = int(input("Enter the number of compounding periods per year: "))

final_amount = compound_interest(principal, rate, time, compounding_periods)
print(f"The final amount after compound interest is: ${final_amount:.2f}")  