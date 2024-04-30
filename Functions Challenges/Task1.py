def check_password():
    common_passwords = ['password', '123456', 'qwerty', 'abc123', 'letmein', 'monkey', 'football', 'iloveyou', 'admin']
    
    user_password = input("Enter your password: ")
    
    if user_password in common_passwords:
        print("Use a safer password! '{}' is compromised.".format(user_password))
    else:
        print("Password is safe.")

check_password()
