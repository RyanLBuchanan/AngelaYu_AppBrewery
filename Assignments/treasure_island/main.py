print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Velcome to my home . . . ah, ah, aaah!!!\nYour mission, should you choose to accept it,\nis to find the lost souls I have placed inside the Chest of Spiritual Anguish!\n")

first_decision = input("Before you lies path.\nShould you choose to take the road less-traveled to the left or the well-worn path to the right?\nCome now, what is it, then?\nLeft or right, hmmmm? ").lower()

if first_decision == "right":
    print("\nBwaaah ha, ha, ha!\nYour road, and mortal life, ends here Foolish One!\nGAME OVER!!!")
    exit()
else:
    print("\n\nYou have chosen . . . wisely.\nA bead of sweat slowly rolls down your spine\nand sudden chills take over your body.\n\nYour next decision lies ahead on this path through the darkening night.\nAfter not a little nor comforting stroll, you have come to murky moat.\n\nThere is a ferry coming.\nIt moves slowly and eradically.\nA dark, hooded figure leaning on a treacherous-looking scythe guides the skiff.\n")

second_decision = input("How are your water-wings, weary Traveller?\nWill you avoid certain Death?\nYou must now swim across the moat or wait for the chthonic Boatman.\n\nWill you swim or wait? ").lower()

if second_decision == "swim":
    print("\n\nAnd now you DIE!\nA shrieking eel overtakes you as you begin your swim.\nIt mercilessly bites you in half.\nYour halved remains sink into the depths, leaving a streamer of blood.\nGAME OVER!!!")
    exit()
else:
    print("\n\nAnd . . .\nYour life continues, albeit not without culminating dread.\nYou quickly, but politely leave the Boatman, depositing a gold coin in a tarnished brass pot at the foot to his ragged robe.\nYou flee off into the forest on a small game trail that is the only passable way.\n\nThrough the mist darkly, something is materializing ahead.\nYou have arrived at the crumbling ruins of an ancient temple . . . or tomb, perhaps.\n\nYou trudge forward and reach the base of an enormous hexagonal, granite tower.\nWithin each of the three sides you can see is a massive wood-paneled portal.\nWeather-worn oak doors with great, iron knockers.\n\nSuddenly, a skeletal Wraith materializes not one meter from your nose.\n\"What are you here for?!\" the frightening figure booms, in an underworldly voice that seems to come from all around you.\nYou stumble back but keep your resolve.\n\nYou nod toward the door directly in front of you.\n\"Ah, you wish to pass . . . to move through my Temple and partake of the Chest of Anguished Souls, in which lies unfathomable weath?\" the Wraith smirks.\nAgain, you solemnly nod, inwardly steeling will for the inevitable decision you know is coming.\n\n\"You must choose one of the doors before you, little One!\" the Wraith thunders.\nYou glance at each of the three doors.\nThey have a slight discoloration from the native oak.\n\nOn the left is a red door.\nIn the middle is a yellow door.\nAnd on the right is a blue door.\n\n\"Go on then,\" says the impatient Spirit, \"Chooses a door!\"\n")

third_decision = input("\"Red . . . yellow . . . or blue, Traveller?\" presents the Wraith.\n\nYou choose . . . ").lower()

if third_decision == "yellow":
    print("\nRight then.  YOU WIN!!!  Off with ya.")
    exit()
elif third_decision == "red":
    print("\nEpic death ensues!  Why on earth would anyone choose RED, when death is on the line?!\nHa hahahahahahahah!?!\nGAME OVER!!!")
    exit()
else:
    print("\nYou tumble through eternity to a doom scarier than all dooms you have ever had!\nYes, it was actually yellow, you cowardly animal!\nGAME OVER!!!")
    exit()