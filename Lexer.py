class Token:
    TYPE = None
    VALUE = None


class Lexer:
    listType = [
        "+",
        "-",
        "*",
        "/",
        "%",
        "(",
        ")",
        "=",
        "==",
        "<",
        ">",
        "<=",
        ">=",
        "!=",
    ]
    NUM_LIT = 14
    IDENT = 15
    WHETHER = 16
    MEANTIME = 17
    ASIGN_OP = 7
    ADDI_SGN = 0
    SUB_SGN = 1
    MULT_SGN = 2
    DIV_SGN = 3
    MOD_OP = 4
    L_PAREN = 5
    R_PAREN = 6
    EQLTO = 8
    LESTHN = 9
    GRTHN = 10
    LESEQLTO = 11
    GREQLTO = 12
    NTEQLTO = 13

    token = Token()
    lexemeList = list()

    def analyzer(self, inputString):
        def getIdent(self, input, index):
            count = index
            while count < len(input) and input[count] != " ":
                if input[count] in self.listType:
                    return input[index:count]
                count += 1
            return input[index:count]

        def switch(x):
            default = lambda x: x
            return {
                "+": (self.ADDI_SGN, "+"),
                "-": (self.SUB_SGN, "-"),
                "*": (self.MULT_SGN, "*"),
                "/": (self.DIV_SGN, "/"),
                "%": (self.MOD_OP, "%"),
                "(": (self.L_PAREN, "("),
                ")": (self.R_PAREN, ")"),
                "=": (self.ASIGN_OP, "="),
                "==": (self.EQLTO, "=="),
                "<": (self.LESTHN, "<"),
                ">": (self.GRTHN, ">"),
                "<=": (self.LESEQLTO, "<="),
                ">=": (self.GREQLTO, ">="),
                "!=": (self.NTEQLTO, "!="),
                "whether": (self.WHETHER, "whether"),
                "meantime": (self.MEANTIME, "meantime"),
            }.get(x, -1)

        i = 0

        while i < len(inputString):
            newToken = Token()
            if switch(inputString[i]) == -1:
                ident = getIdent(self, inputString, i)
                if self.isNum(ident):
                    newToken.TYPE = self.NUM_LIT
                    newToken.VALUE = ident
                    self.lexemeList.append(newToken)
                    i += len(ident) - 1
                else:
                    if ident and ident.strip():
                        newToken.TYPE = self.IDENT
                        newToken.VALUE = ident
                        self.lexemeList.append(newToken)
                        i += len(ident)
            else:
                newToken.TYPE = switch(inputString[i])[0]
                newToken.VALUE = switch(inputString[i])[1]
                self.lexemeList.append(newToken)
            i += 1

    # Checks to see if the string is a number
    def isNum(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    # Gets the next element in the list
    def getNext(self):
        if len(self.lexemeList) > 0:
            output = self.lexemeList.pop(0)
            print(
                "Next token is: %s with the lexeme being %s"
                % (output.TYPE, output.VALUE)
            )
            return output
        else:
            tmpToken = Token()
            tmpToken.TYPE = -100
            tmpToken.VALUE = "Fail"
            return tmpToken
