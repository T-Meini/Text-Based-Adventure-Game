def instructions():
    print('Welcome to the game!')
    print('Your task is to collect all of the vital information located within this facility.')
    print("Make sure you don't get caught by the security guard before you have everything.")
    print('Direction inputs are: North, South, East, and West')
    print("To collect the item in the room, type: 'Collect Item'")
    print('Good luck!')


def get_item(room, collect, rooms, inventory):
    if collect == rooms[room]['item'] and rooms[room]['item'] not in inventory:
        inventory.append(collect)
        print('You pick up the {}'.format(collect))
        del rooms[room]['item']
    elif 'item' not in rooms[room]:
        print('You do not see the {}'.format(collect))
    elif collect in inventory:
        print('You already have the {}'.format(collect))
    else:
        print('You do not see the {}'.format(collect))


def boss_room(inventory):
    if len(inventory) == 6:
        print('You have encounter the security guard!')
        print('You eliminate him and exit the facility.')
        print('Good work. Report to the safe house for mission debrief.')
        print('You won! Thanks for Playing!')
    elif len(inventory) != 6:
        print('You have encounter the security guard!')
        print('You forgot to get all of the items needed for mission complete!')
        print('The security guard stops you and calls in reinforcements.')
        print('You lost! Thanks for Playing!')


def main():
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

    instructions()

    location = 'Loading Dock'
    inventory = []
    user_input = ""

    while user_input != 'exit':
        print('\nYou are in the {}'.format(location))
        if 'item' not in rooms[location].keys():
            print('There is no item at this location')
        elif location != 'Loading Dock' or 'Break Room' and 'item' in rooms[location].keys():
            print('You see the {}'.format(rooms[location]['item']))
        print('Your current inventory is: {}'.format(inventory))
        print('')
        print('----------------------')

        if location == 'Break Room':
            print('')
            boss_room(inventory)
            break

        user_input = input('Enter your move: ').strip().lower()
        print('----------------------')

        if user_input == 'north' or user_input == 'south' or user_input == 'east' or user_input == 'west':
            if user_input in rooms[location]:
                location = rooms[location][user_input]
            else:
                print('Invalid Direction. Try again.')
        elif user_input == 'Collect Item'.strip().lower():
            get_item(location, rooms[location]['item'], rooms, inventory)
        else:
            print('Invalid Input. Try again.')


main()
