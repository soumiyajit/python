"""

WAP to take string input from users and print the length of the string.
If the user enters quit, it should exit the program

"""

while True:
    str = raw_input("enter a string ::")
    # print(str)
    if str == "quit":
        break
    else:
        print "length of the string",  str, "is ", len(str)