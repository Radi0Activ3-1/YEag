'''
Homework20
Name:
github link: 
'''

def convert_to_ascii(text):
    """
    Converts a given string into its ASCII equivalent.

    Parameters:
    text (str): A character or string.

    Returns:
    If the input is a character, output the ASCII value.
    If the input is a string of characters, output a list of ASCII values.
    """
    if len(text) == 1:
        return ord(text)
    return [ord(char) for char in text]

def filter_non_ascii(text):
    """
    Filters out all non-ASCII characters from a given string.

    Parameters:
    text (str): A string that may contain non-ASCII characters.

    Returns:
    A new string containing only the ASCII characters from the input.
    """
    return ''.join(char for char in text if ord(char) < 128)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest20.py'))