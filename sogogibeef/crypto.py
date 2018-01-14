alphabet = 'abcdefghijklmnopqrstuvwxyz'


def index_to_letter(index):
    if index > 25:
        index = index - 26
    return alphabet[index]


def letter_to_index(letter):
    return alphabet.index(letter)


def is_letter(letter):
    return letter.lower() in alphabet


def shift(text, key):
    """
    Encrypt plain_text using Caesar Cipher method
    :param text: text to be encrypted
    :param key: key to be used for encryption
    :return: encrypted plain_text
    """
    ans = ''
    for letter in text:
        if is_letter(letter):
            if letter.isupper():
                letter = letter.lower()
                ans = ans + index_to_letter(letter_to_index(letter) + key).upper()
            else:
                ans = ans + index_to_letter(letter_to_index(letter) + key)
        else:
            ans = ans + letter

    return ans


def unshift(text, key):
    """
    Decipher text encrypted with Caesar Cipher
    :param text : text to be decrypted
    :param key: key to be used for decryption
    :return: decrypted plain text
    """
    return shift(text, -key)


def vigenere(text, key):
    """
    Encrypt text using Vigenere method
    :param text: text to be encrypted
    :param key: key to be used for encryption
    :return: encrypted text
    """
    ans = ''
    i = 0
    for letter in text:
        if is_letter(letter):
            j = letter_to_index(key[i % len(key)])
            if letter.isupper():
                letter = letter.lower()
                ans = ans + index_to_letter(letter_to_index(letter) + j).upper()
            else:
                ans = ans + index_to_letter(letter_to_index(letter) + j)
        else:
            ans = ans + letter
        i = i + 1
    return ans


def unvigenere(text, key):
    """
    Decrypt text encrypted with Vigenere method
    :param text : text to be decrypted
    :param key: key to be used for decryption
    :return: decrypted plain text
    """
    ans = ''
    i = 0
    for letter in text:
        if is_letter(letter):
            j = letter_to_index(key[i % len(key)])
            # using text.index(letter) returned wrong value, as it returned index of first instance of the letter
            if letter.isupper():
                letter = letter.lower()
                ans = ans + index_to_letter(letter_to_index(letter) - j).upper()
            else:
                ans = ans + index_to_letter(letter_to_index(letter) - j)
        else:
            ans = ans + letter
        i = i + 1
    return ans


def interleave(text):
    """
    Encrypt text using interleave method
    :param text: text to be encrypted
    :return: encrypted text
    """
    text_length = len(text)
    middle_index = int(text_length / 2)
    ans = ''
    if text_length % 2 == 0:
        first_half = text[:middle_index]
        second_half = text[middle_index:]
        for i in range(len(second_half)):
            ans = ans + first_half[i] + second_half[i]

    else:
        first_half = text[:middle_index + 1]
        second_half = text[middle_index + 1:]
        for i in range(len(second_half)):
            ans = ans + first_half[i] + second_half[i]
        ans = ans + first_half[-1]

    return ans


def deinterleave(text):
    """
    Decrypt text encrypted with interleave method
    :param text: text to be decrypted
    :return: decrypted text
    """
    return text[0::2] + text[1::2]


print(interleave('water'))
