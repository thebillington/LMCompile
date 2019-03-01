# Imports
import os
from tokens import *

# Set the start position
global pos

# Create a global variable for the data
global data

# Store the count of the identifiers
identifierCount = 1

# Create a symbol table
symbolTable = {}

# Store the last keyword
lastReservedWord = ""

# Store the current line and position in the line
line = 0
linePos = 0
global lines

# Function to load a file
def load(fName):

    # Fetch the globals
    global data
    global pos
    global lines
    pos = 0

    # Check that the file exists
    if not os.path.isfile(fName):
        print("'{}' was not found\nCheck the file name and try again".format(fName))
        return

    # Fetch the data from the file
    data = open(fName,"r").read() + "\0"
    lines = data.split("\n")

# Create a function to lex a given file
def lexan():

    # Fetch the globals
    global pos
    global identifierCount
    global lastReservedWord
    global line
    global linePos

    # Create a list to hold the tokens
    tokens = []

    # Count the number of tokens
    count = -1

    # Store the lex for this section
    lex = None

    # Check for end of file
    if data[pos] == "\0":
        lex = [END, "\0", pos, 1]

    # Check if the position in the string is a one character token
    if data[pos] == " ":
        lex = [SPACE, " ", pos, 1]
    elif data[pos] == "\n":
        linePos = 0
        line += 1
        lex = [LINEFEED, "\\n", pos, 1]
    elif data[pos] == "\r":
        lex = [CARRIAGERETURN, "\\r", pos, 1]
    elif data[pos] == "\t":
        lex = [TAB, "\\t", pos, 1]
    elif data[pos] == ";":
        lex = [SEMICOLON, ";", pos, 1]
    elif isParenthesis(data[pos]):
        lex = [PARENTHESIS, data[pos], pos, 1]

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
            lex = [CHARCON, string, start, 3]
        else:
            lex = [STRINGCON, string, start, length + 1]

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
        lex = [INTCON, num, start, length]

    # Check if the position is a letter
    elif isCharacter(data[pos]) or isUnderscore(data[pos]):

        # Set the start point
        start = pos

        # Add to a new string
        word = data[pos]

        # Set the length of the identifier
        length = 1

        # While we haven't reached something that isn't a letter, number or underscore
        while isAlphanum(data[pos + 1]):

            # Add to the identifier and increment pos by length
            word += data[pos + 1]
            length += 1
            pos += 1

        # Check if the identifier is a reserved word
        if word in reservedWords:
            # Store the last reserved word
            lastReservedWord = word
            lex = [RESERVEDWORD, word, start, length]
        else:

            # Check it is in the symbol table already
            if word in symbolTable:

                # Check that there is a reserved word waiting
                if not lastReservedWord == None:

                    # Already declared
                    print("\nError on line {}: {} was already declared as {}\n\t{}".format(line,word, symbolTable[word][1], lines[line]))
                    return "ERROR"
                        
            else:

                # Add to the symbol table
                symbolTable[word] = (identifierCount, lastReservedWord)
                identifierCount += 1
            
            lex = [IDENTIFIER, word, start, length]

    # If the position is an equals, check if the character after is as well
    elif data[pos] == "=":
        if data[pos + 1] == "=":
            lex = [COMPOUNDOPERATOR, "==", pos, 2]
            pos += 1
        else:
            lex = [ASSIGNMENTOPERATOR, "=", pos, 1]
    # Check for compound operator
    elif isOperator(data[pos]):

        # Check whether the next location is an operator
        if not isOperator(data[pos + 1]):
            lex = [UNARYOPERATOR, data[pos], pos, 1]
        else:

            # Fetch the compound operator
            operator = data[pos] + data[pos + 1]
            
            # Check whether it is a valid compound operator
            if operator in compoundOperators:
                lex = [COMPOUNDOPERATOR, operator, pos, 2]
            else:
                print("\nError on line {}: {} is not a valid operator\n\t{}".format(line, operator, lines[line]))
                return "ERROR"
                
                
    # If the synbol is not a space or reserved word, reset last reserved word
    if not lex[0] == RESERVEDWORD and not lex[0] == SPACE:
        lastReservedWord = None

    # Add one to the line position
    linePos += 1

    return lex

if __name__ == "__main__":

    # Open the file
    load("main.smc")

    # While we haven't reached the end of the file
    while pos < len(data):
        t = lexan()
        pos += 1
