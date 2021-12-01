minimal_length = 100
user_random_str = ""
allowed_symbols = ["0", "1"]
triads = ["000", "001", "010", "011", "100", "101", "110", "111"]
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

triads_dic = dict.fromkeys(triads)
for i in triads:
    triads_dic[i] = {"0": 0, "1": 0}

# triads_dic = dict.fromkeys(["000", "001", "010", "011", "100", "101", "110", "111"], {"0": 0, "1": 0})

for i in range(0, user_str_len - 2, 1):
    peace_of_string = user_random_str[i:i + 4]
    if len(peace_of_string) == 4:
        triad_str = peace_of_string[0:3]
        next_symbol = peace_of_string[3]
        triads_dic[triad_str][next_symbol] = triads_dic[triad_str][next_symbol] + 1

for key, value in triads_dic.items():
    print(key+": "+str(value["0"])+","+str(value["1"]))



