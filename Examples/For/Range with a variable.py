# Create a variable called `connection_attempts` that stores the number of times the user has attempted to connect to the network

connection_attempts = 4

# Iterative statement using `for`, `range()`, a loop variable `i`, and `connection_attempts`
# Displays "Connection could not be established" as many times as specified by `connection_attempts`

for i in range(connection_attempts):
    print("Connection could not be established.")

