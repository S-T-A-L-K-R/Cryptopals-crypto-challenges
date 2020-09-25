# Implement repeating-key XOR

# Here is the opening stanza of an important work of the English language:

# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal

# Encrypt it, under the key "ICE", using repeating-key XOR.

# In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

# It should come out to:

# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
# a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

# Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.


from textwrap import wrap

hex_table = "0123456789abcdef"
hex_table_binary = ["0000", "0001", "0010", "0011",
                    "0100", "0101", "0110", "0111",
                    "1000", "1001", "1010", "1011",
                    "1100", "1101", "1110", "1111"]

sentence = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
sentence2 = """x
fukn
d"""
key = "ICE"
expected_output = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

# sentence to binary
# xor sentence
# compare with output
# todo - ignore "enter" while encoding/decoding


def ascii_to_hex(ascii_string):
    binary_string = ascii_to_binary(ascii_string)
    return binary_to_hex(binary_string)

def ascii_to_binary(ascii_string):
    binary_string = ''
    for x in ascii_string:
        binary_string += bin(ord(x))[2:].zfill(8)
    return binary_string


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

def binary_to_hex(binary_string):
    hex_string = ""
    binary_string_table = wrap(binary_string, 4)
    for x in binary_string_table:
        y = int(x,2)
        hex_string += hex_table[y]
    return hex_string

xored_sentence = binary_to_hex(binary_xor_v2(ascii_to_binary(sentence2), ascii_to_binary(key)))
print(xored_sentence)
print(expected_output)
print(xored_sentence == expected_output)