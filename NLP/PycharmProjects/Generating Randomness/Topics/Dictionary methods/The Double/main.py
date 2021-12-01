# put your python code here
double_alphabet = {}
a_num = 97
z_num = 122
for i in range(a_num, z_num + 1, 1):
    double_alphabet[chr(i)] = chr(i) + chr(i)
