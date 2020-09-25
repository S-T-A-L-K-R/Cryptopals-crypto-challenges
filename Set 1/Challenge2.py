# Fixed XOR

# Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c

# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965

# ... should produce:
# 746865206b696420646f6e277420706c6179



from textwrap import wrap

hex_table = "0123456789abcdef"
hex_table_binary = ["0000", "0001", "0010", "0011",
                    "0100", "0101", "0110", "0111",
                    "1000", "1001", "1010", "1011",
                    "1100", "1101", "1110", "1111"]

def hex_to_binary(hex_string):
    hex_string_binary = ""
    for c in hex_string:
        pos = hex_table.find(c)
        hex_string_binary += hex_table_binary[pos]
    return hex_string_binary


def binary_xor(string1, string2):
    string_final = ""
    i = 0
    for x in string1:
        string_final += "1" if x != string2[i] else "0"
        i+=1
    return string_final

def binary_to_hex(binary_string):
    hex_string = ""
    binary_string_table = wrap(binary_string, 4)
    for x in binary_string_table:
        y = int(x,2)
        hex_string += hex_table[y]
    return hex_string


string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"
string_answer = "746865206b696420646f6e277420706c6179"

my_answer = binary_to_hex(binary_xor(hex_to_binary(string1), hex_to_binary(string2)))
print('Answer - ' + string_answer)
print('Your answer - ' + my_answer)

print('Binary answer -      ' + hex_to_binary(string_answer))
print('Your binary answer - ' + hex_to_binary(my_answer))

if string_answer == my_answer:
    print("Good job!")
else:
    print("not good job :/")
    print("try again")