def operator(lexan):
    if not lexan.TOKEN in ("<ASSIGNMENTOPERATOR>", "<UNARYOPERATOR>", "<COMPOUNDOPERATOR>"):
        raise Exception("Token <CONSTANT> must be of type <INTCON> | <CHARCON> | <STRCON")
    return lexan

def const(lexan):
    if not lexan.TOKEN in ("<INTCON>", "<CHARCON>", "<STRCON>"):
        raise Exception("Token <CONSTANT> must be of type <INTCON> | <CHARCON> | <STRCON")
    return lexan

def parse(lexans):
    print(lexans)