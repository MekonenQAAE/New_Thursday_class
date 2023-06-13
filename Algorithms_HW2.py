'''
Split in Half
Given a string. Split it into two equal parts. Swap these parts and return the result.
If the string has odd characters, the first part should be one character greater than the second part.
Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
'''

def split_swap(str_0):
    length = len(str_0)
    str_1 = ''
    str_2 = ''
    if length % 2 == 0:
        str_1 = str_0[:(length // 2)]
        str_2 = str_0[(length // 2):]
    else:
        str_1 = str_0[:((length // 2) + 1)]
        str_2 = str_0[(length // 2) + 1:]

    return str_2 + str_1

print(split_swap('bbbbbcaaaaa'))

'''
Unique Characters in String
Given a string, determine if it consists of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.
'''
def unique(str_0):
    count = 0
    index = 0
    for elment in str_0:
        if elment in (str_0[:index] + str_0[index + 1:]):
            count += 1
        index += 1
    if count != 0:
        return False
    else:
        return True

print(unique('aabcde'))
