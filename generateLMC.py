# Import the os module
import os

# Create a function to lex a given file
def lex(fName):

    # Check that the file exists
    if not os.path.isfile(fName):
        print("'{}' was not found\nCheck the file name and try again".format(fName))
        return

    # Fetch the data from the file
    data = open(fName,"r").read()
    print(data)

if __name__ == "__main__":
    lex("main.sc")
