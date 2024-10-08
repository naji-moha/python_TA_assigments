import random

# Create a dictionary to represent zones and items in each zone
zones = {
    'Candy Land': ['power candy', 'battery boost', 'short circuit'],
    'Robotropolis': ['battery boost', 'short circuit', 'power candy'],
    'Circuit City': ['short circuit', 'battery boost', 'power candy'],
    'Gadget Galaxy': ['power candy', 'short circuit'],
}

# Initial robot status
robot_inventory = []  # List to store collected items
battery_level = 10  # Battery starts at 10 units
total_power_candies = 4  # Total power candies to collect
power_candies_collected = 0  # Counter for collected power candies

# Function to move the robot to a new zone and search for items
def move_to_zone(zone):
    global battery_level, power_candies_collected
    if battery_level <= 0:
        print("What are you waiting? Battery dead. Game over!")
        return False
    
    print(f"\nExploring {zone}...")

    # Randomly select an item from the zone
    item = random.choice(zones[zone])
    print(f"Item found: {item}")
    
    if item == 'power candy':
        collect_item(item)
    elif item == 'short circuit':
        battery_level -= 3
        print("Oops! Short circuit! Battery drained by 3 units.")
    elif item == 'battery boost':
        battery_level += 2
        print("Yaay battery boost found! Battery recharged by 2 units.")
    
    battery_level -= 1  # Decrease battery for moving to a zone
    print(f"Battery level: {battery_level}")
    
    if power_candies_collected == total_power_candies:
        print("All power candies collected! You win Beyonce!")
        return False
    
    if battery_level <= 0:
        print("Battery dead. Game over! Don't come back")
        return False
    
    return True

# Function to collect a power candy
def collect_item(item):
    global power_candies_collected
    if item == 'power candy':
        robot_inventory.append(item)
        power_candies_collected += 1
        print(f"Power candy collected! Total power candies: {power_candies_collected}")

# Function to display the robot's inventory

def display_inventory():
    print(f"Inventory: {robot_inventory}")
    print(f"Power candies collected: {power_candies_collected}/{total_power_candies}")

# Main game loop
def play_game():
    global battery_level
    print("Welcome to the Robot Adventure Gameee!")
    print(f"Collect {total_power_candies} power candies before your battery runs out.")
    
    while True:
        display_inventory()
        print("\nZones available to explore: Candy Land, Robotropolis, Circuit City, Gadget Galaxy")
        zone = input("Choose a zone to explore or type 'quit' to end the game: ").capitalize()
        
        if zone.lower() == 'quit ducks':
            print("Exiting game. Thanks for playing!")
            break
        elif zone in zones:
            if not move_to_zone(zone):
                break
        else:
            print("What are you doing here? Please choose a valid zone.")

# Start the game
play_game()
