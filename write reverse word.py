
def reverse_text(text):
    return text[::-1]

# Example usage
input_text = "amgad"
reversed_text = reverse_text(input_text)
print(reversed_text)


print ("=====way 2====≠=")

def reverse_word(text):
    reversed_word = ""
    for char in text:
        reversed_word = char + reversed_word
    return reversed_word

# Example usage
input_word = "reverse text"
reversed_word = reverse_word(input_word)
print(reversed_word)



print("====way 3=====")
a = "hello"
print(a[::-1])