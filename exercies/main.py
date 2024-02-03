
flag = ""
while flag != 'quit':
    user_input = input("Enter a valid number(Type quit to end the program): ")
    # If the user does not type 'quit'
    # we can convert the valid user input to float
    if user_input != 'quit':
        user_input = float(user_input)
    else:
        flag = 'quit'
        break; # exit from the loop
    if user_input > 0:
        print("You have supplied is a positive number.")
    elif user_input < 0:
        print("The supplied number is a negative number.")
    else:
        print("You've entered 0.")