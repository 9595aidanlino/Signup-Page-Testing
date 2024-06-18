import time
import sys

dot = '...'

def get_username():
    while True:
        user = input("Enter a username: ")
        if len(user) <= 25:
            print("You will be proceeded soon..")
            return user
        else:
            print("Enter a maximum of 25 letters for the username")
            print("Locking Sign Up")
            time.sleep(10)
            sys.exit()

def get_age():
    while True:
        age = input('Enter your age: ')
        if age.isdigit() and 0 < int(age) <= 100:
            print("You will be proceeded soon")
            return int(age)
        else:
            print("Age not verified, Locking")
            time.sleep(10)
            sys.exit()

def get_password():
    while True:
        pw = input('Enter a password for your account: ')
        if len(pw) < 50:
            print(f"Signing you up {dot}")
            return pw
        else:
            print(f"Locking you out {dot}")
            sys.exit()

def verify_login(user, pw):
    login_info = user + pw
    verf = input("Please enter your password and username as shown YouruserPassword: ")
    if verf == login_info:
        print(f"You have successfully logged in {dot}")
    else:
        print(f"Wrong password {dot}")
        sys.exit()

def change_password(pw):
    change = input('Do you wish to change your password? (yes/no): ').strip().lower()
    if change == "yes":
        new_password = input("Enter your new password: ")
        return new_password
    elif change == "no":
        print("Alright")
        return pw
    else:
        print(f"Enter an appropriate value next time {dot}")
        sys.exit()

def open_app():
    ask = input("Do you wish to open an app? (yes/no): ").strip().lower()
    if ask == "yes":
        print(f"You will be proceeded soon {dot}")
        return True
    elif ask == "no":
        print(f"Shutting down for 5 minutes {dot}")
        time.sleep(300)
        return False
    else:
        print('Error 404')
        sys.exit()

def main():
    print("Welcome to Sign Up Page")
    
    user = get_username()
    age = get_age()
    pw = get_password()
    
    verify_login(user, pw)
    
    pw = change_password(pw)
    
    open_app()

if __name__ == "__main__":
    main()
