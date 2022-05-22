import re


# Madlib
# A command line application which takes advantage of Python's built-in
# capabilities for reading and writing files.  The application will:
# 1. read and parse a template Madlib file
# 2. prompt a user to submit words for each component
# 3. populate the template with the user provided words in the correct
# position
# 4. send the completed response to the user in the command line
# 5. write the completed text to a new file.

def welcome_msg():
    print("Welcome to Madlib CLI.  You will be asked to enter various types "
          "of words.  These will then be used to fill in the blanks of a "
          "story. \n")


def read_template(file_location):
    '''
    This function will read in a file that is a template for a Madlib.  A
    FileNotFoundError will be raised if the path is incorrect.
    '''
    with open(file_location) as file:
        data = file.read()
        #        data = data.strip() # Need to remove newline character.
        return data


def parse_template(madlib_story):
    '''
    This function will parse the template that was read in the read_template
    function.
    '''
#    sentence = "The {Adjective} brown fox jumped over the lazy {noun}."
    # print(sentence.split(' '))

    sentence = madlib_story

    # Find the period at the end of the sentence and move to its own array
    # element.
    pattern = r"[\.]"
    match = re.search(pattern, sentence)
    #    print(match)
    if match:
        # print('Found')
        sentence = sentence.replace(".", " .")
    else:
        print('Not found')

    newArr = sentence.split(' ')
    print(newArr)

    # array to hold words contained within { } for replacement.
    madlib = []
    wordsArr = []
    i = 0 # counter for indexing into the newArr for word replacement.

    # What is wanted by the test.
    # expected_stripped = "It was a {} and {} {}."
    # expected_parts = ("Adjective", "Adjective", "Noun")
    for word in newArr:
        # print(word)
        pattern = r"\{[A-z]+\}"
        wordMatch = re.search(pattern, word)
        if wordMatch:
            # print("True")
            # Remove the { } from the word and put in wordsArr.
            madlib = word.replace("{", "")
            madlib = madlib.replace("}", "")
            # print(madlib)
            wordsArr.append(madlib)
            # print(word)
            # print(newArr)
            newArr[i] = "{}"
        i += 1

    # print(madlib)
    print(wordsArr)
    print(newArr)

    # Re-assign wordsArr to parts.
    parts = tuple(wordsArr)

    # Convert newArr back to a string.
    stripped = ' '.join(newArr)
    stripped = stripped.replace(" .", ".")
    #print(stripped)
    return stripped, parts


def merge():
    pass


welcome_msg()
# parse_template()
