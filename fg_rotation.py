#Functions
def insert_name(default_name):

    ans = input("Enter name of " + default_name + ": ")

    if ans == "":
        return default_name
    else:
        return ans


rotation = ["no rotation selected :P"]
action = ""

# Setting Up Rotation Cycle
r_number = input("Insert # of players (3 to 8)\n")
if r_number == "3":
    p1 = insert_name("P1")
    p2 = insert_name("P2")
    p3 = insert_name("P3")
    rotation = [p1 + " vs " + p2, p2 + " vs " + p3, p3 + " vs " + p1]
elif r_number == "4":
    p1 = insert_name("P1")
    p2 = insert_name("P2")
    p3 = insert_name("P3")
    p4 = insert_name("P4")
    rotation = [p1 + " vs " + p2, p2 + " vs " + p3, p3 + " vs " + p4, p4 + " vs " + p1, p1 + " vs " + p3, p2 + " vs " + p4]
elif r_number == "5":
    p1 = insert_name("P1")
    p2 = insert_name("P2")
    p3 = insert_name("P3")
    p4 = insert_name("P4")
    p5 = insert_name("P5")
    rotation = [p1 + " vs " + p2, p2 + " vs " + p3, p3 + " vs " + p4, p4 + " vs " + p5, p5 + " vs " + p1, p1 + " vs " + p3, p3 + " vs " + p5, p5 + " vs " + p2, p2 + " vs " + p4, p4 + " vs " + p1]
elif r_number == "6":
    p1 = insert_name("P1")
    p2 = insert_name("P2")
    p3 = insert_name("P3")
    p4 = insert_name("P4")
    p5 = insert_name("P5")
    p6 = insert_name("P6")
    rotation = [p1 + " vs " + p2, p2 + " vs " + p3, p3 + " vs " + p4, p4 + " vs " + p5, p5 + " vs " + p6, p6 + " vs " + p1, p1 + " vs " + p3, p3 + " vs " + p5, p5 + " vs " + p1, p2 + " vs " + p4, p4 + " vs " + p6, p6 + " vs " + p2, p1 + " vs " + p4, p2 + " vs " + p5, p3 + " vs " + p6]
elif r_number == "7":
    p1 = insert_name("P1")
    p2 = insert_name("P2")
    p3 = insert_name("P3")
    p4 = insert_name("P4")
    p5 = insert_name("P5")
    p6 = insert_name("P6")
    p7 = insert_name("P7")
    rotation = [p1 + " vs " + p2, p2 + " vs " + p3, p3 + " vs " + p4, p4 + " vs " + p5, p5 + " vs " + p6, p6 + " vs " + p7, p7 + " vs " + p1, p1 + " vs " + p3, p3 + " vs " + p5, p5 + " vs " + p7, p7 + " vs " + p2, p2 + " vs " + p4, p4 + " vs " + p6, p6 + " vs " + p1, p1 + " vs " + p4, p4 + " vs " + p7, p7 + " vs " + p3, p3 + " vs " + p6, p6 + " vs " + p2, p2 + " vs " + p5, p5 + " vs " + p1]   
elif r_number == "8":
    p1 = insert_name("P1")
    p2 = insert_name("P2")
    p3 = insert_name("P3")
    p4 = insert_name("P4")
    p5 = insert_name("P5")
    p6 = insert_name("P6")
    p7 = insert_name("P7")
    p8 = insert_name("P8")
    rotation = [p1 + " vs " + p2, p2 + " vs " + p3, p3 + " vs " + p4, p4 + " vs " + p5, p5 + " vs " + p6, p6 + " vs " + p7, p7 + " vs " + p8, p8 + " vs " + p1, p1 + " vs " + p3, p3 + " vs " + p5, p5 + " vs " + p7, p7 + " vs " + p1, p2 + " vs " + p4, p4 + " vs " + p6, p6 + " vs " + p8, p8 + " vs " + p2, p1 + " vs " + p4, p4 + " vs " + p7, p7 + " vs " + p2, p2 + " vs " + p5, p5 + " vs " + p8, p8 + " vs " + p3, p3 + " vs " + p6, p6 + " vs " + p1, p1 + " vs " + p5, p2 + " vs " + p6, p3 + " vs " + p7, p4 + " vs " + p8]
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
    
