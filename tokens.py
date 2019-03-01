# Imports
import re

# Store the valid tokens as strings
tokens = [
    "<IDENTIFIER>",
    "<INTCON>",
    "<CHARCON>",
    "<STRINGCON>",
    "<END>",
    "<SPACE>",
    "<ASSIGNMENTOPERATOR>",
    "<UNARYOPERATOR>",
    "<PARENTHESIS>",
    "<LINEFEED>",
    "<CARRAGERETURN>",
    "<TAB>",
    "<SEMICOLON>",
    "<RESERVEDWORD>"
]

# Create the 'enums'
IDENTIFIER = 0
INTCON = 1
CHARCON = 2
STRINGCON = 3
END = 4
SPACE = 5
ASSIGNMENTOPERATOR = 6
UNARYOPERATOR = 7
PARENTHESIS = 8
LINEFEED = 9
CARRAGERETURN = 10
TAB = 11
SEMICOLON = 12
RESERVEDWORD = 13

# Store the reserved words
reservedWords = [
    "print",
    "int"
]

# Define functions to check if something is a given token
def isCharacter(x):
    return re.search("[a-zA-Z]", x)
def isNumber(x):
    return re.search("[0-9]", x)
def isUnderscore(x):
    return x == "_"
def isOperator(x):
    return re.search("[\\=\\*\\/\\%\\+\\-\\<\\>\\&\\^\\|\\~\\!]", x)
def isParenthesis(x):
    return re.search("[\\(\\)\\{\\}]", x)
def isIdentifier(x):
    return isCharacter(x) or isNumber(x) or isUnderscore(x)
