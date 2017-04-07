def menu():
    print("1.Message")
    print("2.Contacts")
    print("3.Games")
    print("4.Settings")
    print("5.Media")
    print("6.Web")

    choice = int(input(":"))

    menuSelection(choice)



def menuSelection(choice):
    if choice = 1:
        message()
    if choice = 2:
        contacts()
    if choice = 3:
        gameMenu()
    if choice = 4:
        settings()
    if choice = 5:
        mediaMenu()
    if choice = 6:
        webBrowser()
