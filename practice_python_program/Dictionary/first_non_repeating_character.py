# first non-repeating character

def first_no_rep_char(text):
  d={}
  first=''
  for ch in text:
    d[ch]=d.get(ch,0)+1
  for k,v in d.items():
    if v==1:
      first=k
      break
  return first

text = "aabbcde"
print(first_no_rep_char(text))

def first_no_rep_char1(text):
  d={}
  for ch in text:
    d[ch]=d.get(ch,0)+1
  for k,v in d.items():
    if v==1:
      return k
  return None

text = "aabbcde"
print(first_no_rep_char1(text))
