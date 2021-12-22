# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

i = 0
symbol = 0
word = 0
length_string = len(text)

while i < length_string:
    if text[i] != " ":
        symbol += 1
    else:
        symbol = 0
    if symbol == 6:
        word += 1
    i += 1
print("Number of words per line =", word)
