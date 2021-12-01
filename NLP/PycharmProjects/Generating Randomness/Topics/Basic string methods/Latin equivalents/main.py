name = input()
change_dict = {"é": "e", "ë": "e", "á": "a", "å": "a", "œ": "oe", "æ": "ae"}


def normalize(name_str):
    new_name = name_str
    for old, new in change_dict.items():
        new_name = new_name.replace(old, new)
    return new_name

print(normalize(name))
