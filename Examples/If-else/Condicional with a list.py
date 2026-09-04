# Asign to `approved_list` a list of the names of authorized users 

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Asign to `username` one specific user that tries login 

username = "user"

# If the user trying to log in is among the authorized users, a message will be shown indicating that they are authorized to access this device
# Otherwise, a message will be shown indicating that they don't have access to this device

if username in approved_list:
    print("You have access to this device.")
else:
    print("You don't have access to this device.")

# Assign to `organization_hours` a boolean value that represents whether the user is trying to log in during the organization's schedule

organization_hours = True

# If the entered value of `organization_hours` is True, it will display 'Login attempt made during the organization's schedule'
# Otherwise, it will display 'Login attempt made outside the organization's schedule'

if organization_hours == True:
    print("Login attempt made during the organization's schedule")
else:
    print("Login attempt made outside the organization's schedule")