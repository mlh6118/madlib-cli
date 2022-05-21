# Madlib
# A command line application which takes advantage of Python's built-in
# capabilities for reading and writing files.  The application will:
# 1. read and parse a template Madlib file
# 2. prompt a user to submit words for each component
# 3. populate the tempate with the user provided words in the correct
# position
# 4. send the completed response to the user in the command line
# 5. write the completed text to a new file.

def welcome_msg():
    print("Welcome to Madlib CLI.  You will be asked to enter various types "
          "of words.  These will then be used to fill in the blanks of a "
          "story. \n")

def read_template(file_location):
    with open(file_location) as file:
        data = file.read()
#        data = data.strip() # Need to remove newline character.
        return data

def parse_template():
    pass

def merge():
    pass

welcome_msg()
