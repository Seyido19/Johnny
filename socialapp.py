# This app displays which student is most and least social and states their number of friends.

myclass ={}
myclass['John']={'age':19,'email':'Johnny234@gamil.com','gender':'M','friends':['solomon','omolola','james']}
myclass['John']={'age':29,'email':'Rachel234@gamil.com','gender':'F','friends':['marvellous','Israel']}
myclass['Uche']={'age':29,'email':'Uche234@yahoo.com','gender':'M','friends':[]}
myclass['Emmy']={'age':19,'email':'Johnny234@gamil.com','gender':'M','friends':['Abdul','chioma','Uju']}

# Set variable for collatimg most or least friends
max = 100
min = 0

# loop through the dictionary

for key in myclass:
    user = myclass[key] # get each user's attributes
    friendslist = user['friends'] # get each user's friend list
    if len(friendslist) < max: # compare the lenght of the list with the integer provided
        least_social = key
        max = len(friendslist)
    if len(friendslist) > 0:
        most_social = key
        min = len(friendslist)
print(f"{least_social} is the least sociable person in the class. Number of Friends: {max}\n{most_social} is the most sociable person with {min} friends")
    
