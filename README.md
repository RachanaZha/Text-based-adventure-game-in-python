Rachana Rizhkant Zha [rzha@stevens.edu](mailto:rzha@stevens.edu)



# Github repo URL



#Game Description

Provided the map which is used is the map provided by me, then the game is about saving the princess. You have to find and enter the room where the princess is locked in a cage and use a key to unlovk the cage and thats how you win the game!

# Hours spent

the Number of hours spent is 40+ hours of coding , testing , debugging an fixing the issues.




# a description of how you tested your code

To begin with, I designed the code to take a .map file as an input argument. This file contained information about the game's layout, including the number of rooms, their descriptions, and the items within them.

Once the code was written, I started testing it by providing a sample .map file as input that contained four rooms, each with different inventories. I then ran the code and tried to navigate through each room using the available verbs, as mentioned earlier.

For the "go" verb, I attempted to move in different directions, such as north, south, east, and west, and verified that the code correctly updated the current room and provided the corresponding description.

Similarly, I tested the "get" and "drop" verbs by picking up and dropping items in different rooms, respectively. I also tested the "unlock" verb to ensure that the player could unlock doors or cages if they had the necessary key.

In addition, I tested the "inventory" verb to ensure that the player's inventory was correctly updated with the items they picked up, and the "look" verb to ensure that the code provided the appropriate room description.

Throughout the testing process, I kept a log of any bugs or errors I encountered, such as the code failing to update the player's inventory after they picked up an item or incorrectly providing the room description when using the "look" verb.

Once I identified these issues, I added new test cases to the code to ensure that they were resolved. For example, I added a test case that verified that the player's inventory was updated correctly after picking up an item, and another that verified that the correct room description was provided when using the "look" verb.

Overall, this thorough testing process helped to ensure that the code was functional and provided the expected output in various scenarios. It also helped to identify and resolve any bugs or errors, ensuring that the code was reliable and ready for use.





#Any bugs or issues you could not resolve

There are no unresolved bugs and issues . I tried to resolve as many issues as possible and make the code error free. As of now i havent encountered any known errors or bugs.





#An example of a difficult issue or bug and how you resolved

One major issue i faced was related to a verb that requires something to be written after it. I had not implemented a check for blank input, so if a player entered the verb but did not specify a direction, the code would still execute the verb and move the player in the default direction. To resolve this issue, I took the input and stored each word in a list, and checked if the second word in the list was blank. However, this caused an index error when the list only contained the verb in the 0th index. To fix this, I checked the entire command as a string and made sure that there was something written after the verb. If there was only blank spaces given, we gave the respective error message.





a list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate them (i.e., what are the new verbs/features, how do you exercise them, where are they in the map)

Drop Verb: The drop verb is the opposite of get. It allows the player to take something from their inventory and put it down in the current room. The player can only drop items that they already have in their inventory. The drop verb is exercised by typing "drop [object]" in the command line. This extension can be found in the adeventure.py file.

Help Verb: In complicated text adventures, it can be hard to keep track of what the verbs are. Having a help verb makes things easier for players. This extension adds a help verb that tells players what the valid verbs are. The verb is exercised by typing "help" in the command line. The help verb also indicates which verbs expect a target of some kind by adding "..." after them. This extension can be found in the adeventure.py file.

Locked Doors: This extension adds locked doors to the game. The player must find a key in the current room or another room to unlock the door and proceed. The locked doors are represented as special objects in the game, and the keys are also represented as objects that can be picked up and used. The locked cage extension is exercised by typing "unlock [object]" in the command line. This extension can be found in the adeventure.py file


#How to play the game 
Provided that the map is used is the one submitted by me-The game is all about saving the princess and freeing her from the locked cage. To achieve this, you need to navigate through different rooms and collect the key to unlock the cage. The map consists of several rooms, including the entrance room, armory, tower, library, and princess room. Each room has certain exits and inventories that you can explore.

Please find below a pictorial representation of the map:

![project](https://user-images.githubusercontent.com/124010659/229400022-bea170f4-5101-48ae-bdaf-00fd88578e42.jpg)

Your objective is to find the key and make your way to the princess room to unlock the cage and rescue the princess. The game is won when you successfully unlock the cage and rescue the princess.

To test the winning condition, you can follow this winning path on the map provided:

From the entrance room, go south to reach the tower.
From the tower, go south again to reach the armory.
From the armory, go east to reach the library.
Once you reach the library, pick up the key.
From the library, go north to reach the princess room.
Use the "unlock cage" command to unlock the cage and save the princess.
Have fun playing the game and good luck on your quest to save the princess!


