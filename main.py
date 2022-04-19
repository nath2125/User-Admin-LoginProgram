import time  # allows for the usage of time within the code
import string  # allows for the usage of string within the code
import random  # allows for the usage of random gen within the code

#inputs a bunch of blank lines to keep a gap between each menu
def clr(lines=100):
    print('\n' * lines)

#Main Login Screen
def menuscreen_options():  # defines this section of code so it can be called upon or reference too

    print("Welcome to the Login Screen! Here are your Selections!")  # Welcomes the user into the main screen
    print("")  # creates a gap between the next and previous line

    time.sleep(1)  # delays the next line

    print("1: User Login,")  # displays the "user login" menu option
    time.sleep(1)  # delays the next line
    print("2: Register for account,")  # displays the "register for account" menu option
    time.sleep(1)  # delays the next line
    print("3: Admin Login,")  # displays the "admin login" menu option
    time.sleep(1)  # delays the next line
    print("4: Password Generator")  # displays the "password generator" menu option
    time.sleep(1)  # delays the next line
    print("5: Exit,")  # displays the "exit" menu option
    time.sleep(1)  # delays the next line

    print("")  # creates a gap between the next and previous line
    print("Please choose from the following options above!")  # prints choose from following options

    menuscreenanswer = input("")  # allows for input from user to then send the user based on option decided
    if menuscreenanswer == ("1"):  # puts the "loginscreen" as the first option
        clr()  # clears the previous code off the screen
        loginscreen()  # sends the user to the "loginscreen" menu
    if menuscreenanswer == ("2"):  # puts the "registerforaccount" as the second option
        clr()  # clears the previous code off the screen
        registerforaccount()  # sends the user to the "registerforaccount" menu
    if menuscreenanswer == ("3"):  # puts the "adminlogin" as the third option
        clr()  # clears the previous code off the screen
        adminlogin()  # sends the user to the "adminlogin" menu
    if menuscreenanswer == ("4"):  # puts the "passwordgenerator" as the fourth option
        clr()  # clears the previous code off the screen
        passwordgenerator()  # sends the user to the "passwordgenerator" menu
    if menuscreenanswer == ("5"):  # puts the "quit" function as the fifth option
        quit()  # quits the program and cuts the code
    else:  # else command that sends the user here if they haven't selected the correct option
        print("")  # creates a gap between the next and previous line
        print("Invalid Option, Try Again!")  # prints that the user put in a invalid option
        print("")  # creates a gap between the next and previous line
        time.sleep(1)  # delays the next line
        clr()  # clears the previous code off the screen
        menuscreen_options()  # takes the user back to the menu


#User Login Screen
def loginscreen():  # defines this section of code so it can be called upon or reference too

    username = input("Username: ")  # allows input for username
    password = input("Password: ")  # allows input for password

    f1 = open('accountlistfile.txt', 'r')  # opens accountlistfile.txt for reading
    info = f1.read()  # program assigns the file to an object to be read (info)
    info = info.split()  # splits the info with a space between

    if username and password in info:  # searches for username and password in the file object
        index = info.index(username)  # indexes the username within info objects
        print("Login Successful!")  # message to print out if username there
        f1.close()  # closes the txt file
        quit()   # quits the program and cuts the code
    else:
        print("")  # creates a gap between the next and previous line
        print("Account Details Incorrect! Please Try Again!")  # message that account details are incorrect
        print("")  # creates a gap between the next and previous line
        time.sleep(1)  # delays the next line
        clr()  # clears the previous code off the screen
        loginscreen()  # takes the user back to the menu

def passwordgenerator():  # defines this section of code so it can be called upon or reference too
    print("Welcome to the Password Generator:")  # welcomes user to the random password generator

    time.sleep(1)  # delays the next line

    while True:  # white true condition
        length = int(input('\nEnter the length of password: '))  # inputing the users choice for length of password and set as "length"

        lower = string.ascii_lowercase  # setting 'string.ascii_lowercase' as lower
        upper = string.ascii_uppercase  # setting 'string.ascii_uppercase' as upper
        num = string.digits  # setting 'string.digits' as num
        symbols = string.punctuation  # setting 'string.punctuation' as symbols

        all = lower + upper + num + symbols  # combining all character types together and setting as 'all'

        temp = random.sample(all, length)  # creating random password with chosen 'length' and 'all' character types

        password = "".join(temp)  # making the 'password' the random generated phrase.

        print(password)  # prints the random generated password created
        print("")  # creates a gap between the next and previous line
        another = input("Would you like another password? 'Yes' or 'No' ")  # allows for user to have another password created
        if another == "Yes" or "yes":  # if the user says yes it will re-run this section of code
            print("")  # creates a gap between the next and previous line
            continue  # continues the while condition code
        break  # if anything else inputed it will break and stop

#User Register For Account Screen
def registerforaccount():  # defines this section of code so it can be called upon or reference too
    print("Please Type Your Chosen Username: ")  # prints "type your chose username"
    username = input("Username: ")  # allows for user to type in their chosen username and set as username

    f1 = open("accountlistfile.txt", 'r')  # opens accountlistfile.txt for reading
    info = f1.read()  # program assigns the file to an object to be read (info)
    info = info.split()  # splits the info with a space between

    if username in info:  # searches for username in the file object
        print("")  # creates a gap between the next and previous line
        print("Username has been taken. Please Choose Another!")
        print("")  # creates a gap between the next and previous line
        f1.close()  # closes the txt file
        time.sleep(1)  # delays the next line
        clr()  # clears the previous code off the screen
        registerforaccount()  # takes user back to the 'registerforaccount' menu
    else:
        print("")  # creates a gap between the next and previous line
        print("Your username has been recorded!")  # displays that your username has been recorded
        print("")  # creates a gap between the next and previous line
        time.sleep(1)  # delays the next line
        print("")  # creates a gap between the next and previous line
        print("Please Choose From the Following!: ")  # displays to choose from the following
        time.sleep(1)  # delays the next line
        print("1. Would you like to create your own password! ")  # displays would you like to create your own password
        time.sleep(1)  # delays the next line
        print("2. Get a Randomly Generated Password! ")  # displays would you like to get a random generated password

        g = input("Select 1 or 2:")  # asks user to input their choice on what type of password
        if g == "1":  # continues the code of chosen password
            password = input("Enter your chosen password: ")  # Assigning username for the password
            with open("accountlistfile.txt", 'a') as f1:  # opens the tx file as 'f1'
                combo = username + " " + password  # puts username and generated password together with space and sets as combo
                f1.write(combo + "\n")  # writes the line created in "combo" to "accountlistfile.txt"
                f1.close()  # close the txt file
                time.sleep(2)  # delays the next line
                print("")  # creates a gap between the next and previous line
                print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                print("")  # creates a gap between the next and previous line
        else:  # continues down the random generated password
            print("A Randomly Generated Password Will Be Created for You!")  # displays a random generated password will be created for the user
            useDigits = input("Would you like your password to include numbers? Y or N: ")  # number included option for password
            if useDigits.lower() == "n" or useDigits.lower() == "N":  # checks the digit
                use_digits = False  # sets use_digits as false
                usePunctuation = input("\nWould you like to include symbols? Y or N: ")  # symbols included option for password
                if usePunctuation.lower() == "n" or usePunctuation.lower() == "N":  # checks digit
                    use_punctuation = False  # sets use_punctuation as false
                    passLength = input("\nWould you like to choose the amount of characters? Y or N: ")  # option for chooseing amount of character for the password
                    if passLength == "n" or passLength == "N":  # checks input
                        password_length = 10  # sets password length as 10
                        source = string.ascii_letters  # the source of what will be included in generated password
                        result_str = "".join([random.choice(source) for i in range(password_length)])  # created the random password with the chosen source within the required length already set and sets as result_str
                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + result_str)  # displays the new password
                        with open("accountlistfile.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + result_str  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to accountlistfile.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                    else:
                        pass_Length = True  # sets pass_Length as true
                        length = int(input('\nEnter the length of password: '))  # inputing the users choice for length of password and set as "length"
                        source = string.ascii_letters   # the source of what will be included in generated password
                        temp = random.sample(source, length)  # creating random password with chosen 'length' and all 'source' character types

                        passwordstr = "".join(temp)  # making the 'password' the random generated phrase.

                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + passwordstr)  # displays the new password
                        with open("accountlistfile.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + passwordstr  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to accountlistfile.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                else:
                    use_punctuation = True  # sets use_punctuation as false
                    passLength = input("\nWould you like to choose the amount of characters? Y or N: ")  # option for chooseing amount of character for the password
                    if passLength == "n" or passLength == "N":  # checks input
                        password_length = 10  # sets password length as 10
                        source = string.ascii_letters + string.punctuation  # the source of what will be included in generated password
                        result_str = "".join([random.choice(source) for i in range(password_length)])  # created the random password with the chosen source within the required length already set and sets as result_str
                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + result_str)  # displays the new password
                        with open("accountlistfile.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + result_str  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to accountlistfile.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                    else:
                        pass_Length = True  # sets pass_Length as true
                        length = int(input('\nEnter the length of password: '))  # inputing the users choice for length of password and set as "length"
                        source = string.ascii_letters + string.punctuation   # the source of what will be included in generated password
                        temp = random.sample(source, length)  # creating random password with chosen 'length' and all 'source' character types

                        passwordstr = "".join(temp)  # making the 'password' the random generated phrase

                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + passwordstr)  # displays the new password
                        with open("accountlistfile.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + passwordstr  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to accountlistfile.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
            else:
                use_digits = True  # sets use_digits as True
                usePunctuation = input("\nWould you like to include symbols? Y or N: ")  # symbols included option for password
                if usePunctuation.lower() == "n" or usePunctuation.lower() == "N": # checks input
                    use_punctuation = False  # sets use_punctuation as false
                    passLength = input("\nWould you like to choose the amount of characters? Y or N: ")  # option for chooseing amount of character for the password
                    if passLength == "n" or passLength == "N":  # checks input
                        password_length = 10  # sets password length as 10
                        source = string.ascii_letters + string.digits  # the source of what will be included in generated password
                        result_str = "".join([random.choice(source) for i in range(password_length)])  # created the random password with the chosen source within the required length already set and sets as result_str
                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + result_str)  # displays the new password
                        with open("accountlistfile.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + result_str  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to accountlistfile.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                    else:
                        pass_Length = True  # sets pass_Length as true
                        length = int(input('\nEnter the length of password: '))  # inputing the users choice for length of password and set as "length"
                        source = string.ascii_letters + string.punctuation   # the source of what will be included in generated password
                        temp = random.sample(source, length)  # creating random password with chosen 'length' and all 'source' character types

                        passwordstr = "".join(temp)  # making the 'password' the random generated phrase.

                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + passwordstr)  # displays the new password
                        with open("accountlistfile.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + passwordstr  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to accountlistfile.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                else:
                    use_digits = True  # sets use_digits to True
                    use_punctuation = True  # sets use_punctuation to True
                    passLength = input("\nWould you like to choose the amount of characters? Y or N: ")  # option for chooseing amount of character for the password
                    if passLength == "n" or passLength == "N":  # checks input
                        password_length = 10  # sets password length as 10
                        source = string.ascii_letters + string.punctuation + string.digits  # the source of what will be included in generated password
                        result_str = "".join([random.choice(source) for i in range(password_length)])  # created the random password with the chosen source within the required length already set and sets as result_str
                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + result_str)  # displays the new password
                        with open("accountlistfile.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + result_str  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to accountlistfile.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                    else:
                        pass_Length = True  # sets pass_Length as true
                        length = int(input('\nEnter the length of password: '))  # inputing the users choice for length of password and set as "length"
                        source = string.ascii_letters + string.punctuation   # the source of what will be included in generated password
                        temp = random.sample(source, length)  # creating random password with chosen 'length' and all 'source' character types

                        passwordstr = "".join(temp)  # making the 'password' the random generated phrase.

                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + passwordstr)  # displays the new password
                        with open("accountlistfile.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + passwordstr  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to accountlistfile.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line

    time.sleep(1)  # delays the next line
    clr()  # clears the previous code off the screen
    print("Type 'Back' To Go Back Or 'Quit' To Exit ")  # displays type back to go back or quit to exit

    registeraccountsanswer = input("")  # wait for input on the user to decide where to go
    if registeraccountsanswer == "Back" or "back":  # checks input
        clr()  # clears the previous code off the screen
        menuscreen_options()  # sends the user back to the main menu screen

    else:  # if anything else
        quit()  # quits the program and cuts the code

#Admin Login
def adminlogin():  # defines this section of code so it can be called upon or reference too
    username = input("Username: ")  # allows input for username
    password = input("Password: ")  # allows input for password

    f1 = open('adminaccountlist.txt', 'r')  # opens accountlistfile.txt for reading
    info = f1.read()  # program assigns the file to an object to be read (info)
    info = info.split()  # splits the info with a space between

    if username and password in info:  # searches for username and password in the file object
        index = info.index(username)  # indexes the username within info objects
        print("Login Successful!")  # message to print out if username there
        f1.close()  # closes the file
        time.sleep(1)  # delays the next line
        clr()  # clears previous code off the screen
        adminmenuscreen()  # takes user back to admin menu
    else:
        print("")  # creates a gap between the next and previous line
        print("Account Details Incorrect! Please Try Again!")  # message that account details are incorrect
        print("")  # creates a gap between the next and previous line
        time.sleep(1)  # delays the next line
        clr()  # clears the previous code off the screen
        adminlogin()  # takes the user back to the admin login menu

#Admin Menu Screen
def adminmenuscreen():  # defines this section of code so it can be called upon or reference too
    print("Welcome to the Administration Menu! Here are your Selections!")  # Welcomes the user to the admin menu screen
    print("")  # creates a gap between the next and previous line

    time.sleep(1)  # delays the next line

    print("1: Create Admin Account,")  # displays the "create admin account" menu option
    time.sleep(1)  # delays the next line
    print("2: View User Accounts,")  # displays the "view user accounts" menu option
    time.sleep(1)  # delays the next line
    print("3: Back To Main User Menu,")  # displays the "back to the main user menu" menu option
    time.sleep(1)  # delays the next line
    print("4. Quit")  # displays the "exit" menu option

    print("")  # creates a gap between the next and previous line
    print("Please choose from the following options above!")  # prints choose from the following options

    adminscreenanswer = input("")  # allows for input from user to then send the user based on option decided
    if adminscreenanswer == ("1"):  # puts the "registeradminforaccount" as the first option
        clr()  # clears the previous code off the screen
        registeradminforaccount()  # sends the user to the "registeradminforaccount" menu
    if adminscreenanswer == ("2"):  # puts the "viewuseraccounts" as the second option
        clr()  # clears the previous code off the screen
        viewuseraccounts()  # sends the user to the "viewuseraccounts" menu
    if adminscreenanswer == ("3"):  # puts the "menuscreen_options" as the third option
        clr()  # clears the previous code off the screen
        menuscreen_options()  # sends the user to the "menuscreen_options" menu
    if adminscreenanswer == ("4"):  # puts the "quit" function as the fourth option
        quit()  # quits the program and cuts the code
    else:
        print("")  # creates a gap between the next and previous line
        print("Invalid Option, Try Again!")  # prints that the user put in a invalid option
        print("")  # creates a gap between the next and previous line
        time.sleep(1)  # delays the next line
        clr()  # clears the previous code off the screen
#takes the user back to the menu

def registeradminforaccount():  # defines this section of code so it can be called upon or reference too
    print("Please Type Your Chosen Username: ")  # prints "type your chose username"
    username = input("Username: ")  # allows for user to type in their chosen username and set as username

    f1 = open("adminaccountlist.txt", 'r')  # opens adminaccountlist.txt for reading
    info = f1.read()  # program assigns the file to an object to be read (info)
    info = info.split()  # splits the info with a space between

    if username in info:  # searches for username in the file object
        print("")  # creates a gap between the next and previous line
        print("Username has been taken. Please Choose Another!")
        print("")  # creates a gap between the next and previous line
        f1.close()  # closes the txt file
        time.sleep(1)  # delays the next line
        clr()  # clears the previous code off the screen
        registeradminforaccount()  # takes user back to the 'registeradminforaccount' menu
    else:
        print("")  # creates a gap between the next and previous line
        print("Your username has been recorded!")  # displays that your username has been recorded
        print("")  # creates a gap between the next and previous line
        time.sleep(1)  # delays the next line
        print("")  # creates a gap between the next and previous line
        print("Please Choose From the Following!: ")  # displays to choose from the following
        time.sleep(1)  # delays the next line
        print("1. Would you like to create your own password! ")  # displays would you like to create your own password
        time.sleep(1)  # delays the next line
        print("2. Get a Randomly Generated Password! ")  # displays would you like to get a random generated password

        g = input("Select 1 or 2:")  # asks user to input their choice on what type of password
        if g == "1":  # continues the code of chosen password
            password = input("Enter your chosen password: ")  # Assigning username for the password
            with open("adminaccountlist.txt", 'a') as f1:  # opens the txt file as 'f1'
                combo = username + " " + password  # puts username and generated password together with space and sets as combo
                f1.write(combo + "\n")  # writes the line created in "combo" to "adminaccountlist.txt"
                f1.close()  # close the txt file
                time.sleep(2)  # delays the next line
                print("")  # creates a gap between the next and previous line
                print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                print("")  # creates a gap between the next and previous line
        else:  # continues down the random generated password
            print("A Randomly Generated Password Will Be Created for You!")  # displays a random generated password will be created for the user
            useDigits = input("Would you like your password to include numbers? Y or N: ")  # number included option for password
            if useDigits.lower() == "n" or useDigits.lower() == "N":  # checks the digit
                use_digits = False  # sets use_digits as false
                usePunctuation = input("\nWould you like to include symbols? Y or N: ")  # symbols included option for password
                if usePunctuation.lower() == "n" or usePunctuation.lower() == "N":  # checks digit
                    use_punctuation = False  # sets use_punctuation as false
                    passLength = input("\nWould you like to choose the amount of characters? Y or N: ")  # option for chooseing amount of character for the password
                    if passLength == "n" or passLength == "N":  # checks input
                        password_length = 10  # sets password length as 10
                        source = string.ascii_letters  # the source of what will be included in generated password
                        result_str = "".join([random.choice(source) for i in range(password_length)])  # created the random password with the chosen source within the required length already set and sets as result_str
                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + result_str)  # displays the new password
                        with open("adminaccountlist.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + result_str  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to adminaccountlist.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                    else:
                        pass_Length = True  # sets pass_Length as true
                        length = int(input('\nEnter the length of password: '))  # inputing the users choice for length of password and set as "length"
                        source = string.ascii_letters   # the source of what will be included in generated password
                        temp = random.sample(source, length)  # creating random password with chosen 'length' and all 'source' character types

                        passwordstr = "".join(temp)  # making the 'password' the random generated phrase.

                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + passwordstr)  # displays the new password
                        with open("adminaccountlist.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + passwordstr  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to adminaccountlist.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                else:
                    use_punctuation = True  # sets use_punctuation as false
                    passLength = input("\nWould you like to choose the amount of characters? Y or N: ")  # option for chooseing amount of character for the password
                    if passLength == "n" or passLength == "N":  # checks input
                        password_length = 10  # sets password length as 10
                        source = string.ascii_letters + string.punctuation  # the source of what will be included in generated password
                        result_str = "".join([random.choice(source) for i in range(password_length)])  # created the random password with the chosen source within the required length already set and sets as result_str
                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + result_str)  # displays the new password
                        with open("adminaccountlist.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + result_str  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to adminaccountlist.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                    else:
                        pass_Length = True  # sets pass_Length as true
                        length = int(input('\nEnter the length of password: '))  # inputing the users choice for length of password and set as "length"
                        source = string.ascii_letters + string.punctuation   # the source of what will be included in generated password
                        temp = random.sample(source, length)  # creating random password with chosen 'length' and all 'source' character types

                        passwordstr = "".join(temp)  # making the 'password' the random generated phrase

                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + passwordstr)  # displays the new password
                        with open("adminaccountlist.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + passwordstr  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to adminaccountlist.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
            else:
                use_digits = True  # sets use_digits as True
                usePunctuation = input("\nWould you like to include symbols? Y or N: ")  # symbols included option for password
                if usePunctuation.lower() == "n" or usePunctuation.lower() == "N": # checks input
                    use_punctuation = False  # sets use_punctuation as false
                    passLength = input("\nWould you like to choose the amount of characters? Y or N: ")  # option for chooseing amount of character for the password
                    if passLength == "n" or passLength == "N":  # checks input
                        password_length = 10  # sets password length as 10
                        source = string.ascii_letters + string.digits  # the source of what will be included in generated password
                        result_str = "".join([random.choice(source) for i in range(password_length)])  # created the random password with the chosen source within the required length already set and sets as result_str
                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + result_str)  # displays the new password
                        with open("adminaccountlist.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + result_str  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to v
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                    else:
                        pass_Length = True  # sets pass_Length as true
                        length = int(input('\nEnter the length of password: '))  # inputing the users choice for length of password and set as "length"
                        source = string.ascii_letters + string.punctuation   # the source of what will be included in generated password
                        temp = random.sample(source, length)  # creating random password with chosen 'length' and all 'source' character types

                        passwordstr = "".join(temp)  # making the 'password' the random generated phrase.

                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + passwordstr)  # displays the new password
                        with open("adminaccountlist.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + passwordstr  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to adminaccountlist.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                else:
                    use_digits = True  # sets use_digits to True
                    use_punctuation = True  # sets use_punctuation to True
                    passLength = input("\nWould you like to choose the amount of characters? Y or N: ")  # option for chooseing amount of character for the password
                    if passLength == "n" or passLength == "N":  # checks input
                        password_length = 10  # sets password length as 10
                        source = string.ascii_letters + string.punctuation + string.digits  # the source of what will be included in generated password
                        result_str = "".join([random.choice(source) for i in range(password_length)])  # created the random password with the chosen source within the required length already set and sets as result_str
                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + result_str)  # displays the new password
                        with open("adminaccountlist.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + result_str  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to adminaccountlist.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line
                    else:
                        pass_Length = True  # sets pass_Length as true
                        length = int(input('\nEnter the length of password: '))  # inputing the users choice for length of password and set as "length"
                        source = string.ascii_letters + string.punctuation   # the source of what will be included in generated password
                        temp = random.sample(source, length)  # creating random password with chosen 'length' and all 'source' character types

                        passwordstr = "".join(temp)  # making the 'password' the random generated phrase.

                        print("Here Is Your New Password: (Keep This In A Safe Place!!)")  # displays here is your new password
                        print("New Password: " + passwordstr)  # displays the new password
                        with open("adminaccountlist.txt", 'a') as f1:  # opens the txt file as f1
                            combo = username + " " + passwordstr  # puts username and generated password together with space and sets as combo
                            f1.write(combo + "\n")  # writes the line created in combo to adminaccountlist.txt
                            f1.close()  # close the file
                            time.sleep(2)  # delays the next line
                            print("")  # creates a gap between the next and previous line
                            print("Your Account Details Have Been Recorded!")  # displays that the account details have been recorded
                            print("")  # creates a gap between the next and previous line

    time.sleep(1)  # delays the next line
    clr()  # clears the previous code off the screen
    print("Type 'Back' To Go Back Or 'Quit' To Exit ")  # displays type back to go back or quit to exit

    registeradminforaccountsanswer = input("")  # wait for input on the user to decide where to go
    if registeradminforaccountsanswer == "Back" or "back":  # checks input
        clr()  # clears the previous code off the screen
        adminmenuscreen()  # sends the user back to the admin menu screen

    else:  # if anything else
        quit()  # quits the program and cuts the code

#Screen for accessing and Viewing current accounts
def viewuseraccounts():  # defines this section of code so it can be called upon or reference too
    f1 = open("accountlistfile.txt", "r")  # open txt file and set as f1
    print(f1.read())  # print the file object txt file
    print()  # print blank line
    f1.close()  # closes txt file

    time.sleep(1)  # delays the next line

    print("Type 'Back' To Go Back Or 'Quit' To Exit ")  # displays type back to go back or quit to exit

    viewaccountsanswer = input("")  # wait for input on the user to decide where to go
    if viewaccountsanswer == "Back" or "back":  # checks input
        clr()  # clears the previous code off the screen
        adminmenuscreen()  # sends the user to the "adminmenuscreen"
    else:
        quit()  # quits the program and cuts the code

#Runs the first menu for the application
menuscreen_options()
