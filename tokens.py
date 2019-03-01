# Imports
import re

# Store the valid tokens as strings
tkns = [
    "<IDENTIFIER>",
    "<INTCON>",
    "<CHARCON>",
    "<STRINGCON>",
    "<END>",
    "<SPACE>",
    "<ASSIGNMENTOPERATOR>",
    "<UNARYOPERATOR>",
    "<COMPOUNDOPERATOR>",
    "<PARENTHESIS>",
    "<LINEFEED>",
    "<CARRIAGERETURN>",
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
COMPOUNDOPERATOR = 8
PARENTHESIS = 9
LINEFEED = 10
CARRIAGERETURN = 11
TAB = 12
SEMICOLON = 13
RESERVEDWORD = 14

# Store the reserved words
reservedWords = [
    "print",
    "int",
    "char",
    "str",
    "if"
]

# Store a list of valid compound operators
compoundOperators = [
    ">=",
    "<=",
    "&=",
    "|=",
    "^=",
    "+=",
    "-=",
    "*=",
    "/=",
    "&&",
    "||",
    "!="
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
def isAlphanum(x):
    return isCharacter(x) or isNumber(x) or isUnderscore(x)
def isQuote(x):
    return x == "\"" or x == "\'"
