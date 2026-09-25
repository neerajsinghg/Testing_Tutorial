# Group words by their first character

words = ["apple", "ant", "ball", "bat", "cat"]

def group_words_by_first_char(words):
    grouped_dict = {}
    for word in words:
        first_char = word[0]
        if first_char in grouped_dict:
            grouped_dict[first_char].append(word)
        else:
            grouped_dict[first_char] = [word]
    return grouped_dict

print(group_words_by_first_char(words))