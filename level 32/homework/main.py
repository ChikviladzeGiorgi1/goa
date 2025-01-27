print(sentence_to_words("This is a sample sentence."))
def split_paragraph(paragraph):
    return paragraph.split('.')


print(split_paragraph("This is the first sentence. This is the second sentence."))
print(welcome_user("John", 25))
def format_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"

print(format_name("john", "doe"))
def reverse_string(sentence):
    reversed_str = sentence[::-1]
    return f"The reversed string is: {reversed_str}"

print(reverse_string("hello"))
def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return ' '.join(words)


print(insert_word("I love programming.", "Python", 2))
def sentence_to_words(sentence):
    return sentence.split()