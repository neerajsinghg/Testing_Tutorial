def invert_dict(data):
  invert= {value:key for key, value in data.items()}
  return invert 
  
data={
      "a": 1,
      "b": 2,
      "c": 3
  }
print(invert_dict(data))