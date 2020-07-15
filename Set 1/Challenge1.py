import binascii
from textwrap import wrap

base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
hex_table = "0123456789abcdef"
hex_table_binary = ["0000", "0001", "0010", "0011",
                    "0100", "0101", "0110", "0111",
                    "1000", "1001", "1010", "1011",
                    "1100", "1101", "1110", "1111"]

def hex_to_base64(hex_string):
    # base64 - 6 bytes
    hex_string_binary = hex_to_binary(hex_string)
    return binary_to_base64(hex_string_binary)

def hex_to_binary(hex_string):
    hex_string_binary = ""
    for c in hex_string:
        pos = hex_table.find(c)
        hex_string_binary += hex_table_binary[pos]
    return hex_string_binary

def binary_to_base64(binary_string):
    # for substring in binary_string:
    #     print(substring)
    base64_string = ""
    binary_string_table = wrap(binary_string, 6)
    for x in binary_string_table:
        y = int(x,2)
        base64_string += base64_table[y]
    return base64_string

test_hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
test_answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
answer = hex_to_base64(test_hex_string)
print("Hex string - " + test_hex_string)
print("Expected answer - " + test_answer)
print("Your answer - " + answer)
if test_answer == answer:
    print("Good job!")
else:
    print("not good job :/")
    print("try again")