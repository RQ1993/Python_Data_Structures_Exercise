def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
      Auden
      Ezra
      Fluffy
      Meowsley

    This should work:

        >>> read_file_list("cats")
       -Auden
       -Ezra
       -Fluffy
       -Meowsley

    It will raise an error if the file cannot be found.



    """

def read_file_list(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Print each line with a "-" before it
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found")

# Test the function with a sample file
read_file_list("cats")


def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle



        
 def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.


    def read_file_list(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Print each line with a "-" before it
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found")

# Test the function with a sample file
read_file_list("dogs")


    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!