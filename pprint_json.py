import json
import sys
import argparse


def load_data(filepath):
    with open(filepath) as json_file:
        data = json.loads(json_file.read())
    return data


def pretty_print_json(data):
    print(json.dumps(data, indent='  '))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file")
    namespace = parser.parse_args()
    try:
        data = load_data(namespace.json_file)
    except AttributeError:
        print("Please run the program with passing path to JSON file as argument.")
        sys.exit()
    pretty_print_json(data)
