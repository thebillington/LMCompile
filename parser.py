import string
from collections import deque

from tokens import *
from nodes import *


def parse_str_con(token: Lexan):
    for char in token.VALUE:
        if (
            char
            not in string.ascii_letters
            + string.digits
            + string.punctuation
            + string.whitespace
        ):
            raise Exception()
    return StrCon(token.VALUE)


def parse_char_con(token: Lexan):
    if token.VALUE not in string.ascii_letters:
        raise Exception()
    return CharCon(token.VALUE)


def parse_int_con(token: Lexan):
    for digit in token.VALUE:
        if digit not in string.digits:
            raise Exception()
    return IntCon(token.VALUE)


def parse_print_c(tokens: deque):
    # <PRINTC> ::= <PRINTCFUN> <OPENPARENTHESIS> <CHARCON> <CLOSEPARENTHESIS> <SEMICOLON>
    #            | <PRINTCFUN> <OPENPARENTHESIS> <STRCON> <CLOSEPARENTHESIS> <SEMICOLON>

    # <PRINTCFUN>"
    # token: Lexan = tokens.popleft()
    # if token.TOKEN != "<PRINTCFUN>":
    #     raise Exception()

    # <OPENPARENTHESIS>"
    token: Lexan = tokens.popleft()
    if token.TOKEN != "<OPENPARENTHESIS>":
        raise Exception()

    # <CHARCON>" | <STRCON>
    token: Lexan = tokens.popleft()
    if token.TOKEN == "<CHARCON>":
        char_str_con = parse_char_con(token)
        print_c = PrintC(char_str_con)
    elif token.TOKEN == "<STRCON>":
        char_str_con = parse_str_con(token)
        print_c = PrintC(char_str_con)
    else:
        raise Exception()

    # <CLOSEPARENTHESIS>"
    token: Lexan = tokens.popleft()
    if token.TOKEN != "<CLOSEPARENTHESIS>":
        raise Exception()

    # <SEMICOLON>"
    token: Lexan = tokens.popleft()
    if token.TOKEN != "<SEMICOLON>":
        raise Exception()

    return print_c


def parse_print_i(tokens: deque):
    # <PRINTI> ::= <PRINTIFUN> <OPENPARENTHESIS> <INTCON> <CLOSEPARENTHESIS> <SEMICOLON>

    # <PRINTIFUN>"
    # token: Lexan = tokens.popleft()
    # if token.TOKEN != "<PRINTIFUN>":
    #     raise Exception()

    # <OPENPARENTHESIS>"
    token: Lexan = tokens.popleft()
    if token.TOKEN != "<OPENPARENTHESIS>":
        raise Exception()

    # <INTCON>"
    token: Lexan = tokens.popleft()
    if token.TOKEN != "<INTCON>":
        raise Exception()

    int_con = parse_int_con(token)
    print_i = PrintI(int_con)

    # <CLOSEPARENTHESIS>"
    token: Lexan = tokens.popleft()
    if token.TOKEN != "<CLOSEPARENTHESIS>":
        raise Exception()

    # <SEMICOLON>"
    token: Lexan = tokens.popleft()
    if token.TOKEN != "<SEMICOLON>":
        raise Exception()

    return print_i


def parse_statement(tokens: deque):
    token: Lexan = tokens.popleft()

    if token.TOKEN == "<PRINTIFUN>":
        print_i = parse_print_i(tokens)
        return Statement(print_i)
    elif token.TOKEN == "<PRINTCFUN>":
        print_c = parse_print_c(tokens)
        return Statement(print_c)
    else:
        raise Exception()


def parse(lexans: list[Lexan]):
    tokens = deque(lexans)

    program = []

    while len(tokens) > 0:
        program.append(parse_statement(tokens))

    print(program)
