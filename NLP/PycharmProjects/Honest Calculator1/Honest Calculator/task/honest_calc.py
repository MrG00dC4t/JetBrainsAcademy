# write your code here
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0.0

def is_number(num_str: str) -> bool:
    it_is_number = False
    try:
        if is_float(num_str):
            number = float(num_str)
        else:
            number = int(num_str)
        it_is_number = True
    except:
        it_is_number = False
    return it_is_number


def is_float(num_str: str) -> bool:
    it_is_float = False
    if "." in num_str:
        it_is_float = True
    return it_is_float


def check(v1, v2, v3) -> int:
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)

    return 0


def is_one_digit(v) -> bool:
    output = False
    if v > -10 and v < 10 and int(v) == v:
        output = True
    else:
        output = False
    return output


def get_number(num_str: str):
    number = 0
    if is_float(num_str):
        number = float(num_str)
    else:
        number = int(num_str)

    return number


def get_answer(msg_index):
    msg_text = globals()["msg_"+str(msg_index)]
    return input(msg_text)


def store_result(calc_result) -> int:
    global memory
    if is_one_digit(calc_result):
        msg_index = 10
        while True:
            answer = get_answer(msg_index)
            if not (answer == "y" or answer == "n"):
                continue

            if answer == "y":
                if msg_index < 12:
                    msg_index = msg_index + 1
                    continue
                else:
                    memory = calc_result
                    break

            if answer == "n":
                break
    else:
        memory = calc_result

    return 0


while True:

    calc = input(msg_0)
    x, oper, y = calc.split()

    x_is_number = is_number(x)
    y_is_number = is_number(y)

    if x_is_number:
        x_num = get_number(x)
    elif x == "M":
        x_num = memory
        x_is_number = True

    if y_is_number:
        y_num = get_number(y)
    elif y == "M":
        y_num = memory
        y_is_number = True

    if not (x_is_number and y_is_number):
        print(msg_1)
        continue

    if oper == "+" or oper == "-" or oper == "*" or oper == "/":
        check(x_num, y_num, oper)
    else:
        print(msg_2)
        continue

    result: float = 0
    if oper == "+":
        result = float(x_num + y_num)
    elif oper == "-":
        result = float(x_num - y_num)
    elif oper == "*":
        result = float(x_num * y_num)
    elif oper == "/" and y_num != 0:
        result = float(x_num / y_num)
    else:
        print(msg_3)
        continue

    print(result)

    stop_calc = False

    while True:

        answer_msg_4 = input(msg_4)

        if not (answer_msg_4 == "y" or answer_msg_4 == "n"):
            continue

        if answer_msg_4 == "y":
            store_result(result)

        break

    while True:

        answer_msg_5 = input(msg_5)

        if not (answer_msg_5 == "y" or answer_msg_5 == "n"):
            continue

        if answer_msg_5 == "n":
            stop_calc = True

        break

    if stop_calc:
        break

