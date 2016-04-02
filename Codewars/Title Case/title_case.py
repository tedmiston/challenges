"""
Codewars - Title Case

http://www.codewars.com/kata/5202ef17a402dd033c000009
"""


def title_case(s, minor_words=''):
    if len(s.split()) == 0:
        return s

    words = s.split()
    first = words[0].capitalize()
    rest = words[1:]

    exceptions = minor_words.lower().split()

    for idx, w in enumerate(rest):
        rest[idx] = w.lower() if w.lower() in exceptions else w.capitalize()

    return ' '.join([first] + rest)


assert title_case('') == ''
assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
assert title_case('THE WIND IN THE WILLOWS',
                  'The In') == 'The Wind in the Willows'
assert title_case('the quick brown fox') == 'The Quick Brown Fox'
