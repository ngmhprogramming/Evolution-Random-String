from random import *
def run():
    characters = "~`!@#$%^&*()_+-={}|[]\:;<>?,./ 1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    length = int(input("How long would you like the string to be? "))
    string = ""
    for i in range(length):
        string += characters[randint(0, len(characters)-1)]
    print("\nYour string is:\n\n" + string + "\n\nGenerating output file.\n")
    with open("randomString.txt", "w") as outfile:
        outfile.write(string)
    run()
run()
