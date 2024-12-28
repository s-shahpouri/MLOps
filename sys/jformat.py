import os
import sys
import json
import argparse

def formatter(string, sort_keys=True, indent=4):

    loaded_json = json.loads(string)

    return json.dumps(loaded_json,sort_keys=sort_keys, indent=indent)


def main(path, no_sort):
    if no_sort:
        sort_keys = False
    else:
        sort_keys = True

    with open(path, 'r') as _f:
        print(formatter(_f.read()), sort_keys = sort_keys)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "This is the jformat tool")
    parser.add_argument("--sort", action = 'store_true', help = 'set the sorting')
    args = parser.parse_args()
    print(args.sort)
    #main(sys.argv[-1], no_sort = False)


# To run in command line: python jformat.py -h