# Count frequency of characters using dictionary

def count_freq_of_char(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def count_freq_of_char1(text):
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

text = "automation"
print(count_freq_of_char(text))
print(count_freq_of_char1(text))