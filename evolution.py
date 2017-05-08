from random import *
def run():
    characters = "~`!@#$%^&*()_+-={}|[]\:;<>?,./ 1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    print("Here is the list of characters that are valid. Note that quotation marks are not allowed.\n\n" + characters + "\n")
    string = input("What string would you like to form? ")
    newString = ""
    counter = 0
    for i in range(len(string)):
        newString += characters[randint(0, len(characters)-1)] 
    while(newString != string):
        stringL = list(string)
        newStringL = list(newString)
        for i in range(len(stringL)):
            if(newStringL[i] != stringL[i]):
                newStringL[i] = characters[randint(0, len(characters)-1)]
        newString = "".join(newStringL)
        print(newString)
        counter += 1
    print("\nThat string took " + str(counter) + " generations!\n\nRunning again now!\n")
    run()
run()
