from tokens import *


class Statement:
    def __init__(self, child):
        self.child = child

    def __repr__(self):
        return f"Statement({self.child})"


class PrintI:
    def __init__(self, child):
        self.child = child

    def __repr__(self):
        return f"PrintI({self.child})"


class PrintC:
    def __init__(self, child):
        self.child = child

    def __repr__(self):
        return f"PrintC({self.child})"


class IntCon:
    def __init__(self, child):
        self.child = child

    def __repr__(self):
        return f"IntCon({self.child})"


class CharCon:
    def __init__(self, child):
        self.child = child

    def __repr__(self):
        return f"CharCon({self.child})"


class StrCon:
    def __init__(self, child):
        self.child = child

    def __repr__(self):
        return f"StrCon({self.child})"

    def eval(self):
        output = ""
        for c in self.child:
            output += "DAT {}\n".format(ord(c))
        output += "DAT 3\n"
        return output
