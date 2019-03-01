# Import the os module
import os
from tokens import *

# Create a function to lex a given file
def lex(fName):

    # Check that the file exists
    if not os.path.isfile(fName):
        print("'{}' was not found\nCheck the file name and try again".format(fName))
        return

    # Fetch the data from the file
    data = open(fName,"r").read() + "\0"

    # Create a list to hold the tokens
    tokens = []

    # Count the number of tokens
    count = -1

    # Set the start position
    pos = 0

    # Create a loop to look over the file
    while True:

        # Check for end of file
        if data[pos] == "\0":
            break

        # Check if the position in the string is a one character token
        if data[pos] == " ":
            tokens.append([SPACE, " ", pos])
            pos += 1
            continue
        elif data[pos] == "\n":
            tokens.append([LINEFEED, "\\n", pos])
            pos += 1
            continue
        elif data[pos] == "\r":
            tokens.append([CARRIAGERETURN, "\\r", pos])
            pos += 1
            continue
        elif data[pos] == "\t":
            tokens.append([TAB, "\\t", pos])
            pos += 1
            continue
        elif data[pos] == ";":
            tokens.append([SEMICOLON, ";", pos])
            pos += 1
            continue

        pos += 1

    return tokens
            
            

if __name__ == "__main__":
    
    tks = lex("main.sc")

    for t in tks:
        print("TOKEN {} AT LOCATION {} OF FILE".format(tokens[t[0]],t[2]))
