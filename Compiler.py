from Lexer import *
from Parser import *


def compiler():
    print("Compiler Output:")

    # Change the text file here!!!
    with open("Test1.txt") as inputFile:
        input = inputFile.read()

    lexer = Lexer(input)
    parser = Parser(lexer)

    parser.program()  # Starts the parser
    print("Parsing Complete.")


compiler()
