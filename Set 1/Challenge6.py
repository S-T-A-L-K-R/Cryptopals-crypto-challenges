# Break repeating-key XOR
# It is officially on, now.

# This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

# There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

# Decrypt it.

# Here's how:

#     Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
#     Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:

#     this is a test

#     and

#     wokka wokka!!!

#     is 37. Make sure your code agrees before you proceed.
#     For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
#     The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
#     Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
#     Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
#     Solve each block as if it was single-character XOR. You already have code to do this.
#     For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

# This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.
# No, that's not a mistake.

# We get more tech support questions for this challenge than any of the other ones. We promise, there aren't any blatant errors in this text. In particular: the "wokka wokka!!!" edit distance really is 37.

from textwrap import wrap

hex_table = "0123456789abcdef"
hex_table_binary = ["0000", "0001", "0010", "0011",
                    "0100", "0101", "0110", "0111",
                    "1000", "1001", "1010", "1011",
                    "1100", "1101", "1110", "1111"]

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

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def check_keysize(string1, string2):
    string1_binary = ascii_to_binary(string1)
    string2_binary = ascii_to_binary(string2)

    string1_binary_list = chunkstring(string1_binary, 8)
    string2_binary_list = chunkstring(string2_binary, 8)

    print(type(string1_binary_list))
    print(string2_binary_list)

keysize = 2
sentence1 = "this is a test"
sentence2 = "wokka wokka!!!"
check_keysize(sentence1, sentence2)