import json
from cryptography.fernet import Fernet

"""
To do:

[1] add encryptions
[2] add users
[3] switch to exel format

state: works
"""

mainMessage = """

[1] Add password
[2] Load password
[3] exit

"""

def mainScreen(mainMessage):

    # start screen for the program. lets  you choose action

    run = True
    while run:
        print(mainMessage)
        action = input("What you want to do: ")
        print("\n")

        if action == "1":
            saveNew()
        elif action == "2":
            loadSaved()
        elif action == "3":
            run = False
            print("Exiting... ")




def getData():

    # gets the data from the user and sends it back to saveNew()

    user = input("Enter a username: ")
    password = input("Enter a password: ")
    passwordConfirm = input("Confirm your password: ")

    while password != passwordConfirm:
        print("your password does not match")
        password = input("Enter a password: ")
        passwordConfirm = input("Confirm your password: ")
    
    website = input("Enter the website: ")

    data = {
        "username": user,
        "password": password,
        "website": website
    }

    return data

def saveNew():

    # gets the data  with getData() and save to the file

    data = getData()

    with open("./data.json",'r+') as file:
        file_data = json.load(file)

        if data not in file_data["passwords"]:
            file_data["passwords"].append(data)
        else:
            return "Already exist"

        file.seek(0)
        json.dump(file_data, file, indent = 4)

        return "success"

def loadSaved():

    # load the file and search the wanted cerdentials

    with open("./data.json",'r') as file:
        file_data = json.load(file)
        websites = {}

    empty = True

    i = 1
    for cerdentials in file_data["passwords"]:
        if cerdentials["website"] not in websites:
            empty = False
            websites[str(i)] = (cerdentials["website"])
    
    if not empty:

        i = 0
        for website in websites:
            i+=1
            print(f"[{i}] {websites[str(i)]}")
        
        
        while True:

            try:
                webChoose = websites[input("\nchoose website: ")]
                break
            except KeyError:
                print("Please choose from the list")

        for cerdentials in file_data["passwords"]:
            if cerdentials["website"] == webChoose:
                print(cerdentials)
    else:
        print("\n\nThere is no saves\n\n")
    


        

def main():

    # loads main screen

    mainScreen(mainMessage)


if __name__ == "__main__":
    main()
