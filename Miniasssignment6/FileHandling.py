def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = max(words, key=len)
    return max_len

print(longest_word('a.txt')) #function call