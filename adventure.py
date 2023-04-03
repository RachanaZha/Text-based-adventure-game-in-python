import json
import sys

#input map file name
if len(sys.argv) < 2:
    print("Please enter a Map File name for the game while entering run command.")
    sys.exit(1)

# Store the filename in a variable
mapfile = sys.argv[1]

# Load mapfile
with open(mapfile, "r") as f:
    rooms = {room["name"]: room for room in json.load(f)}

# Validate mapfile
for room_name,room_data in rooms.items():
    if "exits" not in room_data:
        raise ValueError(f"no exits defined for {room_name}")

# Start game in room "The entrance"
current_room = list(rooms.values())[0]

# Print room description
print("> " + current_room["name"])
print()
print(current_room["desc"])
print()
print("Exits: " + " ".join(current_room["exits"].keys()))
print()

if "items" in room_data:
    if len(current_room["items"]) > 0 :
        print("Items: " + " ".join(current_room["items"]))
        print()

# Set up game state
game_won = False
inventory = []
unlock_items=["cage"]

# Creating a dictionary containing a list of valid verbs along with their respective descriptions or meanings.
verbs = {
    'help': 'Print all possible verbs.',
    'look': 'Print a description of the current room.',
    'go': 'Move to another room in the specified direction.',
    'get': 'Pick up an item in the current room and add it to your inventory.',
    'drop': 'Drop an item in the current room',
    'inventory': 'Display the items currently in your inventory.',
    'quit': 'Exit the game.',
    'unlock': 'Unlock a door or a cage'
}

# Get player input
while True:
    try :
        command = input("What would you like to do? ")
        command=command.lower()
  
    except EOFError:
        print("Use 'quit' to exit.")
    
    # Handle movement commands
    if command.startswith("go"):
        
        valid_exit=False

        if not command[3:] :
            print("Sorry, you need to 'go' somewhere.")
            continue

        noun = command.split(" ", 1)[1]

        if(noun.strip()==""):
            print("Sorry, you need to 'go' somewhere.")
            continue
        
        #TODO
        if noun in current_room["exits"].keys():
            valid_exit=True

        if valid_exit==False:
            print()
            print(f"There's no way to go {noun}.")
            print()
            continue

        next_room_name = current_room["exits"][noun]

        current_room = rooms[next_room_name]
        
        print("> " + current_room["name"])
        print()

        print(current_room["desc"])
        print()

        print("Exits: " + " ".join(current_room["exits"].keys()))
        print()
        
        if "items" in room_data:
            print("Items: " + " ".join(current_room["items"]))

        print()
            

    #Handling the look command
    elif command.startswith("look"):
        print("> " + current_room["name"])
        print()
        print(current_room["desc"])
        print()
        print("Exits: " + " ".join(current_room["exits"].keys()))
        print()
        if "items" in room_data:
            print("Items: " + " ".join(current_room["items"]))
        print()


    # Handle item pickup commands
    elif command.startswith("get"):
        
        if not command[4:] :
            print("Sorry, you need to 'get' something.")
            continue

        item_name = command.split(" ", 1)[1]

        if(item_name.strip()==""):
            print("Sorry, you need to 'get' something.")
            continue

        if item_name in current_room["items"]:
            current_room["items"].remove(item_name)
            inventory.append(item_name)
            print(f"You pick up the {item_name}.")
            print()
        else:
            print(f"There is no {item_name} anywhere.")
            print()

    elif command.startswith("drop"):

        if not command[5:] :
            print("Sorry, you need to 'drop' something.")
            continue
        
        item_name = command.split(" ", 1)[1]

        if(item_name.strip()==""):
            print("Sorry, you need to 'drop' something.")
            continue

        if item_name in inventory:
            inventory.remove(item_name)
            current_room["items"].append(item_name)
            print(f"Dropped {item_name}.")
        else:
            print("Item not found in inventory.")
    
    # Handle inventory display command
    elif command == "inventory":
        print("Inventory:")
        for item in inventory:
            print(item)
        if not inventory:
            print("You're not carrying anything")
            
    # Handle quit command
    elif command == "quit":
        print("Goodbye!")
        break

    elif command == "help":
        print("You can run the following commands:")
        for key in verbs.keys():
            print(key)
        
    elif command.startswith("unlock"):
        if not command[6:] :
            print("Sorry, you need to 'unlock' something.")
            continue
        
        unlock_item = command.split(" ", 1)[1]

        if(unlock_item.strip()==""):
            print("Sorry, you need to 'unlock' something.")
            continue

        if unlock_item in unlock_items:
            if current_room["name"]=="Princess's room" and "key" in inventory :
                game_won = True
            elif current_room["name"]!= "Princess's room" :
                print("There is nothing to be unlocked here")
            elif "key" not in inventory:
                print("You need to have the key to unlock")
        else :
            print("This item cannot be unlocked")
    
    # Handle invalid command
    else:
        print("Invalid command.")
    
    #winning condition
    if game_won :
        print("Congratulations! You have rescued the princess and won the game !")
        break
        

