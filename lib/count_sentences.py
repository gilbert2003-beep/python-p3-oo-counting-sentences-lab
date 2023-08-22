import re

class MyString:
    def __init__(self, value=''):
        # Verify that the value is a string before assigning it
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value
    
    def is_sentence(self):
        # Check if the value ends with a period
        return self.value.endswith('.')

    def is_question(self):
        # Check if the value ends with a question mark
        return self.value.endswith('?')

    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the value into sentences using regular expressions
        sentences = re.split(r'[.!?]', self.value)
        # Remove any empty strings from the list
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)

# Testing the MyString class
simple_string = MyString("This is a sentence.")
print(simple_string.is_sentence())  # Output: True
print(simple_string.is_question())  # Output: False
print(simple_string.is_exclamation())  # Output: False
print(simple_string.count_sentences())  # Output: 1

complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(complex_string.count_sentences())  # Output: 4
