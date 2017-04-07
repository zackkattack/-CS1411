import string
original_str = input('Input a string:')
modified_str = original_str.lower()

bad_chars = string.whitespace + string.punctuation
good_chars = ''

for i in modified_str:
    if bad_chars.find(i) == -1:
        good_chars += i

if good_chars == good_chars[::-1]:
    print(\
    'The original string is: {}\n\
    the modified string is: {}\n\
    the reversal is: {}\n\
    String is a palidrome'.format(original_str, good_chars, good_chars[::-1]))
else:
    print(\
    'The original string is: {}\n\
    the modified string is: {}\n\
    the reversal is: {}\n\
    String is not a palidrome'.format(original_str, good_chars, good_chars[::-1]))
