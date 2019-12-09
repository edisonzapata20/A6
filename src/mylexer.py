import re #Regular expression library

class Lexer(object):

    # Serves as "constructor"
    #init class with source_code = content in main()
    def __init__(self, source_code):
        self.source_code = source_code

    #turns source code into tokens
    @property
    def tokenize(self):
        #where all the tokens created by the lexer will be stored
        tokens = []

        #create a word list of the source code
        source_code = self.source_code.split()
        #re.split(source_code, patter)
        #print(source_code)

        #keep track of word index we are at in the source_code
        source_index = 0


        #loop through source_code word list and print every word
        while source_index < len(source_code):

            #Cada palabra leida
            word = source_code[source_index]
            print(word)

            #Recognoze a variable and create a token for it
            if word == "var":
                #token which holds a list: [token type, word]
                tokens.append(["VAR_DECLARATION", word])

            #Recognize an integer ad create an INTEGER token for it
            elif re.match('[0-9]', word):
                # Do not include ':' in token
                if word[len(word) - 1] == ";":
                    tokens.append(['INTEGER', word[0:len(word) - 1]])
                else:
                    tokens.append(['INTEGER', word])

            # Recognize a string if a word is between ""
            elif word[0] == "\"" and word[len(word) - 2] == "\"":
                # Do not include ';' in token
                if word[len(word) - 1] == ";":
                    tokens.append(['STRING', word[0:len(word) - 1]])
                else:
                    tokens.append(['STRING', word])

            #Recognize operators and create an OPERATOR token for it
            elif word in "=/*=-+":
                tokens.append(['OPERATOR', word])

            # Recognize corchetes
            elif word in "{}":
                tokens.append(['PARENTHESIS', word])

            elif word == "main()":
                tokens.append(['MAIN_STATEMENT', word])

            # Recognize method
            elif re.match('[a-z]*[A-Z]*[a-z]*\([a-z]+[A-Z]* ?,? ?[a-z]*?[A-Z]*?\)' , word):
                # Do not include ';' in token
                if word[len(word) - 1] == ";":
                    tokens.append(['METHOD', word[0:len(word) - 1]])
                else:
                    tokens.append(['METHOD', word])

            #This will recognize word and create an identifier token for it
            elif (re.match('[a-z]', word) or re.match('[A-Z]', word)) and word != "main()":
                # Do not include ':' in token
                if word[len(word) - 1] == ";":
                    tokens.append(['IDENTIFIER', word[0:len(word) - 1]])
                else:
                    tokens.append(['IDENTIFIER', word])


            # If a semicolon (;) is found at the end of a word, add a STATEMENT_END token
            if word[len(word) - 1] == ";":
                tokens.append(['STATEMENT_END', ';'])


            #increase word index
            source_index += 1

        print(tokens)

        # return created tokens
        return tokens


