# This app asks for the user's age and categorise the age

# Step one : Ask for user name
print("Welcome!, please enter your username.")
username = input()

# Greet the user and ask for the user's age
print("Hello!", username, "what is your age?, Please ensure you enter a valid number")
userage = input()
userage = int(userage)
if userage >= 0 and userage <= 12:
    print("Dear",username, "You are in the Child Age Category")
elif userage >= 13 and userage <= 19:
    print("Dear",username, "You are a teenager")
elif userage >= 20 and userage <= 64:
    print("Dear", username,  "You are an An Adult")
else:
    print("You are a SeniorMan")
