# Count word frequency

def count_word_frequency(text):
    freq_dict = {}
    words = text.split()
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

def count_word_frequency1(text):
    freq_dict = {}
    words = text.split()
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

text = "the quick brown fox jumps over the lazy dog"
print(count_word_frequency(text))
print(count_word_frequency1(text))