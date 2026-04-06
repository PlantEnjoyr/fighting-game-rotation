"""
-------------------------------------------------------
Code by PlantEnjoyer
GitHub: https://github.com/PlantEnjoyr/fighting-game-rotation
Email: abimrah1234@gmail.com
-------------------------------------------------------
Theory/Abstraction: https://plant-enjoyer.neocities.org/fighting-game-rotations
"""

#Functions
def insert_name(default_name, list):
    ans = input("Enter name of " + default_name + ": ")
    if ans == "":
        list.append(default_name)
    else:
        list.append(ans)

def remove_name(list, key):
    for i in list:
        if i == key:
            list.remove(key)
    return

#Default Variables
name = []
rotation = ["no rotation selected :P"]
action = ""

# Setting Up Rotation Cycle
r_number = input("Insert # of players (3 to 8)\n")
if r_number == "3":
    insert_name("P1", name)
    insert_name("P2", name)
    insert_name("P3", name)
    rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[0]]
elif r_number == "4":
    insert_name("P1", name)
    insert_name("P2", name)
    insert_name("P3", name)
    insert_name("P4", name)
    rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[0], name[0] + " vs " + name[2], name[1] + " vs " + name[3]]
elif r_number == "5":
    insert_name("P1", name)
    insert_name("P2", name)
    insert_name("P3", name)
    insert_name("P4", name)
    insert_name("P5", name)
    rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[0], name[0] + " vs " + name[2], name[2] + " vs " + name[4], name[4] + " vs " + name[1], name[1] + " vs " + name[3], name[3] + " vs " + name[0]]
elif r_number == "6":
    insert_name("P1", name)
    insert_name("P2", name)
    insert_name("P3", name)
    insert_name("P4", name)
    insert_name("P5", name)
    insert_name("P6", name)
    rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[2], name[1] + " vs " + name[3], name[2] + " vs " + name[4], name[3] + " vs " + name[5], name[4] + " vs " + name[0], name[5] + " vs " + name[1], name[0] + " vs " + name[3], name[1] + " vs " + name[4], name[2] + " vs " + name[5]]
elif r_number == "7":
    insert_name("P1", name)
    insert_name("P2", name)
    insert_name("P3", name)
    insert_name("P4", name)
    insert_name("P5", name)
    insert_name("P6", name)
    insert_name("P7", name)
    rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[6], name[6] + " vs " + name[0], name[0] + " vs " + name[2], name[2] + " vs " + name[4], name[4] + " vs " + name[6], name[6] + " vs " + name[1], name[1] + " vs " + name[3], name[3] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[3], name[3] + " vs " + name[6], name[6] + " vs " + name[2], name[2] + " vs " + name[5], name[5] + " vs " + name[1], name[1] + " vs " + name[4], name[4] + " vs " + name[0]]   
elif r_number == "8":
    insert_name("P1", name)
    insert_name("P2", name)
    insert_name("P3", name)
    insert_name("P4", name)
    insert_name("P5", name)
    insert_name("P6", name)
    insert_name("P7", name)
    insert_name("P8", name)        
    rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[6], name[6] + " vs " + name[7], name[7] + " vs " + name[0], name[0] + " vs " + name[2], name[1] + " vs " + name[3], name[2] + " vs " + name[4], name[3] + " vs " + name[5], name[4] + " vs " + name[6], name[5] + " vs " + name[7], name[6] + " vs " + name[0], name[7] + " vs " + name[1], name[0] + " vs " + name[3], name[3] + " vs " + name[6], name[6] + " vs " + name[1], name[1] + " vs " + name[4], name[4] + " vs " + name[7], name[7] + " vs " + name[2], name[2] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[4], name[1] + " vs " + name[5], name[2] + " vs " + name[6], name[3] + " vs " + name[7]]
else:
    print("erm no :3c")
    action = "q"


#Player Inserter
def insert_player(r_number, i):
    
    if r_number == 3:
        insert_name("P4", name)
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[0], name[0] + " vs " + name[2], name[1] + " vs " + name[3]]
        
        if i == 2: #All i values are always round number - 1
            i = 4 

        r_number = "4"
    
    elif r_number == 4:
        insert_name("P5", name)
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[0], name[0] + " vs " + name[2], name[2] + " vs " + name[4], name[4] + " vs " + name[1], name[1] + " vs " + name[3], name[3] + " vs " + name[0]]
    
        if i == 3:
            i = 9
        elif i == 4:
            i = 5
        elif i == 5:
            i = 8

        r_number = "5"

    elif r_number == 5:
        insert_name("P6", name)
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[2], name[1] + " vs " + name[3], name[2] + " vs " + name[4], name[3] + " vs " + name[5], name[4] + " vs " + name[0], name[5] + " vs " + name[1], name[0] + " vs " + name[3], name[1] + " vs " + name[4], name[2] + " vs " + name[5]]
    
        if i == 4:
            i = 8
        elif i == 5 or i == 6 or i == 8:
            i += 1
        elif i == 7:
            i = 13
        elif i == 9:
            i = 12

        r_number = "6"

    elif r_number == 6:
        insert_name("P7", name) 
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[6], name[6] + " vs " + name[0], name[0] + " vs " + name[2], name[2] + " vs " + name[4], name[4] + " vs " + name[6], name[6] + " vs " + name[1], name[1] + " vs " + name[3], name[3] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[3], name[3] + " vs " + name[6], name[6] + " vs " + name[2], name[2] + " vs " + name[5], name[5] + " vs " + name[1], name[1] + " vs " + name[4], name[4] + " vs " + name[0]]   
    
        if i == 5:
            i = 13
        elif i == 6:
            i = 7
        elif i == 7:
            i = 11
        elif i == 9:
            i = 12
        elif i == 10:
            i = 20
        elif i == 11:
            i = 18
        elif i == 12:
            i = 14
        elif i == 13:
            i = 19
        elif i == 14:
            i = 17


        r_number = "7"

    elif r_number == 7:
        insert_name("P8", name)
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[6], name[6] + " vs " + name[7], name[7] + " vs " + name[0], name[0] + " vs " + name[2], name[1] + " vs " + name[3], name[2] + " vs " + name[4], name[3] + " vs " + name[5], name[4] + " vs " + name[6], name[5] + " vs " + name[7], name[6] + " vs " + name[0], name[7] + " vs " + name[1], name[0] + " vs " + name[3], name[3] + " vs " + name[6], name[6] + " vs " + name[1], name[1] + " vs " + name[4], name[4] + " vs " + name[7], name[7] + " vs " + name[2], name[2] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[4], name[1] + " vs " + name[5], name[2] + " vs " + name[6], name[3] + " vs " + name[7]]
    
        if i == 6:
            i = 11
        elif i == 7 or i == 8 or i == 9 or i == 11 or i == 12:
            i += 1
        elif i == 10:
            i = 18
        elif i == 13:
            i = 23
        elif i == 14 or i == 15:
            i += 2
        elif i == 16:
            i = 26
        elif i == 17:
            i = 22
        elif i == 18:
            i = 25
        elif i == 20:
            i = 24
        
        r_number = "8"
    
    elif r_number == 8:
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[6], name[6] + " vs " + name[7], name[7] + " vs " + name[0], name[0] + " vs " + name[2], name[1] + " vs " + name[3], name[2] + " vs " + name[4], name[3] + " vs " + name[5], name[4] + " vs " + name[6], name[5] + " vs " + name[7], name[6] + " vs " + name[0], name[7] + " vs " + name[1], name[0] + " vs " + name[3], name[3] + " vs " + name[6], name[6] + " vs " + name[1], name[1] + " vs " + name[4], name[4] + " vs " + name[7], name[7] + " vs " + name[2], name[2] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[4], name[1] + " vs " + name[5], name[2] + " vs " + name[6], name[3] + " vs " + name[7]]
        print("Cannot add more players!!")

    return rotation, i, r_number

#Player Remover
def remove_player(r_number, i):

    if r_number != 3:
        rm_name = input("Input player name to remove:\n")

    if r_number == 3:
        print("Can't remove any more players!!")
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[0]]
        r_number = "3"
    
    elif r_number == 4:
        remove_name(name, rm_name)
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[0]]
        r_number = "3"

        if i == 5:
            i = 0
        elif i == 3 or i == 4:
            i = 2
    
    elif r_number == 5:
        remove_name(name, rm_name)
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[0], name[0] + " vs " + name[2], name[1] + " vs " + name[3]]
        r_number = "4"

        if i == 3 or i == 5:
            i = 4
        elif i == 6 or i == 7 or i == 8:
            i = 5
        elif i == 9:
            i = 3
    
    elif r_number == 6:
        remove_name(name, rm_name)
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[0], name[0] + " vs " + name[2], name[2] + " vs " + name[4], name[4] + " vs " + name[1], name[1] + " vs " + name[3], name[3] + " vs " + name[0]]
        r_number = "5"

        if i == 4 or i == 5 or i == 6:
            i = 5
        elif i == 7:
            i = 8
        elif i == 8:
            i = 6
        elif i == 9 or i == 10:
            i = 4
        elif i == 11 or i == 12:
            i = 9
        elif i == 13:
            i = 7
        elif i == 14:
            i = 0
        
    elif r_number == 7:
        remove_name(name, rm_name)
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[2], name[1] + " vs " + name[3], name[2] + " vs " + name[4], name[3] + " vs " + name[5], name[4] + " vs " + name[0], name[5] + " vs " + name[1], name[0] + " vs " + name[3], name[1] + " vs " + name[4], name[2] + " vs " + name[5]]
        r_number = "6"

        if i == 5 or i == 6 or i == 7:
            i = 6
        elif i == 8:
            i = 7
        elif i == 10 or i == 11:
            i = 9
        elif i == 12:
            i = 10
        elif i == 13:
            i = 5
        elif i == 14:
            i = 12
        elif i == 15 or i == 16 or i == 17:
            i = 14
        elif i == 18:
            i = 11
        elif i == 19:
            i = 13
        elif i == 20:
            i = 8
    
    elif r_number == 8:
        remove_name(name, rm_name)
        rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[6], name[6] + " vs " + name[0], name[0] + " vs " + name[2], name[2] + " vs " + name[4], name[4] + " vs " + name[6], name[6] + " vs " + name[1], name[1] + " vs " + name[3], name[3] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[3], name[3] + " vs " + name[6], name[6] + " vs " + name[2], name[2] + " vs " + name[5], name[5] + " vs " + name[1], name[1] + " vs " + name[4], name[4] + " vs " + name[0]]   
        r_number = "7"

        if i == 6 or i == 8:
            i = 7
        elif i == 9:
            i = 11
        elif i == 10:
            i = 8
        elif i == 11:
            i = 12
        elif i == 12:
            i = 9
        elif i == 13 or i == 14:
            i = 6
        elif i == 15 or i == 16:
            i = 14
        elif i == 17:
            i = 15
        elif i == 18:
            i = 10
        elif i == 20 or i == 21 or i == 22:
            i = 17
        elif i == 23:
            i = 13
        elif i == 24:
            i = 20
        elif i == 25:
            i = 18
        elif i == 26:
            i = 16
        elif i == 27:
            i = 1

    return rotation, i, r_number


# The Actual Rotation Function
i = int(0)
print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
while action != "q":
    action = input("Enter:\n'n' or nothing for next round\n'p' for previous round\n'q' to quit\n'a' to add player \n'r' to remove player \nanything else to display round\n")
    if action == "n" or action == "":
        i = (i+1) % len(rotation)
        print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
    elif action == "p":
        i = (i-1) % len(rotation)
        print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
    elif action == "q":
        print("\nThanks for using this tool!")
    elif action == "a":
        print("\n")
        rotation, i, r_number = insert_player(int(r_number), i)
        print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
    elif action == "r":
        print("\n")
        rotation, i, r_number = remove_player(int(r_number), i)
        print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
    else:
        print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
    
