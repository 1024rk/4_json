import json
import sys


def load_data(filepath):
    with open(filepath) as json_file:
        data = json.loads(json_file.read())
    return data


def pretty_print_json(data, indent, dict_key, comma):
    """Recursive process JSON content.
    
    Positional arguments:
    data -- current processing data
    indent -- current indentation level
    dict_key -- current dictionary item key (if current item is
    dictionary value, else None)
    comma -- boolean shows need for comma at the end of the string
    
    """
    if isinstance(data, list):
        print("{}{}[".format(
            ' '*indent_value*indent,
            '"{}": '.format(dict_key) if dict_key else ''))
        while len(data) > 1:
            pretty_print_json(data.pop(0), indent+1, None, True)
        pretty_print_json(data.pop(0), indent+1, None, False)
        print("{}]{}".format(' '*indent_value*indent, ',' if comma else ''))
    elif isinstance(data, dict):
        print("{}{}{{".format(
            ' '*indent_value*indent,
            '"{}": '.format(dict_key) if dict_key else '',))
        keys_list = list(data.keys())
        for key in keys_list:
            if len(data) > 1:
                pretty_print_json(data.pop(key), indent+1, key, True)
            else:
                pretty_print_json(data.pop(key), indent+1, key, False)
        print("{}}}{}".format(' '*indent_value*indent, ',' if comma else ''))
    elif isinstance(data, str):
        print('{}{}"{}"{}'.format(
            ' '*indent_value*indent,
            '"{}": '.format(dict_key) if dict_key else '',
            data, ',' if comma else ''))
    else:
        print("{}{}{}{}".format(
            ' '*indent_value*indent,
            '"{}": '.format(dict_key) if dict_key else '',
            data, ',' if comma else ''))


if __name__ == '__main__':
    filepath = sys.argv[1]
    try:
        indent_value = int(sys.argv[2])
    except IndexError:
        indent_value = 4
    except ValueError:
        raise RuntimeError("Indentation level must be a number")
    data = load_data(filepath)
    pretty_print_json(data, 0, None, False)
