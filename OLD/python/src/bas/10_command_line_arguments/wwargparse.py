# https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3.6/howto/argparse.html
import argparse

def return_min_value(l=[]):
    return min(l)

choises = ["min", 'max']

def make_parser():
    parser = argparse.ArgumentParser(prog="demo", description='Process some integers.')
    parser.add_argument('-i','--integers', metavar='N', type=int, nargs=1,
                        help='mode')
    parser.add_argument('--sort', dest='sort_mode', choices=choises, nargs=1,action='store')
    return parser
if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    print(args.integers)
    print(args.sort_mode)
