import pandas as pd

sentence = "Python Automationnn"
s = pd.Series(list(sentence))
print(s)
char_count = s.value_counts()
print(char_count)
char_count = s.value_counts()

max_char = char_count.idxmax()
max_count = char_count.max()

print({max_char: max_count})