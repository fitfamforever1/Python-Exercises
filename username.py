# Username Validation Program

# Get username input from user
username = input("Enter your username: ")

# Validate username
if len(username) > 12:
    print("Username must be at most 12 characters long")
elif username.count(" ") > 0:
    print("Username must not contain spaces")
elif username.isalpha() == False:
    print("Username must only contain letters")

# If all conditions are satisfied, the username is valid
else:
    print("Username is valid")