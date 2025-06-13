def word_count(text):
  return len(text.split())

def letter_count(text):
  char_count = {}
  lc_text = text.lower()
  for char in lc_text:
    if not char.isalpha():
      continue
    elif char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  
  return char_count

def sort_on(dict):
  return dict["num"]

def sort_dict(d):
  dict_list = []
  for char in d:
    dict_list.append({"char": char, "num": d[char]})
  dict_list.sort(reverse=True, key=sort_on)
  return dict_list
