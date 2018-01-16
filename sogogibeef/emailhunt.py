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
    # reversed_line = decoded[::-1]
    decoded = decoded.replace(' at ', '@').replace(' (at) ', '@')
    decoded = decoded.replace(' (at)', '@').replace('(at) ', '@')
    decoded = decoded.replace('(at)', '@')
    decoded = decoded.replace(' dot ', '.').replace(' (dot) ', '.')
    decoded = decoded.replace(' (dot)', '.').replace('(dot) ', '.')
    decoded = decoded.replace('(dot)', '.')
    result_list = emailRegex.findall(decoded)
    
    # Convert to set to return unique values
    result_set = set(result_list)
    if len(result_set) != 0:
        for i in result_set:
            email_address = i
            if 'NOSPAM' in i:
                email_address = i.replace('NOSPAM', '')
            print(email_address)
