# Assign an initial value of 0 to `connection_attempts` to keep track of the number of times the user has attempted to connect to the network 

connection_attempts = 0 

# Iterative statement using `while` and `connection_attempts` # Displays "Connection could not be established" on each iteration, until connection_attempts reaches a specified number

while connection_attempts < 3:
    print("Connection couldn't be established")

    # Actualiza `connection_attempts` (increméntalo en 1 al final de cada iteración) 
    
    connection_attempts = connection_attempts + 1