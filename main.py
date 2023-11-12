import sys
import getopt
import os

from game import run_game

HELP_MESSAGE = 'main.py -f <wordfile> -c <wordcount>'


def error(msg: str):
    print (msg)
    sys.exit(2)


def get_arguments():
    file_arg = ""
    count_arg = ""

    if (len(sys.argv) < 2):
        error (HELP_MESSAGE)

    try:
        opts, _ = getopt.getopt(sys.argv[1:],"hf:c:",["file=","count="])
    except getopt.GetoptError:
        error (HELP_MESSAGE)
    for opt, arg in opts:
        if opt == '-h':
            print (HELP_MESSAGE)
            sys.exit()
        elif opt in ("-f", "--file"):
            file_arg = arg
        elif opt in ("-c", "--count"):
            count_arg = arg

    return file_arg, count_arg


def process_arguments(file_arg, count_arg):
    if not os.path.isfile(file_arg):
        error ("File not found")

    count = 0
    try:
        count = int(count_arg)
        if count <= 0:
            raise ValueError
    except ValueError:
        error ("Word count must be a positive integer")
    
    return file_arg, count

if __name__ == "__main__":
   file_arg, count_arg = get_arguments()
   file, count = process_arguments(file_arg, count_arg)
   run_game(file, count)




    