#!/usr/bin/env python3

class MyString:
    def __init__(self, value='') -> None:
        self._value = value
  
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, strvalue):
        if not isinstance(strvalue, str):
            print("The value must be a string.")
        self._value = strvalue

    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self):
        value = self._value
        # Replace exclamation marks and question marks with periods
        for punc in ['!', '?']:
            value = value.replace(punc, '.')
        
        # Split the string by periods and filter out empty strings
        sentences = [s.strip() for s in value.split('.') if s.strip()]
        
        return len(sentences)


# Example usage
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  # => 3

print(string.is_sentence())      # => False
print(string.is_question())      # => True
print(string.is_exclamation())   # => False
