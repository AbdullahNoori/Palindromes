#!python


#returns boolean indicating whether pattern occurrs in text
def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    num = 0

    if len(pattern) == 0:
        return True
    for letter in text:
        if num > 0 and letter != pattern[num]:
            num = 0
        if letter == pattern[num]:
            num += 1
        if num > len(pattern)-1:
            return True

    return False 
     
#returns starting index of first occurannce of pattern in text 
def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    num = 0
    index = 0

    for text_index in range(len(text)):
        if text_index[text_index] == pattern[0]:
            for pattern_index in range(len(pattern)):
                if pattern[pattern_index] != text[text_index + pattern_index]:
                break
            if pattern_index == len(pattern) - 1:
                return text_index

    return None

#returns list of starting indexes 
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    index = []

    for letter_1 in range(len(text)):
        if len(pattern) == 0:
            index.append(letter_1)
            continue
        if text[letter_1] == pattern[0]:
            index.append(letter_1)
            letter_2 = letter_1
            for letter_3 in range(len(pattern)):
                if text[letter_2] != pattern[letter_3]:
                    del index[len(index)-1]
                    break
                elif letter_2 == len(text)-1 and letter_3 < len(pattern)-1:
                    del index[len(index)-1]
                    break
                elif letter_2 < len(text)-1:
                    letter_2 += 1
                    
    return index




def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()