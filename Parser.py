import sys
from Lexer import *


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

        self.symbols = set()  # All variables we have declared so far
        self.labelsDeclared = set()  # Keeps track of all labels declared
        self.labelsGotoed = set()  # All labels goto'ed, so we know if they exist or not

        self.currentToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()

    # Return true if the current token matches a grammar rule
    def checkToken(self, kind):
        return kind == self.currentToken.kind

    # Return true if the next token matches a grammar rule
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Called when the rule expects a specific token, otherwise it throws an error and continues to the current token
    def match(self, kind):
        if not self.checkToken(kind):
            self.error("Expected " + kind.name + ", got " + self.currentToken.kind.name)
        self.nextToken()

    # Gets the next token
    def nextToken(self):
        self.currentToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    # Returns true if current token is considered to be a comparison operator
    def isComparisonOperator(self):
        return (
            self.checkToken(TokenType.GRTHN)
            or self.checkToken(TokenType.GREQLTO)
            or self.checkToken(TokenType.LESTHN)
            or self.checkToken(TokenType.LESEQLTO)
            or self.checkToken(TokenType.EQLTO)
            or self.checkToken(TokenType.NTEQLTO)
        )

    # Error function
    def error(self, message):
        sys.exit("Error. " + message)

    # Production Rules

    # Parent rule of the program
    def program(self):
        # <program> --> {stamnt}
        print("PROGRAM")

        # Newlines are required in my grammar
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        # Parses all the statements and then calls end of file
        while not self.checkToken(TokenType.EOF):
            self.stamnt()

        # Check that each label referenced in a GOTO is declared.
        for label in self.labelsGotoed:
            if label not in self.labelsDeclared:
                self.error("Attempting to GOTO to undeclared label: " + label)

    # The statement rule calls 7 different types of rules
    def stamnt(self):
        # <stamnt> -->

        # Allows for a print stament
        if self.checkToken(TokenType.PRINT):
            # <print> -- > "PRINT" {(<expr> | <string>)}
            print("PRINT-STATEMENT")
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                # expects a string
                self.nextToken()

            else:
                # expects an expression
                self.expr()

        # Allows for an if statement
        elif self.checkToken(TokenType.WHETHER):
            # <if> --> "WHETHER" <compar> "THEN" <stamnt> "ENDWHETHER" <nl>

            print("IF-STATEMENT")
            self.nextToken()
            self.compar()

            self.match(TokenType.THEN)
            # Expects a then token and then a newline
            self.nl()

            # Allows for the take in of more statements or none
            while not self.checkToken(TokenType.ENDWHETHER):
                self.stamnt()

            self.match(TokenType.ENDWHETHER)

        # Allows for a while loop statement
        elif self.checkToken(TokenType.MEANTIME):
            # <while> --> "MEANTIME" <compar> "REPEAT" <stamnt> "ENDMEANTIME" <nl>

            print("WHILE-STATEMENT")
            self.nextToken()
            self.compar()

            # Expects the repeat token
            self.match(TokenType.REPEAT)
            self.nl()

            # Expects one or more statements in the loop or none
            while not self.checkToken(TokenType.ENDMEANTIME):
                self.stamnt()

            self.match(TokenType.ENDMEANTIME)

        # Allows for the labeling of an ID to be called by goto
        elif self.checkToken(TokenType.LABEL):
            # <label> --> "LABEL" ident <nl>

            print("LABEL-STATEMENT")
            self.nextToken()

            # Checks to see if the label exists already and throws and error
            if self.currentToken.text in self.labelsDeclared:
                self.error("Label already exists: " + self.currentToken.text)
            self.labelsDeclared.add(self.currentToken.text)

            self.match(TokenType.IDENT)

        # Allows for the execution of another line of code instead of the current one
        elif self.checkToken(TokenType.GOTO):
            # <goto> --> ident <nl>

            print("GOTO-STATEMENT")
            self.nextToken()
            self.labelsGotoed.add(self.currentToken.text)
            self.match(TokenType.IDENT)

        # Allows for and ID to be set as an expression
        elif self.checkToken(TokenType.LET):
            # <let> --> "LET" ident {("=")} <expr> } <nl>

            print("LET-STATEMENT")
            self.nextToken()

            # Checks if the ID exists. If it does not it declares it
            if self.currentToken.text not in self.symbols:
                self.symbols.add(self.currentToken.text)

            self.match(TokenType.IDENT)
            # Calls the identification and "=" tokens
            self.match(TokenType.EQL)

            self.expr()

        # Allows for an id to be inserted
        elif self.checkToken(TokenType.INPUT):
            # <input> --> "INPUT" ident <nl>

            print("INPUT-STATEMENT")
            self.nextToken()

            # Checks if the variable exists. If it does not it declares it
            if self.currentToken.text not in self.symbols:
                self.symbols.add(self.currentToken.text)

            self.match(TokenType.IDENT)

        # If the parse is expecting a statement and it does not match any of the above, it throws and error.
        else:
            self.error(
                "Invalid statement at "
                + self.currentToken.text
                + " ("
                + self.currentToken.kind.name
                + ")"
            )
        self.nl()

    # Allows for boolean relations to be created
    def compar(self):
        # <compar> --> <expr> {( "==" | "!=" | ">" | ">=" | "<" | "<=" ) <expr> }

        print("COMPARISON")

        self.expr()
        # Makes sure there is at least one comparison operator and anoter expression right after
        if self.isComparisonOperator():
            self.nextToken()
            self.expr()
        else:
            self.error("Expected comparison operator at: " + self.currentToken.text)

        # Can even take in more comparison operators and expressions or none
        while self.isComparisonOperator():
            self.nextToken()
            self.expr()

    # Allows for expressions to be created
    def expr(self):
        # <expr> --> <term> {( "-" | "+" ) <term> }

        print("EXPRESSION")

        self.term()
        # Allows for more +/- and expressions or none
        while self.checkToken(TokenType.ADDI_SGN) or self.checkToken(TokenType.SUB_SGN):
            self.nextToken()
            self.term()

    # Allows for terms to be created
    def term(self):
        # <term> --> <unary> {( "/" | "*" | "%") <unary>}

        print("TERM")

        self.unary()
        # Allows for 0 or more *// and expressions.
        while (
            self.checkToken(TokenType.MULT_SGN)
            or self.checkToken(TokenType.DIV_SGN)
            or self.checkToken(TokenType.MOD_OP)
        ):
            self.nextToken()
            self.unary()

    # Allows for unary factors to be created
    def unary(self):
        # <unary> --> ["+" | "-"] <factor>

        print("UNARY")
        # Allows for a negative or a positive
        if self.checkToken(TokenType.ADDI_SGN) or self.checkToken(TokenType.SUB_SGN):
            self.nextToken()
        self.factor()

    # Allows for a factor to be created
    def factor(self):
        # <factor> --> numbers | ID | "(" <expr> ")"

        print("FACTOR (" + self.currentToken.text + ")")

        if self.checkToken(TokenType.NUMS):
            self.nextToken()
        elif self.checkToken(TokenType.L_PAREN):
            self.nextToken()
            self.expr()
            if self.checkToken(TokenType.R_PAREN):
                self.nextToken()
            else:
                self.error("Expecting right parenthesis")
        elif self.checkToken(TokenType.IDENT):
            # Checks that the variable exists
            if self.currentToken.text not in self.symbols:
                self.error(
                    "Calling variable before assignment: " + self.currentToken.text
                )

            self.nextToken()
        else:
            self.error("Unexpected token at " + self.currentToken.text)

    # Newline function
    def nl(self):
        # <nl> --> <'\n'>

        print("NEWLINE")

        # Expects at least one new line
        self.match(TokenType.NEWLINE)
        # Expects more than one new line
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()
