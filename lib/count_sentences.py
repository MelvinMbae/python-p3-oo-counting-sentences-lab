#!/usr/bin/env python3

class MyString:
  def __init__(self, value=0):
    self._value = value
  
  def get_value(self):
    print("retrieving value")
    return self._value
  
  def set_value(self, value):
    if isinstance(value, str):
      print("setting value")
      self._value = value
      
    else:
      print("The value must be a string.")
      
  value = property(get_value, set_value,)
  
  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    if not self._value:
      return 0
    value2 = self._value.replace("." , "/").replace("!", "/").replace("?", "/").split("/")
    print(value2)
    valid_sentences = [sentence for sentence in value2 if sentence.strip()]
    print(valid_sentences)
    return len(valid_sentences) 

word = MyString("")
word.value
word.value = "one. two. three?"
word2 = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")

print(word.is_sentence())
print(word.is_question())
print(word.is_exclamation())
print(word.count_sentences())
print(word2.count_sentences())

