print("a) The password must be 8 or more characters long")
print("b) It should contain at least 1 uppercase letter")
print("c) It should contain at least 3 numbers")
print("d) It should at least once contain the word ‘cat’ ")
print("e) It should contain 1 question mark (?) ")
print("f) There cannot be any spaces in the password")

def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8: #checks if password is longer than 8 characters
            print("Your password is less than 8 characters long")
        elif password.isdigit() >= 3: #checks if password has more than one uppercase letter
            print("Your password needs to have at least 3 numbers")
        elif password.isupper() >= 1: #checks if password has more than three numbers
            print("Your password must have more than one uppercase letter.")
        elif  password.find("cat") <= 1: #checks if cat is in the password
            print("The word 'cat' needs to be in your password at least once")
        elif password.find("?") <= 1: #checks if there is at least one ? in password
            print("Your password must contain one question mark.")
        elif password.find(" ") > 0: #checks if there are any spaces in password.
            print("Your password cannot have any spaces.")
        else:
            print("Success")
            break
validate()