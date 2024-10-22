# This app  allows you to create a username, password and asks you to login with it

# create username and password
print("Hello user, create your user name:")
username = input()
print("Awesome! now create a password")
password = input()

# Login with the username and password created
print("............................")
print("You have successfully signed up")
print("............................")
userlogin = input("Enter user name here >>:")
# if userlogin == username:
#     print("Nice One!")
#     userpassword = input("Enter password: ")
#     if userpassword == password:
#         print("Access Granted!")
#     else:
#         print("Wrong Password. Try again") 
# else:
#     print("Wrong User name.. Try again")

while userlogin != username:
    print("Wrong username, please try again:")
    userlogin = input()
userpassword = input ("please enter your password:")
while userpassword != password:
    print("Wrong password, please try again: ")
    userlogin = input()
print(f"Nice work, {username}. Access Ganted! ")
