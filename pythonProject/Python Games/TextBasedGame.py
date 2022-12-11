# Function to display instructions at the beginning of the game
def instructions():
    print('Welcome to the game!')
    print('Your task is to collect all of the vital information located within this facility.')
    print("Make sure you don't get caught by the security guard before you have everything.")
    print('Direction inputs are: North, South, East, and West')
    print("To collect the item in the room, type: 'Collect Item'")
    print('Good luck!')


# Function used to collect the items
def get_item(room, collect, rooms, inventory):
    if collect == rooms[room]['item'] and rooms[room]['item'] not in inventory:     # Collects item if not in inventory
        inventory.append(collect)
        print('You pick up the {}'.format(collect))
        del rooms[room]['item']                             # Deletes item from room once it's in the inventory
    else:
        print('You do not see the {}'.format(collect))


# Function for when the player enters the room with the villain/boss
def boss_room(inventory):
    if len(inventory) == 6:         # Win Sequence
        print('You have encounter the security guard!')
        print('You eliminate him and exit the facility.')
        print('Good work. Report to the safe house for mission debrief.')
        print('You won! Thanks for Playing!')
    elif len(inventory) != 6:       # Loose Sequence
        print('You have encounter the security guard!')
        print('You forgot to get all of the items needed for mission complete!')
        print('The security guard stops you and calls in reinforcements.')
        print('You lost! Thanks for Playing!')


# Main Gameplay Loop
def main():
    # Dictionary with each room. Each room has a dictionary with movement direction and item.
    rooms = {
        'Loading Dock': {'east': 'Manufacturing Floor'},
        'Manufacturing Floor': {'west': 'Loading Dock', 'north': 'Cafeteria', 'east': 'HR Office', 'south': 'QA Office',
                                'item': 'Kill Switch'},
        'Cafeteria': {'south': 'Manufacturing Floor', 'east': 'Break Room', 'item': 'Prototype'},
        'Break Room': {'west': 'Cafeteria', 'item': 'Security Guard'},
        'HR Office': {'west': 'Manufacturing Floor', 'north': 'Server Room', 'item': 'Employee Info'},
        'Server Room': {'south': 'HR Office', 'item': 'Manufacturing Data'},
        'QA Office': {'north': 'Manufacturing Floor', 'east': 'R&D Office', 'item': 'Testing Data'},
        'R&D Office': {'west': 'QA Office', 'item': 'Blueprints'}
    }

    instructions()      # Print Instructions

    # Variables for the location player is at, current inventory, and the users input
    location = 'Loading Dock'
    inventory = []
    user_input = ""

    # Loop used to play game. Game is stopped is 'exit' is typed.
    while user_input != 'exit':
        print('\nYou are in the {}'.format(location))       # Prints your current location
        if 'item' not in rooms[location].keys():            # Checks if item is no longer within the room
            print('There is no item at this location')
        # Sees if item is in room, if so, prints that you see the corresponding item
        elif location != 'Loading Dock' or 'Break Room' and 'item' in rooms[location].keys():
            print('You see the {}'.format(rooms[location]['item']))
        print('Your current inventory is: {}'.format(inventory))        # Prints your current inventory
        print('')
        print('----------------------')

        # If the location is the break room, this triggers the boss_room function
        if location == 'Break Room':
            print('')
            boss_room(inventory)
            break       # Ends game after boss_room function is ran

        # Used to get the users move that they want to perform
        user_input = input('Enter your move: ').strip().lower()
        print('----------------------')

        # Gameplay movement statements. This moves player to different rooms.
        if user_input == 'north' or user_input == 'south' or user_input == 'east' or user_input == 'west':
            if user_input in rooms[location]:
                location = rooms[location][user_input]
            else:
                print('Invalid Direction. Try again.')      # If user doesn't input cardinal direction, error statement
        elif user_input == 'Collect Item'.strip().lower():      # 'Collect Item' needs to be typed to collect item
            get_item(location, rooms[location]['item'], rooms, inventory)   # Uses get_item function to collect items
        else:
            # If input is anything other than designated in directions, error statement
            print('Invalid Input. Try again.')


main()      # Start Game Trigger
