"""
    This script takes a user's input at the command line for:
    - Cost of the food
    - Number of people splitting the bill
    - Percentage of the tip

    It then calculates the total bill and the tip amount.
"""
# Function to calculate the total bill for each person and the tip amount
def calculate_tip():
    # Get the cost of the food from the user and convert to float
    total_food_cost = float(input("How much was the food? ")) 
    # Get the number of people splitting the bill from the user and convert to int
    num_people = int(input("How many people are splitting the bill? ")) 
    # Get the percentage of the tip from the user and convert to float
    tip_percentage = float(input("What percentage would you like to tip? "))
    # Use f-strings to print the tip amount, the total bill, and the total cost per person
    print(f'The tip amount is ${total_food_cost * (tip_percentage / 100)}')
    print(f'The total bill is ${total_food_cost * (1 + tip_percentage / 100)}')
    print(f'The total amount per person is ${total_food_cost / num_people}')

# Start the program
calculate_tip()