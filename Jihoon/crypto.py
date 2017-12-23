import string


def shift(text, key):
    """adds key to every letter in text, where a = 0, b = 1, etc.
    Wrap around if you reach the end: z + 1 = a.
    Don’t change non-letters.
    Preserve case"""
    answer = ''
    for character in text:
        if character.isupper():
            index = string.ascii_uppercase.index(character)
            new_index = (index + key) % 26
            answer += string.ascii_uppercase[new_index]
        elif character.islower():
            index = string.ascii_lowercase.index(character)
            new_index = (index + key) % 26
            answer += string.ascii_lowercase[new_index]
        else:
            answer += character
    return answer


# If you prefer substituting to building up, this is also possible.
def shift2(text, key):
    answer = list(text)
    for i, character in enumerate(text):
        if character.isupper():
            index = string.ascii_uppercase.index(character)
            new_index = (index + key) % 26
            answer[i] = string.ascii_uppercase[new_index]
        elif character.islower():
            index = string.ascii_lowercase.index(character)
            new_index = (index + key) % 26
            answer[i] = string.ascii_lowercase[new_index]
    return ''.join(answer)


def unshift(text, key):
    """subtracts key to every letter in text"""
    return shift(text, -key)


def vignere(text, key):
    """much like the shift cipher, but instead of adding a single number to all letters, a different number is added to each. Those numbers to add are selected by a the letters of a key word"""
    answer = ''
    for index_text, character in enumerate(text):
        if character.isupper():
            index_character = string.ascii_uppercase.index(character)
            letter_chosen = key[index_text % len(key)]
            amount_to_shift = string.ascii_lowercase.index(letter_chosen)
            new_index = (index_character + amount_to_shift) % 26
            answer += string.ascii_uppercase[new_index]
        elif character.islower():
            index_character = string.ascii_lowercase.index(character)
            letter_chosen = key[index_text % len(key)]
            amount_to_shift = string.ascii_lowercase.index(letter_chosen)
            new_index = (index_character + amount_to_shift) % 26
            answer += string.ascii_lowercase[new_index]
        else:
            answer += character
    return answer


def unvignere(text, key):
    """subtracts the key from text instead of adding it to the text"""
    answer = ''
    for index_text, character in enumerate(text):
        if character.isupper():
            index_character = string.ascii_uppercase.index(character)
            amount_to_shift = index_text % len(key)
            index_shift = string.ascii_lowercase.index(key[amount_to_shift])
            new_index = (index_character - index_shift) % 26
            answer += string.ascii_uppercase[new_index]
        elif character.islower():
            index_character = string.ascii_lowercase.index(character)
            amount_to_shift = index_text % len(key)
            index_shift = string.ascii_lowercase.index(key[amount_to_shift])
            new_index = (index_character - index_shift) % 26
            answer += string.ascii_lowercase[new_index]
        else:
            answer += character
    return answer


def interleave(text):
    """splits the string in half and return a string alternating letters from the first and second half"""
    middle_index = int((1 + len(text)) / 2)
    first_half = text[:middle_index]
    second_half = text[middle_index:]
    answer = ''
    for i in range(len(first_half)):
        answer += first_half[i]
        if i <= len(second_half) - 1:
            answer += second_half[i]
    return answer


def deinterleave(text):
    return text[0::2] + text[1::2]
