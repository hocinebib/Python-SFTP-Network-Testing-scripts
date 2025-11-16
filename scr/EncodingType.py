#!/usr/bin/python3

"""

a script to get file encoding and change encoding

use exemple :

    python3 EncodingType.py action filename --encoding new_encoding_type

"""

import argparse
from charset_normalizer import from_path

def file_encoding(filename):
    """
    function to get file encoding
    """
    return(from_path(filename).best().encoding)

def new_encoding(filename, encoding):
    """
    function to write a new file with the chosen encoding
    """
    result = str(from_path(filename).best())
    with open(filename.split('.')[0]+"_new."+filename.split('.')[1], "w", encoding=encoding) as f:
        f.write(result)

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("action", choices=[1, 2, 3], help="1 to get file encoding | 2 to change file format | 3 to do both", type=int)
    PARSER.add_argument("filename", help="the file that the encoding is needed for", type=str)
    PARSER.add_argument("--encoding", choices=["ascii", "utf-8", "latin-1", "cp037", "cp500"], help="Target encoding to use, available options => ascii | utf-8 | latin-1 | cp037 | cp500", type=str)

    ARGS = PARSER.parse_args()

    if ARGS.action != 1 and ARGS.encoding is None:
        PARSER.error("--encoding is required if action 2 or 3 are chosen")
    else:
        ACTION = ARGS.action
        FILENAME = ARGS.filename
        ENCODING = ARGS.encoding

        if ACTION ==1:
            print("The encoding of the file "+FILENAME+" is "+file_encoding(FILENAME))
        elif ACTION == 2:
            new_encoding(FILENAME, ENCODING)
            print("New file "+FILENAME.split('.')[0]+"_new."+FILENAME.split('.')[1]+" created with "+ENCODING+" encoding")
        elif 3:
            print("The encoding of the file "+FILENAME+" is "+file_encoding(FILENAME))
            new_encoding(FILENAME, ENCODING)
            print("New file "+FILENAME.split('.')[0]+"_new."+FILENAME.split('.')[1]+" created with "+ENCODING+" encoding")
