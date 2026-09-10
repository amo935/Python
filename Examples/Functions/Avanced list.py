# Define a function called `list_to_string()`

def list_to_string():

  # Stores the list of authorized usernames in a variable called `username_list`

  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

# Assign an empty string to `sum_variable`

  sum_variable = ""

  # Write a for loop that iterates through the elements of `username_list` and displays each element

  for i in username_list:
    sum_variable = sum_variable + i + ", "

  # Display the value of `sum_variable`

  print(sum_variable)

# Calls the `list_to_string()` function

list_to_string()

