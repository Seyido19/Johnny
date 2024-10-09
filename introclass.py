# This app askes you your name, sge and tells you your age in 2 year's time

#  Step one - Greet the user and ask their name
print("Welcome, Please what is your name?")
username = input()

# Step two, greet the user by the name and ask for their age
print("Hello",username, "How old are you?")
userage = int(input())

# Step three, Tell the user their age next year 
if userage < 18:
    print(f"Dear {username} you are a minor. You will {userage+1} years old next year.")
elif userage <=30:
    print(f"Dear {username} you are a young adult. You will {userage+1} years old next year.")
elif userage <=45:
    print(f"Dear {username} you are middle-age. You will {userage+1} years old next year.")
elif userage <=75:
    print(f"Dear {username} you are getting old. You will {userage+1} years old next year.")
else:
    print(f"Dear {username} you are quite. You will {userage+1} years old next year.")
    