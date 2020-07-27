from textwrap import wrap

hex_table = "0123456789abcdef"
hex_table_binary = ["0000", "0001", "0010", "0011",
                    "0100", "0101", "0110", "0111",
                    "1000", "1001", "1010", "1011",
                    "1100", "1101", "1110", "1111"]

hex_encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def binary_xor_v2(string1, string2):
    if len(string1) == len(string2):
        return binary_xor(string1, string2)
    elif len(string1) > len(string2):
        return binary_xor_variable_length(string1, string2)
    else:
        return binary_xor_variable_length(string2, string1)

def binary_xor(string1, string2):
    string_final = ""
    i = 0
    for x in string1:
        string_final += "1" if x != string2[i] else "0"
        i+=1
    return string_final

def binary_xor_variable_length(string_longer, string_shorter):
    string_final = ""
    # if len(string_longer) % len(string_shorter) != 0:
    #     return "Wrong string lengths"
    string_longer_parts = wrap(string_longer, len(string_shorter))
    i = 0
    for string_longer_parts_char in string_longer_parts:
        i = 0
        for x in string_longer_parts_char:
            string_final += "1" if x != string_shorter[i] else "0"
            i+=1
    return string_final

def hex_to_binary(hex_string):
    hex_string_binary = ""
    for c in hex_string:
        pos = hex_table.find(c)
        hex_string_binary += hex_table_binary[pos]
    return hex_string_binary

def binary_to_hex(binary_string):
    hex_string = ""
    binary_string_table = wrap(binary_string, 4)
    for x in binary_string_table:
        y = int(x,2)
        hex_string += hex_table[y]
    return hex_string

hex_encoded_string_binary = hex_to_binary(hex_encoded_string)

def hex_to_ascii(hex_string):
    binary_string = hex_to_binary(hex_string)
    return binary_to_ascii(binary_string)

def binary_to_ascii(binary_string):
    ascii_string = ""
    binary_string_table = wrap(binary_string, 8)
    for x in binary_string_table:
        y = int(x,2)
        ascii_string += chr(y)
    return ascii_string

for i in range(0,129):
    # print(str(i) + " - " + binary_to_hex(binary_xor_v2(hex_encoded_string_binary, "{0:b}".format(i))))
    decoded_string_hex = binary_to_hex(binary_xor_v2(hex_encoded_string_binary,bin(i)[2:].zfill(8)))
    decoded_string_ascii = hex_to_ascii(decoded_string_hex)
    print(str(i) + " - " + decoded_string_hex + "     ---     " + decoded_string_ascii)

answer = 88
decoded_string_hex = binary_to_hex(binary_xor_v2(hex_encoded_string_binary,bin(answer)[2:].zfill(8)))
decoded_string_ascii = hex_to_ascii(decoded_string_hex)
print(hex_encoded_string + "     ---     " + decoded_string_ascii)