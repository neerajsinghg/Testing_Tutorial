# first duplicate character

def first_dupli_char(text):
  seen = set()
  for ch in text:
    if ch not in seen:
      seen.add(ch)
    else:
      return ch
  return None

text = "automation"
print(first_dupli_char(text))

def first_dupli_char1(text):
  d={}
  for ch in text:
    d[ch]=d.get(ch,0)+1
  for k,v in d.items():
    if v>1:
      return k
  return None

text = "automation"
print(first_dupli_char1(text))