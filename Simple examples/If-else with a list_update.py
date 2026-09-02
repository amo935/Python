# Asign to `approved_list` a list of the names of authorized users 

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Asign to `username` one specific user that tries login 

username = "bmoreno"

# Assign to `organization_hours` a boolean value that represents whether the user is trying to log in during the organization's schedule

organization_hours = True

# If the user is among the authorized users and is logging in during the organization's schedule, notify that the user has logged in
# Otherwise, notify that the username is not authorized or that the login attempt was made outside of the organization's schedule

if username in approved_list and organization_hours == True:
    print("Login attempt made by an authorized user during organization hours.")
else:
    print("Login attempt made by an unauthorized user during the organization's hours.")