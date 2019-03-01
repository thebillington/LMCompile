# Imports
import os
from tokens import *

# Set the start position
global pos

# Create a global variable for the data
global data

# Function to load a file
def load(fName):

    # Fetch the globals
    global data
    global pos
    pos = 0

    # Check that the file exists
    if not os.path.isfile(fName):
        print("'{}' was not found\nCheck the file name and try again".format(fName))
        return

    # Fetch the data from the file
    data = open(fName,"r").read() + "\0"

# Create a function to lex a given file
def lexan():

    # Fetch the position of the lexer
    global pos

    # Create a list to hold the tokens
    tokens = []

    # Count the number of tokens
    count = -1

    # Check for end of file
    if data[pos] == "\0":
        return [END, "\0", pos, 1]

    # Check if the position in the string is a one character token
    if data[pos] == " ":
        return [SPACE, " ", pos, 1]
    elif data[pos] == "\n":
        return [LINEFEED, "\\n", pos, 1]
    elif data[pos] == "\r":
        return [CARRIAGERETURN, "\\r", pos, 1]
    elif data[pos] == "\t":
        return [TAB, "\\t", pos, 1]
    elif data[pos] == ";":
        return [SEMICOLON, ";", pos, 1]
    elif isParenthesis(data[pos]):
        return [PARENTHESIS, data[pos], pos, 1]

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
            return [CHARCON, string, start, 3]
        else:
            return [STRINGCON, string, start, length + 1]

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
        return [INTCON, num, start, length]

        

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
            return [RESERVEDWORD, identifier, start, length]
        else:
            return [IDENTIFIER, identifier, start, length]

    # If the position is an equals, check if the character after is as well
    elif data[pos] == "=":
        if data[pos + 1] == "=":
            return [COMPOUNDOPERATOR, "==", pos, 2]
            pos += 1
        else:
            return [ASSIGNMENTOPERATOR, "=", pos, 1]
    # Check for compound operator
    elif isOperator(data[pos]):

        # Check whether the next location is an operator
        if not isOperator(data[pos + 1]):
            return [UNARYOPERATOR, data[pos], pos, 1]
        else:

            # Fetch the compound operator
            operator = data[pos] + data[pos + 1]
            
            # Check whether it is a valid compound operator
            if operator in compoundOperators:
                return [COMPOUNDOPERATOR, operator, pos, 2]
            
            

if __name__ == "__main__":

    # Open the file
    load("main.sc")

    # While we haven't reached the end of the file
    while pos < len(data):
        t = lexan()
        print("{} '{}' AT LOCATION {} OF FILE".format(tokens[t[0]], t[1], t[2]))
        pos += 1
