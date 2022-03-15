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
# Functions for use in the main split_the_bill() function

# Function to calculate the food cost after tax
def calculate_tax(cost_before_tax):
    # Add 10% sales tax to the food cost rounded to 2 decimal places
    food_cost_after_tax = round(cost_before_tax * 1.1, 2)
    return food_cost_after_tax

# Calculate the tip amount
def calculate_tip(cost, tip_percentage):
    tip_amount = cost * (tip_percentage / 100)
    return tip_amount

# Get the cost of the food from the user and convert to float to 2 decimal places
def get_food_cost():
    food_cost = float(input("How much does the food cost? "))
    return food_cost

# Get the number of people splitting the bill from the user and convert to int
def get_number_of_people():
    num_people = int(input("How many people are splitting the bill? "))
    return num_people

# Get the tip percentage from the user and convert to int
def get_tip_percentage():
    tip_percentage = int(input("What percentage would you like to tip? "))
    return tip_percentage

# Calculate the total bill for each person and round to 2 decimal places
def get_cost_per_person(cost, num_people):
    cost_per_person = round(cost / num_people, 2)
    return cost_per_person

# Function to calculate the total bill for each person and the tip amount
def split_the_bill():
    # Get the cost of the food from the user and convert to float to 2 decimal places
    food_cost = get_food_cost()
    
    # Add tax to the food cost
    food_cost_after_tax = calculate_tax(food_cost)
    
    # Get the number of people splitting the bill from the user and convert to int
    num_people = get_number_of_people()
    
    # Get the percentage of the tip from the user and convert to int
    tip_percentage = int(input("What percentage would you like to tip? "))
    
    # Calculate the tip amount
    tip_amount = calculate_tip(food_cost, tip_percentage)
    
    # Add the tip amount to the food cost after tax to get the total bill to be split
    total_food_cost = food_cost_after_tax + tip_amount
    
    # Calculate the total bill for each person and round to 2 decimal places
    cost_per_person = get_cost_per_person(total_food_cost, num_people)
    
    # Print the total bill in the format: `Total bill: $6,100.00`
    print(f"Total bill: ${total_food_cost:.2f}")
    # Print the tip amount in the format: `Each person should pay $6.96`
    print(f"Each person should pay ${cost_per_person:.2f}")

# A loop to run program multiple times if the user wants to
def split_the_bill_loop():
    while True:
        split_the_bill()
        # Ask the user if they want to continue
        run_again = input("Would you like to run the program again? (y for yes, n for no:) ")
        if run_again == "n" or run_again == "N":
            break

# Run the program when the script is run
split_the_bill_loop()