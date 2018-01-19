import string

alphabet = string.ascii_lowercase


def index_to_letter(index):
    index %= 26
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
                ans += index_to_letter(letter_to_index(letter) + key).upper()
            else:
                ans += index_to_letter(letter_to_index(letter) + key)
        else:
            ans += letter

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
    for counter, letter in enumerate(text):
        if is_letter(letter):
            index_to_move = letter_to_index(key[counter % len(key)])
            if letter.isupper():
                letter = letter.lower()
                ans += index_to_letter(letter_to_index(letter) + index_to_move).upper()
            else:
                ans += index_to_letter(letter_to_index(letter) + index_to_move)
        else:
            ans += letter
    return ans


def unvigenere(text, key):
    """
    Decrypt text encrypted with Vigenere method
    :param text : text to be decrypted
    :param key: key to be used for decryption
    :return: decrypted plain text
    """
    ans = ''
    for counter, letter in enumerate(text):
        if is_letter(letter):
            index_to_move = letter_to_index(key[counter % len(key)])
            if letter.isupper():
                letter = letter.lower()
                ans += index_to_letter(letter_to_index(letter) - index_to_move).upper()
            else:
                ans += index_to_letter(letter_to_index(letter) - index_to_move)
        else:
            ans += letter

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
            ans += first_half[i] + second_half[i]

    else:
        first_half = text[:middle_index + 1]
        second_half = text[middle_index + 1:]
        for i in range(len(second_half)):
            ans += first_half[i] + second_half[i]
        ans += first_half[-1]

    return ans


def deinterleave(text):
    """
    Decrypt text encrypted with interleave method
    :param text: text to be decrypted
    :return: decrypted text
    """
    return text[0::2] + text[1::2]
