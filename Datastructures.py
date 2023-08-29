#Stacks 
def is_balanced(expression):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    
    return len(stack) == 0

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


#Sequences
def remove_duplicates(sequence):
    seen = set()
    result = []
    
    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)
    
    return result

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

 #Dictionaries
import string

def word_frequency(sentence):
    words = sentence.split()
    word_freq = {}

    for word in words:
        # Remove punctuation and convert to lowercase
        cleaned_word = word.strip(string.punctuation).lower()
        if cleaned_word:
            word_freq[cleaned_word] = word_freq.get(cleaned_word, 0) + 1
    
    return word_freq

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
