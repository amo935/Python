# Asign to `approved_user1` and `approved_user2` the name of authorized users 

approved_user1 = "elarson"
approved_user2 = "bmoreno"

# Asign to `username` one specific user that tries login 

username = "bmoreno"

# If the user trying to log in is among the authorized users, a message will be shown indicating that they are authorized to access this device
# Otherwise, a message will be shown indicating that they don't have access to this device

if username == approved_user1 or username == approved_user2:
    print("This user has access to this device.")
else:
    print("This user doesn't have access to this device.")