# Imports
import re

class Lexan:
    def __init__(self, TOKEN, VALUE, POSITION, LENGTH):
        self.TOKEN = "<" + TOKEN + ">"
        self.VALUE = VALUE
        self.POSITION = POSITION
        self.LENGTH = LENGTH

    def __repr__(self):
        return self.TOKEN

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
def isAlphanum(x):
    return isCharacter(x) or isNumber(x) or isUnderscore(x)
def isQuote(x):
    return x == "\"" or x == "\'"
