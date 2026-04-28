# Adding Fuel Calculator

def calculate_fuel_cost():
    miles = float(input("Enter the total trip miles: "))
    mpg = float(input("Enter your vehicle's miles per gallon (MPG): "))
    gas_price = float(input("Enter the current gas price per gallon: "))

    gallons_needed = miles / mpg
    fuel_cost = gallons_needed * gas_price

    print(f"Estimated fuel cost for your trip: ${fuel_cost:.2f}")
    return fuel_cost

# Lodging Calculator

def calculate_lodging_cost():
    nights = int(input("Enter the number of nights you'll be staying: "))
    cost_per_night = float(input("Enter the cost per night: "))

    lodging_cost = nights * cost_per_night

    print(f"Estimated lodging cost for your trip: ${lodging_cost:.2f}")
    return lodging_cost

# Food Cost Calculator

def calculate_food_cost():
    days = int(input("Enter the number of travel days: "))
    daily_food_cost = float(input("Enter your estimated daily food cost: "))

    food_cost = days * daily_food_cost

    print(f"Estimated food cost for your trip: ${food_cost:.2f}")
    return food_cost

# Activity Cost Calculator

def calculate_activity_cost():
    activities_cost = float(input("Enter the estimated cost of activities for your trip: "))

    print(f"Estimated activity cost for your trip: ${activities_cost:.2f}")
    return activities_cost

#Split Cost Per Person Calculator

def split_cost_between_travelers(total_cost):
    travelers= int(input("Enter the number of travelers: "))

    cost_per_person = total_cost / travelers

    print(f"Cost per person for the trip: ${cost_per_person:.2f}")

# Best Route Options (Beginner Friendly, would like if this was better developed and more efficient for user)

def find_best_route():
    destination = input("Enter your trip destination: ")

    route1_name = input("Enter name of route option 1: ")
    route1_miles = float(input(f"Enter the miles for route 1: "))

    route2_name = input("Enter name of route option 2: ")
    route2_miles = float(input(f"Enter the miles for route 2: "))

    route3_name = input("Enter name of route option 3: ")
    route3_miles = float(input(f"Enter the miles for route 3: "))

    shortest_miles= min(route1_miles, route2_miles, route3_miles)

    if shortest_miles == route1_miles:
        best_route = route1_name
    elif shortest_miles == route2_miles:
        best_route = route2_name
    else:
        best_route = route3_name
    
    print(f"The best route to {destination}: {best_route} with {shortest_miles} miles.")
 

# Main Page

def main():
        while True:
            print("\nSmart Road Trip Planner Menu")
            print("1. Find the Best Route")
            print("2. Calculate Trip Costs")
            print("3. Exit")

            choice= input("Enter your choice (1-3): ")

            if choice == '1':
                find_best_route()

            elif choice == '2':
                fuel = calculate_fuel_cost()
                lodging = calculate_lodging_cost()
                food = calculate_food_cost()
                activities = calculate_activity_cost()

                total_cost = fuel + lodging + food + activities
            
                print(f"Total Estimated Trip Cost: ${total_cost:.2f}")

                split_cost_between_travelers(total_cost)
            
            elif choice == '3':
                print("Thank you for using the Smart Road Trip Planner. Safe travels!")
                break
        
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

main()