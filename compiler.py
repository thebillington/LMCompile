# Imports
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
            tokens.append([SPACE, " ", pos, 1])
        elif data[pos] == "\n":
            tokens.append([LINEFEED, "\\n", pos, 1])
        elif data[pos] == "\r":
            tokens.append([CARRIAGERETURN, "\\r", pos, 1])
        elif data[pos] == "\t":
            tokens.append([TAB, "\\t", pos, 1])
        elif data[pos] == ";":
            tokens.append([SEMICOLON, ";", pos, 1])

        # Check for strings
        if data[pos] == "\"":

            # Set the start point
            start = pos

            # Create a new string
            string = data[pos]

            # Set the length of the identifier
            length = 1

            # While we haven't reached something that isn't a letter, number or underscore
            while not data[pos + length] == "\"":

                # Add to the identifier and increment pos by length
                string += data[pos + length]
                pos += length

            # Add the closing quotation mark
            string += data[pos + length]
            pos += 1

            # Add the string constant
            tokens.append([STRINGCON, string, start, length + 1])

        # Check if the position is a letter
        elif isCharacter(data[pos]) or isUnderscore(data[pos]):

            # Set the start point
            start = pos

            # Add to a new string
            identifier = data[pos]

            # Set the length of the identifier
            length = 1

            # While we haven't reached something that isn't a letter, number or underscore
            while isIdentifier(data[pos + length]):

                # Add to the identifier and increment pos by length
                identifier += data[pos + length]
                pos += length

            # Check if the identifier is a reserved word
            if identifier in reservedWords:
                tokens.append([RESERVEDWORD, identifier, start, length])
            else:
                tokens.append([IDENTIFIER, identifier, start, length])

        # If the position is an equals, check if the character after is as well
        elif data[pos] == "=":
            if data[pos + 1] == "=":
                tokens.append([COMPOUNDOPERATOR, "==", pos, 2])
                pos += 1
            else:
                tokens.append([ASSIGNMENTOPERATOR, "=", pos, 1])
                

        # Go to the next position
        pos += 1

            

    return tokens
            
            

if __name__ == "__main__":
    
    tks = lex("main.sc")

    out = ""

    for t in tks:
        print("{} '{}' AT LOCATION {} OF FILE".format(tokens[t[0]], t[1], t[2]))
        out += tokens[t[0]]

    print(out)
