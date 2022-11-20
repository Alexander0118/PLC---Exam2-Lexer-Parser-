from Lexer import Lexer
from Lexer import Token


class Parser:
    lexer = Lexer()
    token = Token()
    nextToken = None

    # Compile function
    def compile(self, inputString):
        self.lexer.analyzer(inputString)
        self.getNextToken()
        self.expr()

    # Statement Function
    def stamnt(self):
        # <stamnt> --> <if_stamnt> | <while_stamnt> | <assign>

        match self.nextToken.TYPE:
            case self.lexer.MEANTIME:
                self.whle_loop()
            case self.lexer.IDENT:
                self.assign()
            case self.lexer.WHETHER:
                self.if_stamnt()
            case _:
                self.error()

    # Assign Function
    def assign(self):
        # <assign> --> `id` `=` <expr>

        if self.nextToken.TYPE == self.lexer.IDENT:
            self.getNextToken()
            if self.nextToken.TYPE == self.lexer.ASIGN_OP:
                self.getNextToken()
                self.term()
            else:
                print("Assignment Error")
                quit()
        else:
            print("ID Error")
            quit()

    # If Statement
    def if_stamnt(self):
        # <if_stamnt> --> ‘whether’ `(` <expr> `)` <stamnt>

        if self.nextToken.TYPE == self.lexer.WHETHER:
            self.getNextToken()
            if self.nextToken.TYPE == self.lexer.L_PAREN:
                self.getNextToken()
                self.bool_rel()
                if self.nextToken.TYPE == self.lexer.R_PAREN:
                    self.getNextToken()
                    self.stamnt()
                else:
                    print("Left Parenthesis Error")
                    quit()
            else:
                print("Right Parenthesis Error")
                quit()
        else:
            print("Whether Error")

    # While Loop Function
    def whle_loop(self):
        # <while_loop> -->  `while``(`<expr>`)` <stamnt>

        if self.nextToken.TYPE == self.lexer.MEANTIME:
            self.getNextToken()
            if self.nextToken.TYPE == self.lexer.L_PAREN:
                self.getNextToken()
                self.bool_rel()
                if self.nextToken.TYPE == self.lexer.R_PAREN:
                    self.getNextToken()
                    self.stamnt()
                else:
                    print("Left Parenthesis Error")
                    quit()
            else:
                print("Right Parenthesis Error")
                quit()
        else:
            print("Meantime Error")

    # Expression Function
    def expr(self):
        # <expr> --> <term> { (`+`|`-`) <term> }

        self.term()
        while (
            self.nextToken.TYPE == self.lexer.ADDI_SGN
            or self.nextToken.TYPE == self.lexer.SUB_SGN
        ):
            self.getNextToken()
            self.term()

    # Term Function
    def term(self):
        # <term> --> <factor> { (`*`|`/`|`%`) <factor> }

        self.factor()
        while (
            self.nextToken.TYPE == self.lexer.MULT_SGN
            or self.nextToken.TYPE == self.lexer.DIV_SGN
            or self.nextToken.TYPE == self.lexer.MOD_OP
        ):
            self.getNextToken()
            self.factor()

    # Boolean Equation Function
    def bool_eq(self):
        # <bool_eq> --> <bool_rel> { (`!=` | `==`) <bool_rel> }

        self.bool_rel()
        while (
            self.nextToken.TYPE == self.lexer.NTEQLTO
            or self.nextToken.TYPE == self.lexer.EQLTO
        ):
            self.getNextToken()
            self.bool_rel()

    # Boolean Relation Function
    def bool_rel(self):
        # <bool_rel> --> <expr> { (`<` | `>` | `<=` | `>=`) <expr> }

        self.expr()
        while (
            self.nextToken.TYPE == self.lexer.LESTHN
            or self.nextToken.TYPE == self.lexer.GRTHN
            or self.nextToken.TYPE == self.lexer.LESEQLTO
            or self.nextToken.TYPE == self.lexer.GREQLTO
        ):
            self.getNextToken()
            self.expr()

    # Factor Function
    def factor(self):
        # <factor> --> `id` | `num_lit` |`(` <expr> `)`

        if (
            self.nextToken.TYPE == self.lexer.IDENT
            or self.nextToken.TYPE == self.lexer.NUM_LIT
        ):
            self.getNextToken()
        elif self.nextToken.TYPE == self.lexer.L_PAREN:
            self.getNextToken()
            self.expr()
            if self.nextToken.TYPE == self.lexer.R_PAREN:
                self.getNextToken()
            else:
                print("Right Parenthesis Error")
                quit()
        else:
            print("Left Parenthesis Error")
            quit()

    # Call the next token function
    def getNextToken(self):
        self.nextToken = self.lexer.getNext()

    # Error Function
    def error(self):
        print("Error")
        quit()


# Calls files to read through them and parse the content within
def main():
    # Change filename here
    file = open("test1.txt", "r")
    with file as lex_file:
        for line in lex_file:
            parser = Parser()
            parser.compile(line.rstrip("\n"))


main()
