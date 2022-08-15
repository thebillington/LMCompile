import string

from typing import List

from utils.data_types import *


class Lexer:
    """
    Small Man C (SMC) Lexer.

    Takes in file data and returns a list of SMC tokens.

    Args
    ----------
    data : str
        The contents of an SMC file.

    Attributes
    ----------
    data : str
        The cleaned contents of an SMC file.
    pos : int
        The current position in the SMC file.
    tokens : List[Token]
        All tokens from the SMC file.

    Methods
    -------
    generate_token():
        Returns the next SMC token.
    """

    def __init__(self, data: str) -> None:
        self.data = data
        self.pos = 0
        self.tokens = []

        self.__clean()
        self.__generate_tokens()

    def __clean(self):
        """
        Cleans the SMC file.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        self.__remove_comments()
        self.__strip()

    def __remove_comments(self) -> None:
        """
        Removes comments from the SMC file.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        pos = 0
        comments = []
        start = None

        while pos < len(self.data):
            char = self.data[pos]
            if start:
                if self.data[pos] == "\n":
                    comments.append([start, pos - 1])
                    start = None
            else:
                if self.data[pos] == "/" and self.data[pos + 1] == "/":
                    start = pos
                    pos += 1
            pos += 1

        if start:
            comments.append([start, pos - 1])

        for comment in comments[::-1]:
            self.data = self.data[0 : comment[0] :] + self.data[comment[1] + 1 : :]

    def __strip(self) -> None:
        """
        Removes leading and trailing spaces in the SMC file.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        self.data = "".join(i.strip() for i in self.data.split("\n"))

    def generate_token(self) -> Token:
        """
        Generates the next token from the SMC file.

        Parameters
        ----------
        None

        Returns
        -------
        token : Token
            The next token from the SMC file.
        """

        if self.pos == len(self.data):
            return None

        # Check if the literal is a one character token
        match self.data[self.pos]:
            case ("{"):
                token = Token(TokenType.OpenBrace, self.data[self.pos], self.pos, 1)
            case ("}"):
                token = Token(TokenType.CloseBrace, self.data[self.pos], self.pos, 1)
            case ("("):
                token = Token(
                    TokenType.OpenParenthesis,
                    self.data[self.pos],
                    self.pos,
                    1,
                )
            case (")"):
                token = Token(
                    TokenType.CloseParenthesis,
                    self.data[self.pos],
                    self.pos,
                    1,
                )
            case (";"):
                token = Token(TokenType.Semicolon, self.data[self.pos], self.pos, 1)
            case ('"' | "'"):
                # Set the type of quote
                quote = self.data[self.pos]

                # Set the start point
                start = self.pos + 1

                # Create a new string
                literal = ""

                # Set the length of the identifier
                length = 1

                # While we haven't reached something that isn't a letter, number or underscore
                while not self.data[self.pos + 1] == quote:

                    # Add to the identifier and increment pos by length
                    literal += self.data[self.pos + 1]
                    length += 1
                    self.pos += 1

                self.pos += 1

                # Check if the length is 1 and if so add a character, otherwise string
                if length == 2:
                    token = Token(TokenType.CharacterLiteral, literal, start, 1)
                else:
                    token = Token(TokenType.StringLiteral, literal, start, length - 1)
            case ("0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"):
                # Set the start point
                start = self.pos

                # Create a new string
                literal = self.data[self.pos]

                # Set the length of the identifier
                length = 1

                # While we haven't reached something that isn't a letter, number or underscore
                while self.data[self.pos + 1] in string.digits:

                    # Add to the identifier and increment pos by length
                    literal += self.data[self.pos + 1]
                    length += 1
                    self.pos += 1

                # Add the integer constant
                token = Token(TokenType.IntegerLiteral, literal, start, length)
            case (
                "a"
                | "b"
                | "c"
                | "d"
                | "e"
                | "f"
                | "g"
                | "h"
                | "i"
                | "j"
                | "k"
                | "l"
                | "m"
                | "n"
                | "o"
                | "p"
                | "q"
                | "r"
                | "s"
                | "t"
                | "u"
                | "v"
                | "w"
                | "x"
                | "y"
                | "z"
                | "A"
                | "B"
                | "C"
                | "D"
                | "E"
                | "F"
                | "G"
                | "H"
                | "I"
                | "J"
                | "K"
                | "L"
                | "M"
                | "N"
                | "O"
                | "P"
                | "Q"
                | "R"
                | "S"
                | "T"
                | "U"
                | "V"
                | "W"
                | "X"
                | "Y"
                | "Z"
                | "0"
                | "1"
                | "2"
                | "3"
                | "4"
                | "5"
                | "6"
                | "7"
                | "8"
                | "9"
                | "_"
            ):
                # Set the start point
                start = self.pos

                # Add to a new string
                literal = self.data[self.pos]

                # Set the length of the identifier
                length = 1

                # While we haven't reached something that isn't a letter, number or underscore
                while (
                    self.data[self.pos + 1]
                    in string.ascii_letters + string.digits + "_"
                ):

                    # Add to the identifier and increment pos by length
                    literal += self.data[self.pos + 1]
                    length += 1
                    self.pos += 1

                # Check if the identifier is a reserved word
                if literal == "printi":
                    token = Token(TokenType.PrintI, literal, start, length)
                elif literal == "printc":
                    token = Token(TokenType.PrintC, literal, start, length)

        self.pos += 1

        return token

    def __generate_tokens(self) -> List[Token]:
        """
        Generates all tokens from the SMC file.

        Parameters
        ----------
        None

        Returns
        -------
        tokens : List[Token]
            All tokens from the SMC file.
        """

        while 1:
            t = self.generate_token()
            if t:
                self.tokens.append(t)
            else:
                break

        self.pos = 0
