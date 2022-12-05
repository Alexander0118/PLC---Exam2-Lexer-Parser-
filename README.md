# PLC - Exam2(Lexer/Parser)

### a)  Define the rules for recognizing all lexemes as their proper token

- Integer Token Codes
  - EOF = -1
    - Used to signal the end of file data
  - NEWLINE = 0
    - Indicatse the end of a line of text
  - NUMS = 1
    - Used to recognize any number. 
  - IDENT = 2
    - Used for an ID
  - STRING = 3
    - Used for a series of characters
  - LABEL = 21
    - Keyword that allows for the labeling of and ID to be called by GOTO
  - GOTO = 22
    - Keyword the allows for the execution of another line of code instead of the current one
  - PRINT = 23
    - Keyword that allows the execution of a string or expression within my language
  - INPUT = 24
    - Keyword that allows for a varible to be inserted and checks if it already exists
  - LET = 25
    - Keyword that allows for a variable to be set as an expression or number
  - WHETHER = 26
    - Keyword that initiates an if statement taking in a boolean expression
  - THEN = 27
    - Keyword that is needed within the if statement for my language to take in a statement right after
  - ENDWHETHER = 28
    - Keyword to end the if statement in my language
  - MEANTIME = 29
    - Keyword that initiates a while loop taking in a boolean expression
  - REPEAT = 30
    - Keyword that is needed within the while loop for my language to take in a statement right after
  - ENDMEANTIME = 31
    - Keyword to end the while loop in my language
  - EQL = 41
    - Regular Expression: =
    - Operator equal sign
  - ADDI_SGN = 42
    - Regular Expression: + 
    - Operator addition sign
  - SUB_SGN = 43
    - Regular Expression: -
    - Operator subtraction sign
  - MULT_SGN = 44
    - Regular Expression: *
    - Operator multiplication sign
  - DIV_SGN = 45
    - Regular Expression: /
    - Operator division sign
  - MOD_OP = 52
    - Regular Expression: %
    - Operator modulo sign
  - EQLTO = 46
    - Regular Expression: ==
    - Operator equal-to sign 
  - LESTHN = 48
    - Regular Expression: <
    - Operator less than sign
  - GRTHN = 50
    - Regular Expression: >
    - Operator greater than sign
  - LESEQLTO = 49
    - Regular Expression: <=
    - Operator less than equal-to sign
  - GREQLTO = 51
    - Regular Expression: >=
    - Operator greater than equal-to sign
  - NTEQLTO = 47
    - Regular Expression: !=
    - Operator not equal-to sign
  - L_PAREN = 52
    - Regular Expression: (
    - The token symbol to represent left parenthesis
  - R_PAREN = 53
    - Regular Expression: )
    - The token symbol to represent right parenthesis
  
### b) Define Production Rules
- Addition and Subtraction
![image](https://user-images.githubusercontent.com/97654476/205469823-d630fb2f-5a77-46b5-8c65-de412462a94f.png)
- Multiplication, Division and Modulo
![image](https://user-images.githubusercontent.com/97654476/205469838-6eede9d3-9185-46ef-930b-22bba533f7a4.png)
- Identification, Numbers, and Parenthesis
![image](https://user-images.githubusercontent.com/97654476/205597156-f98e1081-c5b3-43f7-8d57-ac30eb53db73.png)
- Assigning an ID
![image](https://user-images.githubusercontent.com/97654476/205469876-35e97f0a-d28a-44a0-9e50-36eb24ae876d.png)
- Less Than, Greater Than, Less Than or Equal To, Greater Than or Equal To, Not Equal, Equality
![image](https://user-images.githubusercontent.com/97654476/205469898-630e477b-b4f1-4657-b89c-d714732bd605.png)
- Statement(if, while, print, label, goto, let, input)
![image](https://user-images.githubusercontent.com/97654476/205469931-f3c9ba8a-4383-4ece-bd57-5ca3f2e94f67.png)
- If Statement
![image](https://user-images.githubusercontent.com/97654476/205469942-7f52f360-0d7d-4cb2-b442-42dea24bc5a4.png)
- While Loop
![image](https://user-images.githubusercontent.com/97654476/205469950-3831e4e6-0ddd-428e-8ba4-e72a804c27fb.png)
- Print statement
![image](https://user-images.githubusercontent.com/97654476/205469965-44fc8aac-b88a-479b-b624-da8ed7e997d8.png)
- Label
![image](https://user-images.githubusercontent.com/97654476/205469980-240a1561-1679-4169-a8ff-a4fcf7251f39.png)
- GOTO
![image](https://user-images.githubusercontent.com/97654476/205469989-6de363d0-a505-4cc2-b7aa-2c01e0994983.png)
- Input
![image](https://user-images.githubusercontent.com/97654476/205470009-a862fc36-8d0c-442e-9f79-1f05d9a05be7.png)
- Unary
![image](https://user-images.githubusercontent.com/97654476/205470015-5b8f7fbd-fa74-434d-93c3-eb4500de568e.png)
- Newline
![image](https://user-images.githubusercontent.com/97654476/205470020-4826b593-881c-4130-ba49-87c9cc7d781b.png)

### c) Show whether every rule set in your language conforms to the standard of an LL Grammar

- An LL grammar is a context-free grammar that can be parsed by an LL parser, which parses the input from left to right, and constructs a leftmost derivation of the sentence. Therefore, the rules that I have created conforms to the standard of an LL Grammar. This can be said because my rules are coded to be parsed left to right within my parser. All my rules are written to be read and interpreted in a left to right procedure. So, when an input stream is inserted, the parser reads the next-available symbol left to right, which can be considered a top-down parser for a restricted context-free language.

### d) Make sure it is not ambiguous grammar

- In this case, a grammar is said to be ambiguous if there exists more than one leftmost derivation or more than one parse tree for the given input string. Looking at my given production rules, they are written to where only one parse tree can be created. For example, my created rule for an addition or subtraction expression is written to where an input that follows that rule can be processed with a term, addition sign, and another term or a term, subtraction sign, and another term. Coming to show that it does not contain more than one left most derivation, because no other derivation can be produced from that rule. Since all my rules follow this same structure, it is unambiguous grammar.

### g) Test Files

- Text files can be found right underneath the Lexer.py, Parser.py and README.md files.
- 2 with no errors
  - Test1.txt
  - Test2.txt
- 1 with 5 lexical errors
  - Test4.txt
    - Line 9 has '&&'(and), which is not a token in the language
    - Line 9 has ':'(colon symbol) at the end of the line which is not recognized in the language
    - Line 10 has ';'(semicolon) at the end of the PRINT statement, which isnt needed at the end of a statement in the language
    - Line 11 has '||"(or), which is not a token
    - Line 12 has '^' trying to act as an exponent operator, which is not a token in the language
- 1 with 5 syntax errors
  - Test3.txt
    - Line 6 is missing the right parenthesis in order to close the parenthesized expression
    - Line 7 misspelling the "LET" keyword to assign a variable
    - Line 10 misspelling the "MEANTIME" keyword to initiate a while loop by using actual "WHILE"
    - Line 12 misspelling the "ENDMEANTIME" keyword to end a while loop in the langauge
    - Line 11 is missing another double quotation mark at the end of series of characters to properly take in a print statement

### h) Create a LR (1) parse table for your language

- LR (1) Grammar
<img width="450" alt="Screenshot 2022-12-05 at 4 12 46 AM" src="https://user-images.githubusercontent.com/97654476/205598768-ed319d66-fc6f-432e-896c-79de7732b939.png">

- LR Table
<img width="757" alt="Screenshot 2022-12-05 at 4 13 26 AM" src="https://user-images.githubusercontent.com/97654476/205598911-d3487f24-4802-4128-b3a0-3f511b63f04f.png">
<img width="739" alt="Screenshot 2022-12-05 at 4 13 52 AM" src="https://user-images.githubusercontent.com/97654476/205599007-2e21321b-760a-42d2-94db-e84853dd620a.png">
<img width="757" alt="Screenshot 2022-12-05 at 4 14 46 AM" src="https://user-images.githubusercontent.com/97654476/205599202-c961f80f-474a-44a4-a734-eb56694e3a52.png">

- 2 Correct Samples
<img width="1181" alt="Screenshot 2022-12-05 at 4 21 05 AM" src="https://user-images.githubusercontent.com/97654476/205600543-284b86ab-4dd0-4d4f-bbcb-5ec5ffbeffda.png">
<img width="1150" alt="Screenshot 2022-12-05 at 4 19 12 AM" src="https://user-images.githubusercontent.com/97654476/205600148-54a7d670-76bb-4610-b949-9b56c23bd3f1.png">

<img width="923" alt="Screenshot 2022-12-05 at 4 22 48 AM" src="https://user-images.githubusercontent.com/97654476/205600888-1125ccc8-94f7-4dc6-88e3-8617a477840a.png">
<img width="912" alt="Screenshot 2022-12-05 at 4 23 06 AM" src="https://user-images.githubusercontent.com/97654476/205600967-b4801331-210e-48ea-a9dc-90101c5e27cf.png">

- 2 Wrong Samples

In between steps 9 and 10 it is missing an operator token. Either it being a comparison operator or a regular addition or subtraction operator. It instead throws an error and cannot parse the "id - id" expression.
<img width="537" alt="Screenshot 2022-12-05 at 4 26 57 AM" src="https://user-images.githubusercontent.com/97654476/205601820-e1250dff-2b35-4f02-aefb-fd5a3b99a93a.png">

After step 17, it is missing either an id or num after the addition symbol. For this reason it cannot finish parsing and creating a proper tree.

<img width="548" alt="Screenshot 2022-12-05 at 4 30 31 AM" src="https://user-images.githubusercontent.com/97654476/205602546-20ebedbf-932c-43fc-b135-ffa98637fca7.png">
<img width="517" alt="Screenshot 2022-12-05 at 4 30 49 AM" src="https://user-images.githubusercontent.com/97654476/205602600-5e358603-a408-4437-90a9-e50fe0bf96c0.png">
