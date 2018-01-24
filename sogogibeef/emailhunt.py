import re
# () group
# | match one of many expressions
# ()? optional matching
# ()* zero or more matching
# ()+ one or more matching
# (){integer} specific repetition matching
# (){}? nongreedy matching - shortest possible / greedy : longest possible
# findall() return strings of every match in the searched string
# \d : numeric digit 0-9
# \D : character that is not a numeric digit form 0-9
# \w : letter / digit / underscore
# \s : space, tab, newline
# \S : not space, tab, newline
# . : wildcard character, matches any character except for newline
# .* : match everything
# .*? : nongreedy fashion
# ^, $ : beginning / end
# re.IGNORECASE / re.I : case insensitive
# regex.sub(new, target_string)
# re.VERBOSE : ignore whitespace and comments in regex


import urllib.request

def decode_markdown(match_object):
    characters = match_object.group(1)
    # print(characters)
    if characters.startswith('x'):
        return chr(int(characters[1:], 16))
    else:
        return chr(int(characters))

# Create email regex.

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     # username
    \@
    [a-zA-Z0-9.-]+        # domain name
    \.
    [a-zA-Z]{2,}
    )''', re.VERBOSE)

email_hunt_url = 'http://cs1110.cs.virginia.edu/emails.html', \
                 'http://cs1110.cs.virginia.edu/emails.php'
stream = urllib.request.urlopen(email_hunt_url[1])

for line in stream:
    decoded = line.decode('UTF-8').strip()

    replace_at = [' at ', ' (at) ', ' (at)', '(at) ', '(at)']
    replace_dot = [' dot ', ' (dot) ', ' (dot)', '(dot) ', '(dot)']

    for at in replace_at:
        decoded = decoded.replace(at, '@')
    for dot in replace_dot:
        decoded = decoded.replace(dot, '.')

    decoded = decoded.replace('<br>', '')

    # Replaced by 'some_char's. Should be a better way to do this
    if 'replaced by' and '_' in decoded:
        decoded = decoded.replace('_', decoded[-3])

    if 'reversed' in decoded:
        decoded = decoded[::-1]

    if 'initial' in decoded:
        name_finder = re.compile(r'([A-Za-z]+)\s([A-Za-z]+)\.')
        name = name_finder.findall(decoded)
        first_name = name[0][0]
        last_initial = name[0][1][0]
        email_name = first_name + last_initial
        decoded = decoded.replace('first name plus my last initial', email_name)

    # Markdown encoding
    if '&#' in decoded:
        # decoded = ''.join(decoded.split("&#")[1:])
        # decoded = decoded.split('">')[1].replace('</a>', '')
        # decoded = decoded.replace('&#', '')
        # decoded_list = decoded.split(';')
        # new_list = []
        # for letter in decoded_list:
        #     base = 10
        #     if letter == '':
        #         continue
        #     elif 'x' in letter:
        #         base = 16
        #         letter = letter.replace('x', '')
        #     encoded_letter = chr(int(letter, base))
        #     new_list.append(encoded_letter)
        #
        # decoded = ''.join(new_list)
        decoded = re.sub('&#(.*?);', decode_markdown, decoded)

    result_list = emailRegex.findall(decoded)

    # Convert to set to return unique values
    result_set = set(result_list)

    # Check if line has reversed email address
    if len(result_set) != 0:
        for i in result_set:
            email_address = i
            if 'NOSPAM' in i:
                email_address = i.replace('NOSPAM', '')
            print(email_address)


