#!/usr/bin/python3

"""

a script for personal use

use exemple :

    python3 remote_folder.py csv_file

"""

import argparse
import pandas as pd

def get_dir(chaincar):
    return chaincar.split("generique")[1].split("ftp")[1].split("/")[1]+'/'+chaincar.split("generique")[1].split("/")[1]+'/'+'/'.join(chaincar.split("generique")[1].split("ftp")[1].split("/")[2:])


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("file", help="the csv file with the data", type=str)

    ARGS = PARSER.parse_args()

    FILE = ARGS.file

    DF = pd.read_csv(FILE, sep=";", names = ["IDF", "directory"])

    DF["directory"]=DF["directory"].apply(get_dir)

    print(DF)
