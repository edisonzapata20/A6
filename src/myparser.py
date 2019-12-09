from Objects.varObjects import VariableObject

class Parser(object):

    # Init with the tokens created from the lexer
    def __init__(self, tokens):
        # Global varibles
        # Holds all tokens that have been created by the lexer
        self.tokens = tokens
        # Holds the token index we are parsing at
        self.token_index = 0
        # Holds python executable string that make up all out code
        self.transpiled_code = ""

        self.values = []

    # Method to loop through tokens
    def parse(self):
        while self.token_index < len(self.tokens):

            # First slot of the pair [token type, word] ex. IDENTIFIER
            token_type = self.tokens[self.token_index][0]
            # Second slot of the pair [token type, word] ex. var
            token_value = self.tokens[self.token_index][1]

            # print(token_type, token_value)

            # This will trigger when a variable declaration token is found
            if token_type == "VAR_DECLARATION" and token_value == "var":
                self.parse_variable_declaration(self.tokens[self.token_index: len(self.tokens)])

            # Exits if there is no main statement
            if "MAIN_STATEMENT" not in self.tokens[0]:
                print("Error! No main() found")
                quit()

            # count = 0
            # if token_type == "PARENTHESIS":
            #     count += 1
            #
            # if self.token_index == len(self.tokens ) -1 and count % 2 != 0:
            #     print("Error, missing '{'")

            # Increment token index to loop to next token
            self.token_index += 1

        # Print transpiled code
        print(self.transpiled_code)
        return self.values

    # Method to parse a variableeclaration and create an object for it
    def parse_variable_declaration(self, token_stream):
        # Holds amount of tokens that we check that make up the variable declaration
        tokens_checked = 0

        name = ""
        operator = ""
        value = ""

        # Loop through token_stream to get all tokens and parse them
        for token in range(0, len(token_stream)):
            # Same concept as parse()
            btoken_type  = token_stream[tokens_checked][0]
            btoken_value = token_stream[tokens_checked][1]

            # If the ';' is found, break out of loop as we have parsed the variable declaration
            if btoken_type == "STATEMENT_END": break

            # # This will get the variable type. ex. var, let or const
            # if token == 0:
            #     print('Variable type: ' + btoken_value)

            # this will get the variable name and also perform error validation for invalid name
            elif token == 1 and btoken_type == "IDENTIFIER":
                # print('Variable name: ' + btoken_value)
                name = btoken_value
            elif token == 1 and btoken_type != "IDENTIFIER":
                print("Error: Invalid variable name '" + btoken_value + "'")
                quit()

            # This will get variable assignment operator e.g. = or += and also dows error validation
            elif token == 2 and btoken_type == "OPERATOR":
                # print('Assignment Operator: ' + btoken_value)
                operator = btoken_value
            elif token == 2 and btoken_type != "OPERATOR":
                print('ERROR! Missing or invalid assignment operator: ' + btoken_value + '. It should be \'=\'')
                quit()

            # This will get the variable value assigned
            elif token == 3 and btoken_type in ['STRING', 'INTEGER', 'IDENTIFIER']:
                # print('Variable value: ' + btoken_value)
                value = btoken_value
            elif token == 3 and btoken_type not in ['STRING', 'INTEGER', 'IDENTIFIER']:
                print("Invalid variable assignment value '" + btoken_value + "'.")
                quit()

            self.values.append(value)

            # Increase for every toke we check to add it to index to prevent checking tokens again
            tokens_checked += 1

        # Init VariableObject class
        varObj = VariableObject()
        # Call transpile method, which uses value we parsed above to create a Variable Declaration in python
        # and add it to the global transpiled_code variable
        self.transpiled_code += varObj.transpile(name, operator,value)

        # Increment token index by the amount of tokens we checked so we dont check them again
        self.token_index += tokens_checked
