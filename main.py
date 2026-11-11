

# Initialize the user's health, oxygen, and score.
health = 100
oxygen = 60
score = 0

# Create a function to display the current statistics of the user. 
# This function will take in the user's health, oxygen, and score as parameters and print them out in a formatted way.
def display_statistics(health, oxygen, score):
    print(f"Health: {health}%/100%")
    # Let's evaluate the user's health and print out a message based on the current health level.
    # If health is less than 20, print a warning message to the user.
    if health < 20:
        print("WARNING: Health is critically low!")
    elif health < 50:
        print("CAUTION: Health is below 50%.")
    elif health > 80:
        print("You feel amazing your health is in good condition.")
    print(f"Oxygen: {oxygen}%/100%")
    print(f"Score: {score}")

# Create an adventure sim
# First Let's display the title of the sim
print("\n\n\n===============================================================================")
print("                        Let the Adventure Begin                                ")
print("===============================================================================\n\n") 

# Lets print out the introduction to the sim
print("Introduction: \nThe Awakening\n")
# Printing out a blank line which will be a better user experience for
# the user.
print("")
print("Year: 2287")
print("")
print("Location: Unknown Sector — Deep Space")
print("Ship: USV Horizon")

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

print("\nYou awaken violently from cryogenic sleep.")
print("Your cryogenic chamber hisses open, releasing a cloud of freezing vapor. Emergency lights flash red across the medical bay.")
print("")
print("Your head pounds. You struggle to remember your name, your mission, or how long you've been asleep.")

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

print("A computerized voice breaks the silence.")
print("")
print("WARNING. CRITICAL SHIP SYSTEM FAILURE. LIFE SUPPORT OPERATING AT 27 PERCENT. CREW STATUS: UNKNOWN.")
print("")

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

print("You stagger toward the nearest computer terminal.")

# now let's print out many lines of text with only one print statement.
# The reason this works is that I am making use of the triple quotes to print out a multi-line string.
print("""
The screen displays an unsettling message:

CREW COMPLEMENT: 47

CREW MEMBERS DETECTED: 1

LAST COMMUNICATION: 93 DAYS AGO
""")

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

print("""
Suddenly, something metallic scrapes through the ventilation shaft above your head.
You freeze.
Three heavy thuds echo through the ceiling.
Then silence.""")

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

print("""
The computer speaks again.

"Unidentified biological presence detected. Recommend immediate evacuation."

You look toward the medical bay door.
It is locked.
The lights flicker.
Whatever is inside the ventilation system has started moving again.

Your mission begins now.
""")

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

# Now print out the game directions for our user
print("""
Game Directions

You are the sole conscious survivor aboard the USV Horizon. 
Your objective is to survive ten dangerous encounters, restore critical ship systems, 
uncover the mystery of the missing crew, and escape.

Each scenario presents three choices: A, B, or C.

Your decisions determine how much oxygen remains, the condition of the ship, and your overall survival score.
""")

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

# Print out the game Rules for our user
print(""" Starting statistics
Health
100
Out of 100

Oxygen
60
Out of 100

Score
0
Survival points

Rules
- Each scenario has exactly three choices.
- Each choice changes your score, health, oxygen, or a combination.
- Record your statistics after each choice.
- Health and oxygen cannot exceed 100.
- If health or oxygen reaches 0, you immediately lose.
- If you survive all ten scenarios, your final score determines the ending.""")

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

print("""
Scoring system
Decision quality	Points
Excellent decision	+20
Reasonable but risky decision	+10
Poor decision	−10

Your possible final score ranges from −100 to 200.""")

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

display_statistics(health, oxygen, score)

print("""
Scenario 1: The Locked Medical Bay

You approach the medical bay's sealed exit.

The electronic lock is malfunctioning. Sparks shoot from the control panel.

Above you, something scratches along the ventilation duct.

A nearby terminal displays three possible ways to leave.

What do you do?

A. Force open the door using an emergency crowbar.
B. Repair the door's electronic controls using a maintenance toolkit.
C. Crawl through the ventilation shaft to bypass the locked door.
""")

# This will take the user's choice and store it in a variable called user_choice. 
user_choice = input("Enter your choice (A, B, or C): ").strip().upper()

# Now let's evaluate the user's choice and update the score, health, and oxygen accordingly.
if user_choice == "A":
    score += 10
    oxygen -= 10
    print("\nYou chose option A: Force open the door using an emergency crowbar.")
    print("You escape quickly, but the damaged door releases a burst of pressurized oxygen.")
    # Call the display_statistics function to show the updated statistics.
    display_statistics(health, oxygen, score)
elif user_choice == "B":
    score += 20
    print("\nYou chose option B: Repair the door's electronic controls using a maintenance toolkit.")
    print("You carefully reconnect the damaged circuits. The door slides open without compromising the atmosphere.")
    # Call the display_statistics function to show the updated statistics.
    display_statistics(health, oxygen, score)
elif user_choice == "C":
    score -= 10
    health -= 20
    print("\nYou chose option C: Crawl through the ventilation shaft to bypass the locked door.")
    print("You squeeze into the dark ventilation system. Something bites your arm before you escape into the corridor.")
    # Call the display_statistics function to show the updated statistics.
    display_statistics(health, oxygen, score)

# The user will have to press enter to continue the sim. This make a better user experience for the user.
input("\nPress Enter to continue...")
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)

# END OF SIMULATION this should always be the last thing that is printed out in the sim. 
# This will print out a line of underscores to separate this section from the rest of the sim.
print("_" * 80)
print("\n\nThis is the end of the current simulation. More content will be added in the future.\n\n")
# The user will have to press end to continue the sim. This make a better user experience for the user.
input("\nPress Enter to END The Simulation...")




