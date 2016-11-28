import json
import sys
import argparse


def load_json_data(filepath):
    with open(filepath) as json_file:
        json_content = json.loads(json_file.read())
    return json_content


def pretty_print_json(json_content):
    print(json.dumps(json_content, indent='  '))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file")
    namespace = parser.parse_args()
    try:
        json_content = load_json_data(namespace.json_file)
    except AttributeError:
        print("Please run the program with passing path to JSON file as argument.")
        sys.exit()
    pretty_print_json(json_content)
