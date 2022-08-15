from enum import Enum
from dataclasses import dataclass
from typing import Tuple


class TokenType(Enum):
    """
    Possible token types in SMC.
    """

    OpenBrace = 1
    CloseBrace = 2
    OpenParenthesis = 3
    CloseParenthesis = 4
    Semicolon = 5
    IntegerLiteral = 6
    CharacterLiteral = 7
    StringLiteral = 8
    PrintI = 9
    PrintC = 10

    def __str__(self) -> str:
        return self.name


@dataclass
class Token:
    """
    Small Man C (SMC) Token.

    A token to be used to compile smc(Small Man C).

    Args
    ----------
    type : TokenType
        The type of token.
    literal : str
        The literal of the token.
    position : Tuple[int, int]
        The line and column of the literal in the SMC file.
    length : int
        The length of the literal.

    Attributes
    ----------
    data : str
        The cleaned contents of an SMC file.
    pos : int
        The current position in data.

    Methods
    -------
    generate_token():
        Returns the next SMC token.
    """

    def __init__(
        self, type: TokenType, literal: str, position: Tuple[int, int], length: int
    ) -> None:
        self.type = type
        self.literal = literal
        self.position = position
        self.length = length

    def __repr__(self) -> None:
        return f'<{self.type}, "{self.literal}">'
