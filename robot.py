import random

# Create a dictionary to represent zones and items in each zone
zones = {
    1: {'name': 'Candy Land', 'items': ['power candy', 'battery boost', 'short circuit']},
    2: {'name': 'Robotropolis', 'items': ['battery boost', 'short circuit', 'power candy']},
    3: {'name': 'Circuit City', 'items': ['short circuit', 'battery boost', 'power candy']},
    4: {'name': 'Gadget Galaxy', 'items': ['power candy', 'short circuit']},
}

# Initial robot status
robot_inventory = []  # List to store collected items
battery_level = 10  # Battery starts at 10 units
total_power_candies = 4  # Total power candies to collect
power_candies_collected = 0  # Counter for collected power candies

# Function to move the robot to a new zone and search for items
def move_to_zone(zone_num):
    global battery_level, power_candies_collected
    if battery_level <= 0:
        print("What are you waiting for? Battery dead. Game over!")
        return False
    
    zone_name = zones[zone_num]['name']
    print(f"\nExploring {zone_name}...")

    # Randomly select an item from the zone
    item = random.choice(zones[zone_num]['items'])
    print(f"Item found: {item}")
    
    if item == 'power candy':
        collect_item(item)
    elif item == 'short circuit':
        battery_level -= 3
        print("Oops! Short circuit! Battery drained by 3 units.")
    elif item == 'battery boost':
        battery_level += 2
        print("Yay! Battery boost found! Battery recharged by 2 units.")
    
    battery_level -= 1  # Decrease battery for moving to a zone
    print(f"Battery level: {battery_level}")
    
    if power_candies_collected == total_power_candies:
        print("All power candies collected! You win Beyonce!")
        return False
    
    if battery_level <= 0:
        print("Battery dead. Game over! Don't come back.")
        return False
    
    return True

# Function to collect a power candy
def collect_item(item):
    global power_candies_collected
    if item == 'power candy':
        robot_inventory.append(item)
        power_candies_collected += 1
        print(f"Power candy collected! Total power candies: {power_candies_collected}")

# function to display the robot's inventory
def display_inventory():
    print(f"Inventory: {robot_inventory}")
    print(f"Power candies collected: {power_candies_collected}/{total_power_candies}")

# Main game loop
def play_game():
    global battery_level
    print("Welcome to the Robot Adventure Game!")
    print(f"Collect {total_power_candies} power candies before your battery runs out.")
    
    while True:
        display_inventory()
        print("\nZones available to explore:")
        for zone_num, zone_info in zones.items():
            print(f"{zone_num}. {zone_info['name']}")
        
        choice = input("Choose a zone number to explore or type '0' to quit: ")
        
        if choice == '0':
            print("Exiting game. Thanks for playing!")
            break
        elif choice.isdigit() and int(choice) in zones:
            if not move_to_zone(int(choice)):
                break
        else:
            print("What are you doing here? Please choose a valid zone.")

# Starts the game!!
play_game()
