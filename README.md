# Makeplace-Differenciator
Finds the differences in and old and new layout of Makeplace.list.txt

This script you help you make a purchase list from the differences in an old build and a new build using Makeplace.

When you save a build, 2 files are generated, a .json and a .list.txt. The .json is used by the plugin while the list.txt is meant as a list of all items and dyes used in the build.

However i encounted a problem, this script is here to fix that.

Many people will build in stages or update their apartments and houses by placing more items into it as they get more items or more ideas, or maybe they decorate one floor at a time.

The problem comes when the new build will tell you that the items from the old will need to be purchased, let me make an example.

For the sake of simplicity, lets say you have placed 4 partitions and 2 doors. This is your Old Build.

Now lets say you want to update or flesh out this build, so you import what you have into Makeplace and you continue, lets say you add two partitions and one door as well as 3 plants. You save that and open the list to see what you need to buy.

The problem comes when the list says "6 Partitions, 3 Doors, 3 plants". You already have 4 partitions placed and 2 doors, but your new list will tell you that you need 6 partitions instead.

What this script does is that it compares the old to the new, accounts for differences and generates a list of all the things you need to buy, a list this script will generate will in this case be "2 partitions, 1 door, 3 plants". The difference between new and old.

Here is how you make it work.




Navigate to your .list.txt file in Makeplace/Saves
Copy everything between 
     Furniture     
=====================

And

        Dyes        
=====================

Your text files should look like this with no empty linebreaks:

Allagan Commerce Node Permit: 1
Allagan Resupply Node Permit: 1
Alpine Breakfast: 2
Apothecary's Workbench: 1

Neither "===" or "Furniture" at the top should be included in the file.

The list.txt of your old build that you have currently and want to add to should be copied into "Old List.txt"
The list.txt of your new build that you made in Makeplace and want to import should go into "New List.txt"

Run the differencer.py script with either IDLE, VSCode or any other compiler of your choice.

If the program is successful, "Purchase List.txt" should have all the things you need to buy. 

"Debug.txt" is included for troubleshooting purposes.
