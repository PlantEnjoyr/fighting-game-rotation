#Functions
def insert_name(default_name, list):

    ans = input("Enter name of " + default_name + ": ")

    if ans == "":
        list.append(default_name)
    else:
        list.append(ans)

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
    rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[2], name[2] + " vs " + name[4], name[4] + " vs " + name[0], name[1] + " vs " + name[3], name[3] + " vs " + name[5], name[5] + " vs " + name[1], name[0] + " vs " + name[3], name[1] + " vs " + name[4], name[2] + " vs " + name[5]]
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
    rotation = [name[0] + " vs " + name[1], name[1] + " vs " + name[2], name[2] + " vs " + name[3], name[3] + " vs " + name[4], name[4] + " vs " + name[5], name[5] + " vs " + name[6], name[6] + " vs " + name[7], name[7] + " vs " + name[0], name[0] + " vs " + name[2], name[2] + " vs " + name[4], name[4] + " vs " + name[6], name[6] + " vs " + name[0], name[1] + " vs " + name[3], name[3] + " vs " + name[5], name[5] + " vs " + name[7], name[7] + " vs " + name[1], name[0] + " vs " + name[3], name[3] + " vs " + name[6], name[6] + " vs " + name[1], name[1] + " vs " + name[4], name[4] + " vs " + name[7], name[7] + " vs " + name[2], name[2] + " vs " + name[5], name[5] + " vs " + name[0], name[0] + " vs " + name[4], name[1] + " vs " + name[5], name[2] + " vs " + name[6], name[3] + " vs " + name[7]]
else:
    print("erm no :3c")
    action = "q"


# The Actual Rotation Function
i = int(0)
print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
while action != "q":
    action = input("Enter nothing or n for next round, p for previous round, q to quit and anything else to display current round\n")
    if action == "n" or action == "":
        i = (i+1) % len(rotation)
        print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
    elif action == "p":
        i = (i-1) % len(rotation)
        print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
    elif action == "q":
        print("\nThanks for using this tool!")
    else:
        print("\nRound " + str(i+1) + ": " + rotation[i] + "\n")
    
