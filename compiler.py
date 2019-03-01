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
            tokens.append([END, "\0", pos, 1])
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
        elif isQuote(data[pos]):

            # Set the type of quote
            quote = data[pos]

            # Set the start point
            start = pos

            # Create a new string
            string = data[pos]

            # Set the length of the identifier
            length = 1

            # While we haven't reached something that isn't a letter, number or underscore
            while not data[pos + 1] == quote:

                # Add to the identifier and increment pos by length
                string += data[pos + 1]
                length += 1
                pos += 1

            # Add the closing quotation mark
            string += data[pos + 1]
            pos += 1

            # Check if the length is 1 and if so add a character, otherwise string
            if length == 2:
                tokens.append([CHARCON, string, start, 3])
            else:
                tokens.append([STRINGCON, string, start, length + 1])

        # Check for a number
        elif isNumber(data[pos]):

            # Set the start point
            start = pos

            # Create a new string
            num = data[pos]

            # Set the length of the identifier
            length = 1

            # While we haven't reached something that isn't a letter, number or underscore
            while isNumber(data[pos + 1]):

                # Add to the identifier and increment pos by length
                num += data[pos + 1]
                length += 1
                pos += 1

            # Add the string constant
            tokens.append([INTCON, num, start, length])

            

        # Check if the position is a letter
        elif isCharacter(data[pos]) or isUnderscore(data[pos]):

            # Set the start point
            start = pos

            # Add to a new string
            identifier = data[pos]

            # Set the length of the identifier
            length = 1

            # While we haven't reached something that isn't a letter, number or underscore
            while isIdentifier(data[pos + 1]):

                # Add to the identifier and increment pos by length
                identifier += data[pos + 1]
                length += 1
                pos += 1

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
        # Check for compound operator
        elif isOperator(data[pos]):

            # Check whether the next location is an operator
            if not isOperator(data[pos + 1]):
                tokens.append([UNARYOPERATOR, data[pos], pos, 1])
            else:

                # Fetch the compound operator
                operator = data[pos] + data[pos + 1]
                
                # Check whether it is a valid compound operator
                if operator in compoundOperators:
                    tokens.append([COMPOUNDOPERATOR, operator, pos, 2])

                # Shift pos to next position
                pos += 1
                    
                

        # Go to the next position
        pos += 1

            

    return tokens
            
            

if __name__ == "__main__":
    
    tks = lex("main.sc")

    out = ""

    for t in tks:
        print("{} '{}' AT LOCATION {} OF FILE".format(tokens[t[0]], t[1], t[2]))
        out += tokens[t[0]]
