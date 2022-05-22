import re


# Madlib
# A command line application which takes advantage of Python's built-in
# capabilities for reading and writing files.  The application will:
# 1. read and parse a template Madlib file
# 2. populate the template with the user provided words in the correct
# position
# 3. send the completed response to the user in the command line
# 4. write the completed text to a new file.

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

    sentence = madlib_story

    # Find the period at the end of the sentence and move to its own array
    # element.
    pattern = r"[\.]"
    match = re.search(pattern, sentence)
    if match:
        sentence = sentence.replace(".", " .")
    else:
        print('Not found')

    newArr = sentence.split(' ')
    print(newArr)

    # array to hold words contained within { } for replacement.
    madlib = []
    wordsArr = []
    i = 0 # counter for indexing into the newArr for word replacement.

    # Find the words in curly braces and separate the words from the braces. 
    # Put the word into a new array.
    for word in newArr:
        pattern = r"\{[A-z]+\}"
        wordMatch = re.search(pattern, word)
        if wordMatch:
            # Remove the { } from the word and put in wordsArr.
            madlib = word.replace("{", "")
            madlib = madlib.replace("}", "")
            wordsArr.append(madlib)
            newArr[i] = "{}"
        i += 1

    # Re-assign wordsArr to parts.
    parts = tuple(wordsArr)

    # Convert newArr back to a string.
    stripped = ' '.join(newArr)
    stripped = stripped.replace(" .", ".")
    return stripped, parts


def merge(story, userInput):
    """
    This function will combine user input with the given story and return it.
    """
    completedStory = story.format(*userInput)
    return(completedStory)


welcome_msg()
