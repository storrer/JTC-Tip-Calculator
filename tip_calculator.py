"""
    This script takes a user's input at the command line for:
    - Cost of the food
    - Number of people splitting the bill
    - Percentage of the tip

    It then calculates the total bill and the tip amount.
    Inputs:
    * Food costs $5000
    * 876 people paying
    * 12% tip

    Expected output:
    * `Total bill: $6,100.00`
    * `Each person should pay $6.96`

"""
# Function to calculate the total bill for each person and the tip amount
def calculate_tip():
    # Get the cost of the food from the user and convert to float
    food_cost = float(input("How much was the food? ")) 
    # Get the number of people splitting the bill from the user and convert to int
    num_people = int(input("How many people are splitting the bill? ")) 
    # Get the percentage of the tip from the user and convert to float
    tip_percentage = float(input("What percentage would you like to tip? "))
    # Calculate the tip amount
    tip_amount = food_cost * (tip_percentage / 100)
    total_food_cost = food_cost + tip_amount
    cost_per_person = total_food_cost / num_people
    # Print the total bill in the format: `Total bill: $6,100.00`
    print(f"Total bill: ${total_food_cost:.2f}")
    # Print the tip amount in the format: `Each person should pay $6.96`
    print(f"Each person should pay ${cost_per_person:.2f}")
# Start the program
calculate_tip()