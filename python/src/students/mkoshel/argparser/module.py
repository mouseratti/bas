import argparse


parser = argparse.ArgumentParser(prog="SUPERMEGASCRIPT")
parser.add_argument("filename", type=str, metavar="FILENAME")
parser.add_argument("-m", '--most_popular', type=int, action='store')


args = parser.parse_args()
print(args.filename)