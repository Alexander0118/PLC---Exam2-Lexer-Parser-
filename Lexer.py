import enum
import sys

# Token contains the original text and the type of token.
class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText  # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind  # The TokenType that this token is classified as.

    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # Relies on all keyword enum values being above 20
            if kind.name == tokenText and kind.value >= 20 and kind.value < 35:
                return kind
        return None


# TokenType is our enum for all the types of tokens.
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMS = 1
    IDENT = 2
    STRING = 3
    LABEL = 21
    GOTO = 22
    PRINT = 23
    INPUT = 24
    LET = 25
    WHETHER = 26
    THEN = 27
    ENDWHETHER = 28
    MEANTIME = 29
    REPEAT = 30
    ENDMEANTIME = 31
    EQL = 41
    ADDI_SGN = 42
    SUB_SGN = 43
    MULT_SGN = 44
    DIV_SGN = 45
    MOD_OP = 52
    EQLTO = 46
    NTEQLTO = 47
    LESTHN = 48
    LESEQLTO = 49
    GRTHN = 50
    GREQLTO = 51
    L_PAREN = 52
    R_PAREN = 53


class Lexer:
    def __init__(self, input):
        self.source = input + "\n"  # Source code to lex as a string
        self.currentChar = ""  # Gets the current character in the string
        self.currentPos = -1  # Gets the current position in the string
        self.nextChar()

    # Processes the next character
    def nextChar(self):
        self.currentPos += 1
        if self.currentPos >= len(self.source):
            self.currentChar = "\0"  # EOF
        else:
            self.currentChar = self.source[self.currentPos]

    # Returns the lookahead character
    def peek(self):
        if self.currentPos + 1 >= len(self.source):
            return "\0"
        return self.source[self.currentPos + 1]

    # Prints the error messages
    def error(self, message):
        sys.exit("Lexing error. " + message)

    # Skips whitespace except the start of a new line. Indicates the end of a statement
    def skipWhitespace(self):
        while (
            self.currentChar == " "
            or self.currentChar == "\t"
            or self.currentChar == "\r"
        ):
            self.nextChar()

    # Skips comments
    def skipComment(self):
        if self.currentChar == "#":
            while self.currentChar != "\n":
                self.nextChar()

    # Gets the next token
    def getToken(self):
        self.skipWhitespace()
        self.skipComment()
        token = None

        if self.currentChar == "+":
            token = Token(self.currentChar, TokenType.ADDI_SGN)
        elif self.currentChar == "-":
            token = Token(self.currentChar, TokenType.SUB_SGN)
        elif self.currentChar == "*":
            token = Token(self.currentChar, TokenType.MULT_SGN)
        elif self.currentChar == "%":
            token = Token(self.currentChar, TokenType.MOD_OP)
        elif self.currentChar == "/":
            token = Token(self.currentChar, TokenType.DIV_SGN)
        elif self.currentChar == "(":
            token = Token(self.currentChar, TokenType.L_PAREN)
        elif self.currentChar == ")":
            token = Token(self.currentChar, TokenType.R_PAREN)
        elif self.currentChar == "=":
            # Checks whether it's = or ==
            if self.peek() == "=":
                lastChar = self.currentChar
                self.nextChar()
                token = Token(lastChar + self.currentChar, TokenType.EQLTO)
            else:
                token = Token(self.currentChar, TokenType.EQL)
        elif self.currentChar == ">":
            # Checks whether it's > or >=
            if self.peek() == "=":
                lastChar = self.currentChar
                self.nextChar()
                token = Token(lastChar + self.currentChar, TokenType.GREQLTO)
            else:
                token = Token(self.currentChar, TokenType.GRTHN)
        elif self.currentChar == "<":
            # Checks whether it's < or <=
            if self.peek() == "=":
                lastChar = self.currentChar
                self.nextChar()
                token = Token(lastChar + self.currentChar, TokenType.LESEQLTO)
            else:
                token = Token(self.currentChar, TokenType.LESTHN)
        elif self.currentChar == "!":
            if self.peek() == "=":
                lastChar = self.currentChar
                self.nextChar()
                token = Token(lastChar + self.currentChar, TokenType.NTEQLTO)
            else:
                self.error("Expected !=, got !" + self.peek())
        elif self.currentChar == '"':
            # Get characters between quotations.
            self.nextChar()
            startPos = self.currentPos

            while self.currentChar != '"':
                # Don't allow special characters in the string.
                if (
                    self.currentChar == "\r"
                    or self.currentChar == "\n"
                    or self.currentChar == "\t"
                    or self.currentChar == "\\"
                    or self.currentChar == "%"
                ):
                    self.error("Illegal character in string.")
                self.nextChar()

            tokText = self.source[startPos : self.currentPos]
            token = Token(tokText, TokenType.STRING)
        elif self.currentChar.isdigit():
            # The first character is a digit so recognizes it as a number
            # Get all digits or decimal numbers
            startPos = self.currentPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == ".":  # Classifies it as a decimal number
                self.nextChar()

                # There must be another digit after the decimal
                if not self.peek().isdigit():
                    self.error("Illegal character in number.")
                while self.peek().isdigit():
                    self.nextChar()

            tokText = self.source[startPos : self.currentPos + 1]
            token = Token(tokText, TokenType.NUMS)
        elif self.currentChar.isalpha():
            # The first character is a letter so recognizes it as an ID or keyword
            startPos = self.currentPos
            while self.peek().isalnum():
                self.nextChar()

            # Checks if the token is in the list of keywords
            tokText = self.source[startPos : self.currentPos + 1]
            keyword = Token.checkIfKeyword(tokText)
            if keyword == None:
                token = Token(tokText, TokenType.IDENT)
            else:
                token = Token(tokText, keyword)
        elif self.currentChar == "\n":
            token = Token(self.currentChar, TokenType.NEWLINE)
        elif self.currentChar == "\0":
            token = Token("", TokenType.EOF)
        else:
            # Throws error if the token is not known
            self.error("Unknown token: " + self.currentChar)

        self.nextChar()
        return token
