import random

minimal_length = 100
start_random_str_len = 3
allowed_symbols = ["0", "1"]
triads = ["000", "001", "010", "011", "100", "101", "110", "111"]


def print_user_stat(stat_data: dict):
    # debug function
    print("triads,0,0 prob, 1, 1 prob ")
    for key, value in stat_data.items():
        print("{0},{1},{2},{3},{4}".format(key
              , value["0"]
              , value["0_prob"]
              , value["1"]
              , value["1_prob"]))


def predict_next(triad_list: list, stat_data):
    next_symbol = ""
    triad = "".join(triad_list)
    if stat_data[triad]["0_prob"] > stat_data[triad]["1_prob"]:
        next_symbol = "0"
    elif stat_data[triad]["0_prob"] < stat_data[triad]["1_prob"]:
        next_symbol = "1"
    else:
        next_symbol = str(random.randint(0, 1))

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


def update_user_statistic(user_string, stat_container: dict):
    user_str_len = len(user_string)

    for i in range(0, user_str_len - 2, 1):
        peace_of_string = user_string[i:i + 4]
        if len(peace_of_string) == 4:
            triad_str = peace_of_string[0:3]
            next_symbol = peace_of_string[3]
            stat_container[triad_str][next_symbol] = stat_container[triad_str][next_symbol] + 1

    calc_probability(stat_container)


def prepare_statistic():
    user_random_str = ""

    triads_dic = initialize_stat_container()

    print("Please give AI some data to learn...")

    while True:
        user_random_str_part = input("Print a random string containing 0 or 1:")

        for symbol in user_random_str_part:
            if symbol in allowed_symbols:
                user_random_str += symbol

        user_str_len = len(user_random_str)
        if user_str_len < minimal_length:
            print("Current data length is {0}, {1} symbols left".format(user_str_len
                                                                        , minimal_length - user_str_len))
            continue
        else:
            break

    print("Final data string:")
    print(user_random_str)

    """for i in range(0, user_str_len - 2, 1):
        peace_of_string = user_random_str[i:i + 4]
        if len(peace_of_string) == 4:
            triad_str = peace_of_string[0:3]
            next_symbol = peace_of_string[3]
            triads_dic[triad_str][next_symbol] = triads_dic[triad_str][next_symbol] + 1

    calc_probability(triads_dic)"""

    update_user_statistic(user_random_str, triads_dic)

    return triads_dic


def print_rules(player_balance):
    print("""You have ${0}. Every time the system successfully predicts your next press, you lose $1.
    Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!""".format(str(player_balance)))


def start_game():

    player_statistic = prepare_statistic()
    # print_user_stat(user_statistic)
    player_balance = 1000

    print_rules(player_balance)

    while True:

        print("Print a random string containing 0 or 1:")
        player_string = input()

        if player_string == "enough":
            # end game
            break

        player_string_len = len(player_string)
        player_string_symbols = [char for char in player_string if char in allowed_symbols]

        if player_string_len != len(player_string_symbols):
            # Wrong string. Try again
            continue

        predicted_symbols = [char for char in random_string()]
        guessed_amount = 0
        check_len = player_string_len - start_random_str_len

        for i in range(3, player_string_len, 1):
            next_symbol = predict_next(player_string_symbols[i - 3:i], player_statistic)
            predicted_symbols.append(next_symbol)
            if next_symbol == player_string[i]:
                guessed_amount += 1

        update_user_statistic(player_string, player_statistic)

        print("prediction:")
        print("".join(predicted_symbols))

        print("Computer guessed right {guessed} out of {length} symbols ({rate} %)".format(guessed=str(guessed_amount)
              , length=check_len
              , rate=round(100 * guessed_amount / check_len, 2) if check_len > 0 else 0))

        # Result:               Player won              Computer guessed
        player_balance += (check_len - guessed_amount) - guessed_amount
        print("Your balance is now ${0}".format(str(player_balance)))

    print("Game over!")


start_game()
