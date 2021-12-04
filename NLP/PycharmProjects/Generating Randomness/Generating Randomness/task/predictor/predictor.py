import random
from unittest.mock import patch
from unittest import TestCase

minimal_length = 100
start_random_str_len = 3
allowed_symbols = ["0", "1"]
triads = ["000", "001", "010", "011", "100", "101", "110", "111"]


def predict_next(triad_list: list, stat_data):
    next_symbol = ""
    triad = "".join(triad_list)
    if stat_data[triad]["0_prob"] > stat_data[triad]["1_prob"]:
        next_symbol = "0"
    else:
        next_symbol = "1"
    return next_symbol


def random_string():
    result = ""
    for i in range(1, start_random_str_len + 1, 1):
        result += str(random.randint(0, 1))
    return result


def calc_probability(stat_data):
    for key, value in stat_data.items():
        b = value["0"] + value["1"]
        if b != 0:
            value["1_prob"] = int((value["1"] / b) * 100)
            value["0_prob"] = 100 - value["1_prob"]
        else:
            value["1_prob"] = 1
            value["0_prob"] = 0


def initialize_stat_container():

    stat_container = dict.fromkeys(triads)
    for i in triads:
        stat_container[i] = {"0": 0, "1": 0, "0_prob": 0, "1_prob": 0}
    return stat_container


def prepare_statistic():
    user_random_str = ""

    triads_dic = initialize_stat_container()

    while True:
        user_random_str_part = input("Print a random string containing 0 or 1:")

        for symbol in user_random_str_part:
            if symbol in allowed_symbols:
                user_random_str += symbol

        user_str_len = len(user_random_str)
        if user_str_len < minimal_length:
            print("Current data length is {0}, {1} symbols left".format(user_str_len, minimal_length - user_str_len))
            continue
        else:
            break

    print("Final data string:")
    print(user_random_str)

    for i in range(0, user_str_len - 2, 1):
        peace_of_string = user_random_str[i:i + 4]
        if len(peace_of_string) == 4:
            triad_str = peace_of_string[0:3]
            next_symbol = peace_of_string[3]
            triads_dic[triad_str][next_symbol] = triads_dic[triad_str][next_symbol] + 1

    calc_probability(triads_dic)

    return triads_dic


def user_input_prediction():

    user_statistic = prepare_statistic()

    test_string = input("Please enter a test string containing 0 or 1:")
    test_string_len = len(test_string)

    # random_string = random_string()
    predicted_symbols = [char for char in random_string()]
    guessed_amount = 0
    check_len = test_string_len - start_random_str_len

    for i in range(3, test_string_len, 1):
        next_symbol = predict_next(predicted_symbols[i - 3:i], user_statistic)
        predicted_symbols.append(next_symbol)
        if next_symbol == test_string[i]:
            guessed_amount += 1

    print("prediction:")
    print("".join(predicted_symbols))

    print("Computer guessed right {guessed} out of {length} symbols ({rate} %)".format(guessed=str(guessed_amount)
          , length=check_len
          , rate=100 * round(guessed_amount / check_len, 2) if check_len > 0 else 0))


user_input_prediction()
